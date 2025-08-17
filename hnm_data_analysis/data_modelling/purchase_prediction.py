"""
Purchase Prediction Model

Implements classification models to predict whether a customer will
purchase a specific product based on customer and product features.

Author: Claude Code
Date: 2025-08-15
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, classification_report, confusion_matrix
)
from typing import Dict, List, Tuple, Optional, Any, Union
import pickle
import warnings
warnings.filterwarnings('ignore')


class PurchasePredictionModel:
    """
    Purchase prediction model using classification algorithms.
    
    This model predicts the likelihood of a customer purchasing a specific
    product based on customer demographics, behaviour, and product features.
    """
    
    def __init__(self, test_size: float = 0.2, random_state: int = 42, max_samples: int = 20000):
        """
        Initialise the purchase prediction model.
        
        Args:
            test_size: Proportion of data for validation split
            random_state: Random seed for reproducibility
            max_samples: Maximum number of samples to use for training (for speed)
        """
        self.test_size = test_size
        self.random_state = random_state
        self.max_samples = max_samples
        
        # Feature definitions
        self.numerical_features = [
            'price', 'age', 'recency', 'frequency', 'monetary',
            'purchase_diversity_score', 'price_sensitivity_index',
            'colour_preference_entropy', 'style_consistency_score'
        ]
        
        self.categorical_features = [
            'club_member_status', 'fashion_news_frequency', 'sales_channel_id',
            'product_type_name', 'colour_group_name', 'department_name'
        ]
        
        # Model components
        self.models = {}
        self.scaler = None
        self.label_encoders = {}
        self.feature_columns = None
        self.model_scores = {}
        
        # Model fitted flag
        self.is_fitted = False
    
    def create_negative_samples(self, positive_df: pd.DataFrame, n_negative: int = 10000) -> pd.DataFrame:
        """
        Create negative samples for balanced training.
        
        Args:
            positive_df: DataFrame with positive purchase examples
            n_negative: Number of negative samples to create
            
        Returns:
            DataFrame with negative purchase examples
        """
        print(f"Creating {n_negative:,} negative samples...")
        
        # Get unique customers and articles
        all_customers = positive_df['customer_id'].unique()
        all_articles = positive_df['article_id'].unique()
        
        # Create set of positive pairs for exclusion
        positive_pairs = set(zip(positive_df['customer_id'], positive_df['article_id']))
        
        # Generate random customer-article pairs
        negative_samples = []
        max_attempts = n_negative * 3  # Avoid infinite loops
        attempts = 0
        
        while len(negative_samples) < n_negative and attempts < max_attempts:
            customer_id = np.random.choice(all_customers)
            article_id = np.random.choice(all_articles)
            
            if (customer_id, article_id) not in positive_pairs:
                negative_samples.append((customer_id, article_id))
            
            attempts += 1
        
        print(f"Generated {len(negative_samples):,} negative samples after {attempts} attempts")
        
        # Create negative samples dataframe more efficiently
        if not negative_samples:
            print("Warning: Could not create negative samples")
            return pd.DataFrame()
        
        # Create lookup dictionaries for faster access
        customer_features = positive_df.drop_duplicates(subset=['customer_id']).set_index('customer_id')
        article_features = positive_df.drop_duplicates(subset=['article_id']).set_index('article_id')
        
        negative_df_list = []
        
        for customer_id, article_id in negative_samples[:n_negative]:  # Limit to requested number
            if customer_id not in customer_features.index or article_id not in article_features.index:
                continue
                
            # Get customer and article features
            customer_row = customer_features.loc[customer_id].copy()
            article_row = article_features.loc[article_id]
            
            # Update article-specific features
            article_feature_cols = ['product_type_name', 'product_group_name', 'colour_group_name',
                                  'department_name', 'section_name', 'garment_group_name']
            
            for feature in article_feature_cols:
                if feature in article_row.index:
                    customer_row[feature] = article_row[feature]
            
            # Set the article_id
            customer_row['article_id'] = article_id
            negative_df_list.append(customer_row)
        
        if not negative_df_list:
            print("Warning: Could not create negative samples")
            return pd.DataFrame()
        
        negative_df = pd.DataFrame(negative_df_list)
        negative_df['purchased'] = 0
        
        print(f"Created negative samples dataframe: {negative_df.shape}")
        return negative_df
    
    def prepare_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Prepare features for model training.
        
        Args:
            df: Input dataframe with features
            
        Returns:
            Processed feature dataframe
        """
        # Select available features
        available_numerical = [col for col in self.numerical_features if col in df.columns]
        available_categorical = [col for col in self.categorical_features if col in df.columns]
        
        all_features = available_numerical + available_categorical
        feature_df = df[all_features].copy()
        
        print(f"Using {len(available_numerical)} numerical and {len(available_categorical)} categorical features")
        print(f"Features: {all_features}")
        
        # Handle missing values
        for col in available_numerical:
            feature_df[col] = feature_df[col].fillna(feature_df[col].median())
        
        for col in available_categorical:
            feature_df[col] = feature_df[col].fillna('Unknown')
        
        return feature_df
    
    def fit(self, train_df: pd.DataFrame, balance_data: bool = True, n_negative_samples: int = 5000) -> 'PurchasePredictionModel':
        """
        Fit the purchase prediction models on training data.
        
        Args:
            train_df: Training dataframe with features and interactions
            balance_data: Whether to create balanced dataset with negative samples
            n_negative_samples: Number of negative samples to create
            
        Returns:
            Fitted model instance
        """
        print("=== Training Purchase Prediction Models ===")
        
        # Prepare positive samples (with sampling for speed)
        positive_samples = train_df.copy()
        
        # Sample data if it's too large
        if len(positive_samples) > self.max_samples:
            print(f"Sampling {self.max_samples:,} from {len(positive_samples):,} transactions for speed")
            positive_samples = positive_samples.sample(n=self.max_samples, random_state=self.random_state)
        
        positive_samples['purchased'] = 1
        print(f"Positive samples (actual purchases): {len(positive_samples):,}")
        
        # Create balanced dataset
        if balance_data:
            # Create negative samples
            negative_samples = self.create_negative_samples(positive_samples, n_negative_samples)
            
            if negative_samples.empty:
                print("Warning: Using only positive samples (unbalanced)")
                classification_data = positive_samples
            else:
                # Combine positive and negative samples
                classification_data = pd.concat([
                    positive_samples.sample(n=min(len(positive_samples), len(negative_samples)), 
                                          random_state=self.random_state),
                    negative_samples
                ], ignore_index=True)
        else:
            classification_data = positive_samples
        
        print(f"Combined classification dataset: {classification_data.shape}")
        print(f"Class distribution:")
        print(classification_data['purchased'].value_counts())
        
        # Prepare features
        features_df = self.prepare_features(classification_data)
        self.feature_columns = features_df.columns.tolist()
        
        # Encode categorical variables
        print("Encoding categorical variables...")
        encoded_features = features_df.copy()
        
        available_categorical = [col for col in self.categorical_features if col in encoded_features.columns]
        
        for col in available_categorical:
            le = LabelEncoder()
            encoded_features[col] = le.fit_transform(encoded_features[col].astype(str))
            self.label_encoders[col] = le
        
        # Scale numerical features
        available_numerical = [col for col in self.numerical_features if col in encoded_features.columns]
        
        self.scaler = StandardScaler()
        encoded_features[available_numerical] = self.scaler.fit_transform(encoded_features[available_numerical])
        
        # Prepare target and feature matrices
        y = classification_data['purchased']
        X = encoded_features
        
        print(f"Final feature matrix shape: {X.shape}")
        
        # Split into train and validation sets
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state, 
            stratify=y if len(y.unique()) > 1 else None
        )
        
        print(f"Training set: {X_train.shape}")
        print(f"Validation set: {X_val.shape}")
        
        # Define models to train (optimized for speed)
        model_configs = {
            'Logistic Regression': LogisticRegression(random_state=self.random_state, max_iter=500),
            'Random Forest': RandomForestClassifier(n_estimators=50, max_depth=10, random_state=self.random_state, n_jobs=-1),
        }
        
        # Train models
        for name, model in model_configs.items():
            print(f"\nTraining {name}...")
            
            # Train model
            model.fit(X_train, y_train)
            
            # Make predictions
            y_pred = model.predict(X_val)
            y_pred_proba = model.predict_proba(X_val)[:, 1] if hasattr(model, 'predict_proba') else y_pred
            
            # Calculate metrics
            accuracy = accuracy_score(y_val, y_pred)
            precision = precision_score(y_val, y_pred, zero_division=0)
            recall = recall_score(y_val, y_pred, zero_division=0)
            f1 = f1_score(y_val, y_pred, zero_division=0)
            
            try:
                auc = roc_auc_score(y_val, y_pred_proba)
            except ValueError:
                auc = 0.0  # Handle case where only one class present
            
            # Store results
            self.models[name] = model
            self.model_scores[name] = {
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                'auc_roc': auc
            }
            
            print(f"{name} Results:")
            print(f"  Accuracy: {accuracy:.4f}")
            print(f"  Precision: {precision:.4f}")
            print(f"  Recall: {recall:.4f}")
            print(f"  F1-score: {f1:.4f}")
            print(f"  AUC-ROC: {auc:.4f}")
        
        self.is_fitted = True
        print("\nPurchase prediction models training complete")
        
        return self
    
    def predict_purchase_probability(self, customer_features: Dict[str, Any], 
                                   article_features: Dict[str, Any],
                                   model_name: str = 'Random Forest') -> float:
        """
        Predict purchase probability for a customer-article pair.
        
        Args:
            customer_features: Dictionary with customer feature values
            article_features: Dictionary with article feature values
            model_name: Name of the model to use for prediction
            
        Returns:
            Purchase probability (0-1)
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not available. Available models: {list(self.models.keys())}")
        
        # Combine features
        combined_features = {**customer_features, **article_features}
        
        # Create feature vector
        feature_vector = []
        for col in self.feature_columns:
            value = combined_features.get(col, 0)  # Default to 0 for missing features
            
            # Apply label encoding if categorical
            if col in self.label_encoders:
                try:
                    value = self.label_encoders[col].transform([str(value)])[0]
                except ValueError:
                    value = 0  # Unknown category
            
            feature_vector.append(value)
        
        # Convert to DataFrame for scaling
        feature_df = pd.DataFrame([feature_vector], columns=self.feature_columns)
        
        # Apply scaling to numerical features
        available_numerical = [col for col in self.numerical_features if col in self.feature_columns]
        if available_numerical:
            feature_df[available_numerical] = self.scaler.transform(feature_df[available_numerical])
        
        # Make prediction
        model = self.models[model_name]
        if hasattr(model, 'predict_proba'):
            probability = model.predict_proba(feature_df)[0, 1]
        else:
            probability = model.predict(feature_df)[0]
        
        return float(probability)
    
    def get_model_performance(self) -> pd.DataFrame:
        """
        Get performance metrics for all trained models.
        
        Returns:
            DataFrame with model performance metrics
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted first")
        
        return pd.DataFrame(self.model_scores).T
    
    def get_feature_importance(self, model_name: str = 'Random Forest') -> pd.DataFrame:
        """
        Get feature importance for a specific model.
        
        Args:
            model_name: Name of the model
            
        Returns:
            DataFrame with feature importance scores
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted first")
        
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not available")
        
        model = self.models[model_name]
        if not hasattr(model, 'feature_importances_'):
            print(f"Model {model_name} does not support feature importance")
            return pd.DataFrame()
        
        importance_df = pd.DataFrame({
            'feature': self.feature_columns,
            'importance': model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        return importance_df
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the fitted models.
        
        Returns:
            Dictionary with model information
        """
        if not self.is_fitted:
            return {"fitted": False}
        
        return {
            "fitted": True,
            "n_models": len(self.models),
            "model_names": list(self.models.keys()),
            "n_features": len(self.feature_columns),
            "feature_names": self.feature_columns,
            "numerical_features": [col for col in self.numerical_features if col in self.feature_columns],
            "categorical_features": [col for col in self.categorical_features if col in self.feature_columns]
        }
    
    def save_model(self, filepath: str) -> None:
        """
        Save the fitted models to a file.
        
        Args:
            filepath: Path to save the models
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before saving")
        
        model_data = {
            'models': self.models,
            'scaler': self.scaler,
            'label_encoders': self.label_encoders,
            'feature_columns': self.feature_columns,
            'model_scores': self.model_scores,
            'numerical_features': self.numerical_features,
            'categorical_features': self.categorical_features,
            'test_size': self.test_size,
            'random_state': self.random_state,
            'is_fitted': self.is_fitted
        }
        
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
        
        print(f"Models saved to {filepath}")
    
    def load_model(self, filepath: str) -> 'PurchasePredictionModel':
        """
        Load fitted models from a file.
        
        Args:
            filepath: Path to load the models from
            
        Returns:
            Loaded model instance
        """
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
        
        self.models = model_data['models']
        self.scaler = model_data['scaler']
        self.label_encoders = model_data['label_encoders']
        self.feature_columns = model_data['feature_columns']
        self.model_scores = model_data['model_scores']
        self.numerical_features = model_data['numerical_features']
        self.categorical_features = model_data['categorical_features']
        self.test_size = model_data['test_size']
        self.random_state = model_data['random_state']
        self.is_fitted = model_data['is_fitted']
        
        print(f"Models loaded from {filepath}")
        return self
