"""
Content-Based Filtering Model

Implements content-based filtering using product features and TF-IDF
vectorisation to find similar products and generate recommendations.

Author: Claude Code
Date: 2025-08-15
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple, Optional, Dict, Any
import pickle


class ContentBasedFilteringModel:
    """
    Content-based filtering model using product features.
    
    This model creates recommendations based on product content similarity
    and customer purchase history patterns.
    """
    
    def __init__(self, max_features: int = 1000, ngram_range: Tuple[int, int] = (1, 2), min_df: int = 2):
        """
        Initialise the content-based filtering model.
        
        Args:
            max_features: Maximum number of TF-IDF features
            ngram_range: Range of n-grams for TF-IDF
            min_df: Minimum document frequency for TF-IDF
        """
        self.max_features = max_features
        self.ngram_range = ngram_range
        self.min_df = min_df
        
        # Model components
        self.tfidf_vectorizer = None
        self.content_matrix = None
        self.content_similarity = None
        
        # Data mappings
        self.article_features = None
        self.article_to_idx = None
        self.idx_to_article = None
        self.train_interactions = None
        
        # Text columns for content features
        self.text_columns = [
            'product_type_name', 'product_group_name', 'colour_group_name',
            'department_name', 'section_name', 'garment_group_name'
        ]
        
        # Model fitted flag
        self.is_fitted = False
    
    def prepare_article_features(self, train_df: pd.DataFrame) -> pd.DataFrame:
        """
        Prepare article features for content-based filtering.
        
        Args:
            train_df: Training dataframe with article features
            
        Returns:
            DataFrame with unique articles and their content features
        """
        # Extract product features
        feature_columns = [
            'article_id', 'product_type_name', 'product_group_name',
            'graphical_appearance_name', 'colour_group_name',
            'perceived_colour_value_name', 'perceived_colour_master_name',
            'department_name', 'index_name', 'index_group_name',
            'section_name', 'garment_group_name'
        ]
        
        # Get available columns
        available_columns = [col for col in feature_columns if col in train_df.columns]
        
        article_features = train_df[available_columns].drop_duplicates(subset=['article_id'])
        
        print(f"Prepared features for {article_features.shape[0]:,} unique articles")
        
        # Convert categorical columns to string and handle missing values
        for col in self.text_columns:
            if col in article_features.columns:
                article_features[col] = article_features[col].astype(str).replace('nan', 'unknown')
        
        # Create content features by combining text descriptions
        content_parts = []
        for col in self.text_columns:
            if col in article_features.columns:
                content_parts.append(article_features[col])
        
        if content_parts:
            # Concatenate all text columns with spaces
            article_features['content_features'] = (
                content_parts[0].astype(str)
            )
            for part in content_parts[1:]:
                article_features['content_features'] = (
                    article_features['content_features'] + ' ' + part.astype(str)
                )
            # Clean up extra whitespace
            article_features['content_features'] = article_features['content_features'].apply(
                lambda x: ' '.join(str(x).split())
            )
        else:
            # Fallback if no text columns available
            article_features['content_features'] = 'product'
        
        return article_features
    
    def prepare_interaction_data(self, train_df: pd.DataFrame) -> pd.DataFrame:
        """
        Prepare interaction data from transaction dataframe.
        
        Args:
            train_df: Training dataframe with customer_id, article_id columns
            
        Returns:
            DataFrame with customer_id, article_id interactions
        """
        interactions = train_df[['customer_id', 'article_id']].drop_duplicates().reset_index(drop=True)
        print(f"Prepared {interactions.shape[0]:,} unique customer-article interactions")
        return interactions
    
    def fit(self, train_df: pd.DataFrame) -> 'ContentBasedFilteringModel':
        """
        Fit the content-based filtering model on training data.
        
        Args:
            train_df: Training dataframe with article features and interactions
            
        Returns:
            Fitted model instance
        """
        print("=== Training Content-Based Filtering Model ===")
        
        # Prepare article features
        self.article_features = self.prepare_article_features(train_df)
        
        # Prepare interaction data
        self.train_interactions = self.prepare_interaction_data(train_df)
        
        # Create TF-IDF vectors for content features
        print("Creating TF-IDF vectors for product content...")
        
        self.tfidf_vectorizer = TfidfVectorizer(
            max_features=self.max_features,
            stop_words='english',
            ngram_range=self.ngram_range,
            min_df=self.min_df
        )
        
        self.content_matrix = self.tfidf_vectorizer.fit_transform(
            self.article_features['content_features']
        )
        
        print(f"Content matrix shape: {self.content_matrix.shape}")
        
        # Calculate content similarity matrix
        print("Computing content similarity matrix...")
        self.content_similarity = cosine_similarity(self.content_matrix)
        print(f"Content similarity matrix shape: {self.content_similarity.shape}")
        
        # Create article index mappings
        self.article_to_idx = {
            article_id: idx for idx, article_id in enumerate(self.article_features['article_id'])
        }
        self.idx_to_article = {
            idx: article_id for article_id, idx in self.article_to_idx.items()
        }
        
        self.is_fitted = True
        print("Content-based filtering model training complete")
        
        return self
    
    def get_similar_articles(self, article_id: int, n_similar: int = 10) -> List[Tuple[int, float]]:
        """
        Get articles similar to a given article.
        
        Args:
            article_id: Article to find similar items for
            n_similar: Number of similar articles to return
            
        Returns:
            List of tuples (article_id, similarity_score)
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before finding similar articles")
        
        if article_id not in self.article_to_idx:
            print(f"Article {article_id} not found in training data")
            return []
        
        article_idx = self.article_to_idx[article_id]
        similarity_scores = self.content_similarity[article_idx]
        
        # Get top similar articles (excluding the article itself)
        similar_indices = similarity_scores.argsort()[::-1][1:n_similar+1]
        
        similar_articles = [
            (self.idx_to_article[idx], similarity_scores[idx])
            for idx in similar_indices
        ]
        
        return similar_articles
    
    def get_recommendations(self, customer_id: str, n_recommendations: int = 10) -> List[Tuple[int, float]]:
        """
        Get content-based recommendations for a customer.
        
        Args:
            customer_id: Customer identifier
            n_recommendations: Number of recommendations to return
            
        Returns:
            List of tuples (article_id, score) sorted by score descending
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before making recommendations")
        
        # Get customer's purchased articles
        customer_articles = self.train_interactions[
            self.train_interactions['customer_id'] == customer_id
        ]['article_id'].tolist()
        
        if not customer_articles:
            print(f"No purchase history found for customer {customer_id}")
            return []
        
        # Calculate average similarity scores for articles similar to purchased ones
        similarity_scores = np.zeros(len(self.article_features))
        valid_articles = 0
        
        for article_id in customer_articles:
            if article_id in self.article_to_idx:
                article_idx = self.article_to_idx[article_id]
                similarity_scores += self.content_similarity[article_idx]
                valid_articles += 1
        
        if valid_articles == 0:
            print(f"No valid purchase history found for customer {customer_id}")
            return []
        
        # Average the similarity scores
        similarity_scores /= valid_articles
        
        # Get top recommendations excluding already purchased items
        customer_articles_set = set(customer_articles)
        recommendations = []
        
        # Sort by similarity score
        sorted_indices = np.argsort(similarity_scores)[::-1]
        
        for idx in sorted_indices:
            article_id = self.idx_to_article[idx]
            if article_id not in customer_articles_set and len(recommendations) < n_recommendations:
                recommendations.append((article_id, similarity_scores[idx]))
        
        return recommendations
    
    def predict_score(self, customer_id: str, article_id: int) -> float:
        """
        Predict content-based score for a customer-article pair.
        
        Args:
            customer_id: Customer identifier
            article_id: Article identifier
            
        Returns:
            Predicted content-based score
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        # Get customer's purchased articles
        customer_articles = self.train_interactions[
            self.train_interactions['customer_id'] == customer_id
        ]['article_id'].tolist()
        
        if not customer_articles or article_id not in self.article_to_idx:
            return 0.0
        
        article_idx = self.article_to_idx[article_id]
        total_similarity = 0.0
        valid_articles = 0
        
        # Calculate average similarity to customer's purchased articles
        for purchased_article in customer_articles:
            if purchased_article in self.article_to_idx:
                purchased_idx = self.article_to_idx[purchased_article]
                total_similarity += self.content_similarity[purchased_idx, article_idx]
                valid_articles += 1
        
        if valid_articles == 0:
            return 0.0
        
        return total_similarity / valid_articles
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the fitted model.
        
        Returns:
            Dictionary with model information
        """
        if not self.is_fitted:
            return {"fitted": False}
        
        return {
            "fitted": True,
            "n_articles": len(self.article_features),
            "n_interactions": len(self.train_interactions),
            "content_matrix_shape": self.content_matrix.shape,
            "similarity_matrix_shape": self.content_similarity.shape,
            "max_features": self.max_features,
            "ngram_range": self.ngram_range,
            "min_df": self.min_df,
            "vocabulary_size": len(self.tfidf_vectorizer.vocabulary_)
        }
    
    def save_model(self, filepath: str) -> None:
        """
        Save the fitted model to a file.
        
        Args:
            filepath: Path to save the model
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before saving")
        
        model_data = {
            'tfidf_vectorizer': self.tfidf_vectorizer,
            'content_matrix': self.content_matrix,
            'content_similarity': self.content_similarity,
            'article_features': self.article_features,
            'article_to_idx': self.article_to_idx,
            'idx_to_article': self.idx_to_article,
            'train_interactions': self.train_interactions,
            'max_features': self.max_features,
            'ngram_range': self.ngram_range,
            'min_df': self.min_df,
            'text_columns': self.text_columns,
            'is_fitted': self.is_fitted
        }
        
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
        
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath: str) -> 'ContentBasedFilteringModel':
        """
        Load a fitted model from a file.
        
        Args:
            filepath: Path to load the model from
            
        Returns:
            Loaded model instance
        """
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
        
        self.tfidf_vectorizer = model_data['tfidf_vectorizer']
        self.content_matrix = model_data['content_matrix']
        self.content_similarity = model_data['content_similarity']
        self.article_features = model_data['article_features']
        self.article_to_idx = model_data['article_to_idx']
        self.idx_to_article = model_data['idx_to_article']
        self.train_interactions = model_data['train_interactions']
        self.max_features = model_data['max_features']
        self.ngram_range = model_data['ngram_range']
        self.min_df = model_data['min_df']
        self.text_columns = model_data['text_columns']
        self.is_fitted = model_data['is_fitted']
        
        print(f"Model loaded from {filepath}")
        return self
