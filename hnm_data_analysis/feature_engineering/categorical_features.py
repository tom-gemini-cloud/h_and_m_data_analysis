"""
Categorical Feature Engineering for Articles Data

This module provides comprehensive categorical feature engineering for H&M articles data,
preparing categorical variables for clustering by creating encoded representations that
can be combined with TF-IDF text features.

Key capabilities:
- One-hot encoding for nominal categories
- Target encoding for high-cardinality categories  
- Ordinal encoding for ordinal categories
- Feature scaling and normalisation
- Integration with TF-IDF features for unified clustering
"""

from __future__ import annotations

import os
import json
import warnings
from typing import Any, Dict, List, Optional, Tuple, Union
from dataclasses import dataclass, asdict

import joblib
import polars as pl
import numpy as np
from scipy.sparse import csr_matrix, hstack, save_npz
from sklearn.preprocessing import (
    OneHotEncoder, 
    LabelEncoder, 
    StandardScaler,
    MinMaxScaler
)
from sklearn.compose import ColumnTransformer


@dataclass
class CategoricalEncodingConfig:
    """Configuration for categorical encoding strategies."""
    onehot_categories: List[str]
    target_categories: List[str]  # For target encoding (if we have targets)
    ordinal_categories: Dict[str, List[str]]  # category -> ordered values
    drop_categories: List[str]  # Categories to exclude
    max_categories_onehot: int = 50  # Max unique values for one-hot encoding
    min_frequency_threshold: float = 0.001  # Min frequency to include category
    

class ArticleCategoricalEncoder:
    """
    Encode categorical features from articles data for clustering.
    
    This class transforms categorical article features into numerical representations
    suitable for clustering algorithms, with options for different encoding strategies
    based on the nature of each categorical variable.
    """
    
    def __init__(
        self,
        input_path: Optional[str] = None,
        id_column: str = "article_id",
        encoding_strategy: str = "mixed",  # 'onehot', 'target', 'mixed'
        handle_rare_categories: str = "group",  # 'group', 'drop', 'keep'
        rare_threshold: float = 0.001,
    ):
        """
        Initialise the categorical encoder.
        
        Args:
            input_path: Path to articles dataset
            id_column: Column name for article IDs
            encoding_strategy: Strategy for encoding ('onehot', 'target', 'mixed')
            handle_rare_categories: How to handle rare categories
            rare_threshold: Threshold for considering categories as rare
        """
        self.input_path = input_path
        self.id_column = id_column
        self.encoding_strategy = encoding_strategy
        self.handle_rare_categories = handle_rare_categories
        self.rare_threshold = rare_threshold
        
        self.df: Optional[pl.DataFrame] = None
        self.article_ids: List[Any] = []
        self.encoded_features: Optional[np.ndarray] = None
        self.feature_names: List[str] = []
        
        self.encoders: Dict[str, Any] = {}
        self.scaler: Optional[StandardScaler] = None
        self.encoding_config: Optional[CategoricalEncodingConfig] = None
        
    def _auto_detect_input(self) -> Optional[str]:
        """Try to find a reasonable default input if none provided."""
        base = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        candidates = [
            os.path.join(base, "data", "cleaned", "articles_last_3_months_cleaned.parquet"),
            os.path.join(base, "data", "processed", "articles_last_3_months.parquet"),
            os.path.join(base, "data", "cleaned", "articles_last_3_months_cleaned.csv"),
            os.path.join(base, "data", "processed", "articles_last_3_months.csv"),
            os.path.join(base, "data", "raw", "articles.csv"),
        ]
        for p in candidates:
            if os.path.exists(p):
                return p
        return None
        
    def load_data(self) -> pl.DataFrame:
        """Load articles data and prepare for encoding."""
        path = self.input_path or self._auto_detect_input()
        if path is None:
            raise FileNotFoundError(
                "No input path provided and no default articles file found in data/."
            )
        self.input_path = path
        
        print(f"Loading articles from: {path}")
        if path.endswith(".parquet"):
            df = pl.read_parquet(path)
        else:
            df = pl.read_csv(path)
            
        if self.id_column not in df.columns:
            raise KeyError(f"Input data must contain column '{self.id_column}'.")
            
        self.df = df
        self.article_ids = df.get_column(self.id_column).to_list()
        print(f"Loaded {df.height:,} articles with {len(df.columns)} columns")
        return df
        
    def _get_categorical_columns(self) -> List[str]:
        """Identify categorical columns for encoding."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        categorical_cols = []
        
        # Find columns that are categorical or string type
        for col in self.df.columns:
            if col == self.id_column:
                continue
                
            dtype = self.df[col].dtype
            if dtype in [pl.Categorical, pl.Utf8]:
                categorical_cols.append(col)
            elif dtype in [pl.Int64, pl.Int32] and col.endswith(('_no', '_id', '_code')):
                # Treat ID/code columns as categorical
                categorical_cols.append(col)
                
        return categorical_cols
        
    def _create_encoding_config(self, categorical_cols: List[str]) -> CategoricalEncodingConfig:
        """Create encoding configuration based on data characteristics."""
        if self.df is None:
            raise ValueError("Data not loaded.")
            
        onehot_categories = []
        target_categories = []  # We'll use these for label encoding instead
        ordinal_categories = {}
        drop_categories = []
        
        for col in categorical_cols:
            unique_count = self.df[col].n_unique()
            total_count = len(self.df)
            
            # Skip columns with too many unique values
            if unique_count > 1000:
                print(f"Dropping {col}: too many unique values ({unique_count})")
                drop_categories.append(col)
                continue
                
            # Skip columns with mostly unique values (like product names)
            if unique_count / total_count > 0.8:
                print(f"Dropping {col}: too sparse ({unique_count}/{total_count})")
                drop_categories.append(col)
                continue
                
            # Use one-hot encoding for reasonable number of categories
            if unique_count <= 50:
                onehot_categories.append(col)
            else:
                # Use label encoding for higher cardinality
                target_categories.append(col)
                
        # Define ordinal categories if any exist
        # For now, we'll treat colour_value as ordinal if it exists
        if 'perceived_colour_value_name' in categorical_cols:
            # These seem to have a natural order from light to dark
            ordinal_categories['perceived_colour_value_name'] = [
                'Light', 'Dusty Light', 'Medium', 'Medium Dusty', 'Dark'
            ]
            if 'perceived_colour_value_name' in onehot_categories:
                onehot_categories.remove('perceived_colour_value_name')
                
        config = CategoricalEncodingConfig(
            onehot_categories=onehot_categories,
            target_categories=target_categories,
            ordinal_categories=ordinal_categories,
            drop_categories=drop_categories,
            max_categories_onehot=50,
            min_frequency_threshold=self.rare_threshold
        )
        
        return config
        
    def _handle_rare_categories(self, df: pl.DataFrame, col: str) -> pl.DataFrame:
        """Handle rare categories in a column."""
        if self.handle_rare_categories == "keep":
            return df
            
        # Calculate value counts
        value_counts = df[col].value_counts().sort("count", descending=True)
        total_count = len(df)
        
        # Find categories below threshold
        rare_mask = value_counts["count"] < (self.rare_threshold * total_count)
        rare_categories = value_counts.filter(rare_mask)[col].to_list()
        
        if not rare_categories:
            return df
            
        if self.handle_rare_categories == "group":
            # Group rare categories as "Other"
            df = df.with_columns(
                pl.when(pl.col(col).is_in(rare_categories))
                .then(pl.lit("Other"))
                .otherwise(pl.col(col))
                .alias(col)
            )
            print(f"Grouped {len(rare_categories)} rare categories in {col} as 'Other'")
        elif self.handle_rare_categories == "drop":
            # Drop rows with rare categories
            original_count = len(df)
            df = df.filter(~pl.col(col).is_in(rare_categories))
            dropped_count = original_count - len(df)
            print(f"Dropped {dropped_count} rows with rare categories in {col}")
            
        return df
        
    def _encode_onehot_features(self, df: pl.DataFrame, columns: List[str]) -> Tuple[np.ndarray, List[str]]:
        """Encode features using one-hot encoding."""
        if not columns:
            return np.empty((len(df), 0)), []
            
        # Handle rare categories
        for col in columns:
            df = self._handle_rare_categories(df, col)
            
        # Convert to pandas for sklearn
        data = df.select(columns).to_pandas()
        
        # One-hot encode
        encoder = OneHotEncoder(sparse_output=True, handle_unknown="ignore")
        encoded = encoder.fit_transform(data)
        
        # Generate feature names
        feature_names = []
        for i, col in enumerate(columns):
            categories = encoder.categories_[i]
            for cat in categories:
                feature_names.append(f"{col}_{cat}")
                
        self.encoders["onehot"] = encoder
        print(f"One-hot encoded {len(columns)} columns into {encoded.shape[1]} features")
        
        return encoded.toarray(), feature_names
        
    def _encode_label_features(self, df: pl.DataFrame, columns: List[str]) -> Tuple[np.ndarray, List[str]]:
        """Encode features using label encoding."""
        if not columns:
            return np.empty((len(df), 0)), []
            
        encoded_data = []
        feature_names = []
        
        for col in columns:
            # Handle rare categories
            df = self._handle_rare_categories(df, col)
            
            # Label encode
            encoder = LabelEncoder()
            values = df[col].to_pandas().astype(str)
            encoded_values = encoder.fit_transform(values)
            
            encoded_data.append(encoded_values.reshape(-1, 1))
            feature_names.append(f"{col}_encoded")
            self.encoders[f"label_{col}"] = encoder
            
        if encoded_data:
            result = np.hstack(encoded_data)
            print(f"Label encoded {len(columns)} columns into {result.shape[1]} features")
            return result, feature_names
        else:
            return np.empty((len(df), 0)), []
            
    def _encode_ordinal_features(self, df: pl.DataFrame, ordinal_config: Dict[str, List[str]]) -> Tuple[np.ndarray, List[str]]:
        """Encode ordinal features with specified order."""
        if not ordinal_config:
            return np.empty((len(df), 0)), []
            
        encoded_data = []
        feature_names = []
        
        for col, ordered_values in ordinal_config.items():
            if col not in df.columns:
                continue
                
            # Create mapping from category to ordinal value
            ordinal_map = {cat: i for i, cat in enumerate(ordered_values)}
            
            # Handle categories not in the predefined order
            unique_values = df[col].unique().to_list()
            missing_values = [v for v in unique_values if v not in ordinal_map]
            
            if missing_values:
                print(f"Warning: {col} contains values not in ordinal mapping: {missing_values}")
                # Assign them to the end of the order
                for i, val in enumerate(missing_values):
                    ordinal_map[val] = len(ordered_values) + i
                    
            # Apply mapping
            encoded_values = df[col].map_dict(ordinal_map).to_numpy()
            encoded_data.append(encoded_values.reshape(-1, 1))
            feature_names.append(f"{col}_ordinal")
            self.encoders[f"ordinal_{col}"] = ordinal_map
            
        if encoded_data:
            result = np.hstack(encoded_data)
            print(f"Ordinal encoded {len(ordinal_config)} columns into {result.shape[1]} features")
            return result, feature_names
        else:
            return np.empty((len(df), 0)), []
            
    def fit_transform(self, scale_features: bool = True) -> np.ndarray:
        """Fit encoders and transform categorical features."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Get categorical columns
        categorical_cols = self._get_categorical_columns()
        print(f"Found {len(categorical_cols)} categorical columns: {categorical_cols}")
        
        # Create encoding configuration
        self.encoding_config = self._create_encoding_config(categorical_cols)
        print(f"Encoding config: {len(self.encoding_config.onehot_categories)} one-hot, "
              f"{len(self.encoding_config.target_categories)} label, "
              f"{len(self.encoding_config.ordinal_categories)} ordinal")
        
        # Encode different types of features
        encoded_parts = []
        all_feature_names = []
        
        # One-hot encoding
        if self.encoding_config.onehot_categories:
            onehot_features, onehot_names = self._encode_onehot_features(
                self.df, self.encoding_config.onehot_categories
            )
            if onehot_features.shape[1] > 0:
                encoded_parts.append(onehot_features)
                all_feature_names.extend(onehot_names)
                
        # Label encoding
        if self.encoding_config.target_categories:
            label_features, label_names = self._encode_label_features(
                self.df, self.encoding_config.target_categories  
            )
            if label_features.shape[1] > 0:
                encoded_parts.append(label_features)
                all_feature_names.extend(label_names)
                
        # Ordinal encoding
        if self.encoding_config.ordinal_categories:
            ordinal_features, ordinal_names = self._encode_ordinal_features(
                self.df, self.encoding_config.ordinal_categories
            )
            if ordinal_features.shape[1] > 0:
                encoded_parts.append(ordinal_features)
                all_feature_names.extend(ordinal_names)
                
        if not encoded_parts:
            raise ValueError("No categorical features could be encoded.")
            
        # Combine all encoded features
        self.encoded_features = np.hstack(encoded_parts)
        self.feature_names = all_feature_names
        
        # Scale features if requested
        if scale_features:
            self.scaler = StandardScaler()
            self.encoded_features = self.scaler.fit_transform(self.encoded_features)
            print("Applied standard scaling to categorical features")
            
        print(f"Final categorical feature matrix: {self.encoded_features.shape[0]:,} x {self.encoded_features.shape[1]:,}")
        return self.encoded_features
        
    def save_features(self, output_dir: str) -> None:
        """Save encoded categorical features and metadata."""
        if self.encoded_features is None:
            raise ValueError("No features to save. Call fit_transform() first.")
            
        os.makedirs(output_dir, exist_ok=True)
        
        # Save encoded features as numpy array
        features_path = os.path.join(output_dir, "categorical_features.npy")
        np.save(features_path, self.encoded_features)
        print(f"Saved categorical features to: {features_path}")
        
        # Save article ID index
        index_path = os.path.join(output_dir, "categorical_article_id_index.csv")
        pl.DataFrame({self.id_column: self.article_ids}).write_csv(index_path)
        print(f"Saved article ID index to: {index_path}")
        
        # Save feature names
        names_path = os.path.join(output_dir, "categorical_feature_names.json")
        with open(names_path, "w") as f:
            json.dump(self.feature_names, f, indent=2)
        print(f"Saved feature names to: {names_path}")
        
        # Save encoders
        encoders_path = os.path.join(output_dir, "categorical_encoders.joblib")
        joblib.dump(self.encoders, encoders_path)
        print(f"Saved encoders to: {encoders_path}")
        
        if self.scaler is not None:
            scaler_path = os.path.join(output_dir, "categorical_scaler.joblib")
            joblib.dump(self.scaler, scaler_path)
            print(f"Saved scaler to: {scaler_path}")
            
        # Save configuration
        config_path = os.path.join(output_dir, "categorical_config.json")
        config_dict = {
            "input_path": self.input_path,
            "id_column": self.id_column,
            "encoding_strategy": self.encoding_strategy,
            "handle_rare_categories": self.handle_rare_categories,
            "rare_threshold": self.rare_threshold,
            "encoding_config": asdict(self.encoding_config) if self.encoding_config else None,
            "feature_count": len(self.feature_names),
            "article_count": len(self.article_ids)
        }
        with open(config_path, "w") as f:
            json.dump(config_dict, f, indent=2)
        print(f"Saved configuration to: {config_path}")


class CombinedFeatureProcessor:
    """
    Combine TF-IDF text features with categorical features for unified clustering.
    
    This class loads pre-computed TF-IDF features and categorical features,
    aligns them by article_id, and creates combined feature matrices suitable
    for clustering algorithms.
    """
    
    def __init__(self, tfidf_dir: str, categorical_dir: str):
        """
        Initialise with paths to TF-IDF and categorical feature directories.
        
        Args:
            tfidf_dir: Directory containing TF-IDF features
            categorical_dir: Directory containing categorical features
        """
        self.tfidf_dir = tfidf_dir
        self.categorical_dir = categorical_dir
        
        self.tfidf_features: Optional[csr_matrix] = None
        self.categorical_features: Optional[np.ndarray] = None
        self.combined_features: Optional[np.ndarray] = None
        self.article_ids: Optional[List[Any]] = None
        self.feature_names: List[str] = []
        
    def load_tfidf_features(self) -> Tuple[csr_matrix, List[Any]]:
        """Load TF-IDF features and article IDs."""
        # Load TF-IDF matrix
        tfidf_path = os.path.join(self.tfidf_dir, "tfidf_features.npz")
        if not os.path.exists(tfidf_path):
            raise FileNotFoundError(f"TF-IDF features not found at {tfidf_path}")
            
        from scipy.sparse import load_npz
        self.tfidf_features = load_npz(tfidf_path)
        
        # Load article ID index
        index_path = os.path.join(self.tfidf_dir, "article_id_index.csv")
        if not os.path.exists(index_path):
            raise FileNotFoundError(f"Article ID index not found at {index_path}")
            
        tfidf_ids = pl.read_csv(index_path).get_column("article_id").to_list()
        
        print(f"Loaded TF-IDF features: {self.tfidf_features.shape[0]:,} x {self.tfidf_features.shape[1]:,}")
        return self.tfidf_features, tfidf_ids
        
    def load_categorical_features(self) -> Tuple[np.ndarray, List[Any]]:
        """Load categorical features and article IDs."""
        # Load categorical features
        features_path = os.path.join(self.categorical_dir, "categorical_features.npy")
        if not os.path.exists(features_path):
            raise FileNotFoundError(f"Categorical features not found at {features_path}")
            
        self.categorical_features = np.load(features_path)
        
        # Load article ID index
        index_path = os.path.join(self.categorical_dir, "categorical_article_id_index.csv")
        if not os.path.exists(index_path):
            raise FileNotFoundError(f"Categorical article ID index not found at {index_path}")
            
        categorical_ids = pl.read_csv(index_path).get_column("article_id").to_list()
        
        print(f"Loaded categorical features: {self.categorical_features.shape[0]:,} x {self.categorical_features.shape[1]:,}")
        return self.categorical_features, categorical_ids
        
    def combine_features(self, tfidf_weight: float = 0.7, categorical_weight: float = 0.3) -> np.ndarray:
        """
        Combine TF-IDF and categorical features with specified weights.
        
        Args:
            tfidf_weight: Weight for TF-IDF features
            categorical_weight: Weight for categorical features
            
        Returns:
            Combined feature matrix aligned by article_id
        """
        # Load features if not already loaded
        if self.tfidf_features is None:
            tfidf_features, tfidf_ids = self.load_tfidf_features()
        else:
            tfidf_ids = self.article_ids
            
        if self.categorical_features is None:
            categorical_features, categorical_ids = self.load_categorical_features()
        else:
            categorical_ids = self.article_ids
            
        # Find common article IDs
        tfidf_id_set = set(tfidf_ids)
        categorical_id_set = set(categorical_ids)
        common_ids = tfidf_id_set.intersection(categorical_id_set)
        
        if not common_ids:
            raise ValueError("No common article IDs found between TF-IDF and categorical features")
            
        print(f"Found {len(common_ids):,} common articles between TF-IDF and categorical features")
        
        # Create mapping for alignment
        tfidf_id_to_idx = {aid: idx for idx, aid in enumerate(tfidf_ids)}
        categorical_id_to_idx = {aid: idx for idx, aid in enumerate(categorical_ids)}
        
        # Align features
        common_ids_list = list(common_ids)
        tfidf_indices = [tfidf_id_to_idx[aid] for aid in common_ids_list]
        categorical_indices = [categorical_id_to_idx[aid] for aid in common_ids_list]
        
        # Extract aligned features
        aligned_tfidf = self.tfidf_features[tfidf_indices].toarray()
        aligned_categorical = self.categorical_features[categorical_indices]
        
        # Normalise features to unit scale for fair combination
        from sklearn.preprocessing import StandardScaler
        
        tfidf_scaler = StandardScaler()
        aligned_tfidf_scaled = tfidf_scaler.fit_transform(aligned_tfidf)
        
        categorical_scaler = StandardScaler()
        aligned_categorical_scaled = categorical_scaler.fit_transform(aligned_categorical)
        
        # Apply weights and combine
        weighted_tfidf = aligned_tfidf_scaled * tfidf_weight
        weighted_categorical = aligned_categorical_scaled * categorical_weight
        
        self.combined_features = np.hstack([weighted_tfidf, weighted_categorical])
        self.article_ids = common_ids_list
        
        print(f"Combined features shape: {self.combined_features.shape[0]:,} x {self.combined_features.shape[1]:,}")
        print(f"TF-IDF contribution: {weighted_tfidf.shape[1]:,} features (weight: {tfidf_weight})")
        print(f"Categorical contribution: {weighted_categorical.shape[1]:,} features (weight: {categorical_weight})")
        
        return self.combined_features
        
    def save_combined_features(self, output_dir: str) -> None:
        """Save combined features for clustering."""
        if self.combined_features is None:
            raise ValueError("No combined features to save. Call combine_features() first.")
            
        os.makedirs(output_dir, exist_ok=True)
        
        # Save combined features
        features_path = os.path.join(output_dir, "combined_features.npy")
        np.save(features_path, self.combined_features)
        print(f"Saved combined features to: {features_path}")
        
        # Save article ID index
        index_path = os.path.join(output_dir, "combined_article_id_index.csv")
        pl.DataFrame({"article_id": self.article_ids}).write_csv(index_path)
        print(f"Saved article ID index to: {index_path}")
        
        # Save metadata
        metadata = {
            "tfidf_dir": self.tfidf_dir,
            "categorical_dir": self.categorical_dir,
            "feature_shape": list(self.combined_features.shape),
            "article_count": len(self.article_ids)
        }
        metadata_path = os.path.join(output_dir, "combined_features_metadata.json")
        with open(metadata_path, "w") as f:
            json.dump(metadata, f, indent=2)
        print(f"Saved metadata to: {metadata_path}")


def main():
    """Example usage of categorical feature encoding."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Encode categorical features from articles data")
    parser.add_argument("--input-path", type=str, help="Path to articles dataset")
    parser.add_argument("--output-dir", type=str, default="../data/processed/categorical_features",
                       help="Output directory for categorical features")
    parser.add_argument("--encoding-strategy", type=str, default="mixed", 
                       choices=["onehot", "target", "mixed"],
                       help="Encoding strategy for categorical variables")
    parser.add_argument("--rare-threshold", type=float, default=0.001,
                       help="Threshold for rare category handling")
    parser.add_argument("--handle-rare", type=str, default="group",
                       choices=["group", "drop", "keep"],
                       help="How to handle rare categories")
    parser.add_argument("--no-scaling", action="store_true",
                       help="Skip feature scaling")
    
    args = parser.parse_args()
    
    # Encode categorical features
    encoder = ArticleCategoricalEncoder(
        input_path=args.input_path,
        encoding_strategy=args.encoding_strategy,
        handle_rare_categories=args.handle_rare,
        rare_threshold=args.rare_threshold
    )
    
    encoder.load_data()
    encoder.fit_transform(scale_features=not args.no_scaling)
    encoder.save_features(args.output_dir)
    
    print("\nCategorical feature encoding completed successfully!")


if __name__ == "__main__":
    main()
