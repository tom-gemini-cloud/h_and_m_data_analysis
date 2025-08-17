"""
Collaborative Filtering Model

Implements collaborative filtering using SVD (Singular Value Decomposition) 
for matrix factorization on user-item interaction data.

Author: Claude Code
Date: 2025-08-15
"""

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder
from typing import List, Tuple, Optional, Dict, Any
import pickle
from pathlib import Path


class CollaborativeFilteringModel:
    """
    Collaborative filtering model using SVD matrix factorization.
    
    This model learns user and item latent factors from interaction data
    and provides recommendations based on predicted user-item affinities.
    """
    
    def __init__(self, n_components: int = 50, random_state: int = 42):
        """
        Initialise the collaborative filtering model.
        
        Args:
            n_components: Number of latent factors for SVD decomposition
            random_state: Random seed for reproducibility
        """
        self.n_components = n_components
        self.random_state = random_state
        
        # Model components
        self.svd_model = None
        self.customer_encoder = None
        self.article_encoder = None
        self.customer_factors = None
        self.article_factors = None
        self.interaction_matrix = None
        
        # Data mappings
        self.all_customers = None
        self.all_articles = None
        self.train_interactions = None
        
        # Model fitted flag
        self.is_fitted = False
    
    def prepare_interaction_data(self, train_df: pd.DataFrame) -> pd.DataFrame:
        """
        Prepare interaction data from transaction dataframe.
        
        Args:
            train_df: Training dataframe with customer_id, article_id columns
            
        Returns:
            DataFrame with customer_id, article_id, and interaction columns
        """
        # Create binary interaction matrix
        interactions = train_df[['customer_id', 'article_id']].drop_duplicates().reset_index(drop=True)
        interactions['interaction'] = 1
        
        print(f"Prepared {interactions.shape[0]:,} unique interactions")
        return interactions
    
    def fit(self, train_df: pd.DataFrame) -> 'CollaborativeFilteringModel':
        """
        Fit the collaborative filtering model on training data.
        
        Args:
            train_df: Training dataframe with customer_id, article_id columns
            
        Returns:
            Fitted model instance
        """
        print("=== Training Collaborative Filtering Model ===")
        
        # Prepare interaction data
        self.train_interactions = self.prepare_interaction_data(train_df)
        
        # Get unique customers and articles
        self.all_customers = train_df['customer_id'].unique()
        self.all_articles = train_df['article_id'].unique()
        
        n_customers = len(self.all_customers)
        n_articles = len(self.all_articles)
        
        print(f"Training on {n_customers:,} customers and {n_articles:,} articles")
        
        # Create encoders
        self.customer_encoder = LabelEncoder()
        self.article_encoder = LabelEncoder()
        
        self.customer_encoder.fit(self.all_customers)
        self.article_encoder.fit(self.all_articles)
        
        # Encode interactions
        self.train_interactions['customer_idx'] = self.customer_encoder.transform(
            self.train_interactions['customer_id']
        )
        self.train_interactions['article_idx'] = self.article_encoder.transform(
            self.train_interactions['article_id']
        )
        
        # Create sparse interaction matrix
        print(f"Creating {n_customers:,} x {n_articles:,} interaction matrix...")
        
        self.interaction_matrix = csr_matrix(
            (self.train_interactions['interaction'], 
             (self.train_interactions['customer_idx'], self.train_interactions['article_idx'])),
            shape=(n_customers, n_articles)
        )
        
        density = self.interaction_matrix.nnz / (n_customers * n_articles) * 100
        print(f"Interaction matrix density: {density:.4f}%")
        print(f"Non-zero elements: {self.interaction_matrix.nnz:,}")
        
        # Apply SVD for matrix factorization
        print("Applying SVD matrix factorization...")
        
        n_components = min(self.n_components, min(n_customers, n_articles) - 1)
        self.svd_model = TruncatedSVD(n_components=n_components, random_state=self.random_state)
        
        # Fit SVD on the interaction matrix
        self.customer_factors = self.svd_model.fit_transform(self.interaction_matrix)
        self.article_factors = self.svd_model.components_
        
        explained_variance = self.svd_model.explained_variance_ratio_.sum()
        print(f"SVD completed with {n_components} components")
        print(f"Explained variance ratio: {explained_variance:.4f}")
        print(f"Customer factors shape: {self.customer_factors.shape}")
        print(f"Article factors shape: {self.article_factors.shape}")
        
        self.is_fitted = True
        print("Collaborative filtering model training complete")
        
        return self
    
    def get_recommendations(self, customer_id: str, n_recommendations: int = 10) -> List[Tuple[int, float]]:
        """
        Get SVD-based recommendations for a customer.
        
        Args:
            customer_id: Customer identifier
            n_recommendations: Number of recommendations to return
            
        Returns:
            List of tuples (article_id, score) sorted by score descending
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before making recommendations")
        
        try:
            customer_idx = self.customer_encoder.transform([customer_id])[0]
        except ValueError:
            print(f"Customer {customer_id} not found in training data")
            return []
        
        # Get customer's latent factors
        customer_vector = self.customer_factors[customer_idx]
        
        # Compute scores for all articles
        scores = np.dot(customer_vector, self.article_factors)
        
        # Get articles customer has already interacted with
        customer_articles = set(
            self.train_interactions[self.train_interactions['customer_id'] == customer_id]['article_id']
        )
        
        # Create recommendations excluding already purchased items
        recommendations = []
        article_scores = list(zip(self.all_articles, scores))
        article_scores.sort(key=lambda x: x[1], reverse=True)
        
        for article_id, score in article_scores:
            if article_id not in customer_articles and len(recommendations) < n_recommendations:
                recommendations.append((article_id, score))
        
        return recommendations
    
    def predict_score(self, customer_id: str, article_id: int) -> float:
        """
        Predict the affinity score for a specific customer-article pair.
        
        Args:
            customer_id: Customer identifier
            article_id: Article identifier
            
        Returns:
            Predicted affinity score
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        try:
            customer_idx = self.customer_encoder.transform([customer_id])[0]
            article_idx = self.article_encoder.transform([article_id])[0]
            
            customer_vector = self.customer_factors[customer_idx]
            article_vector = self.article_factors[:, article_idx]
            
            score = np.dot(customer_vector, article_vector)
            return float(score)
            
        except ValueError as e:
            print(f"Error predicting score: {e}")
            return 0.0
    
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
            "n_components": self.svd_model.n_components,
            "n_customers": len(self.all_customers),
            "n_articles": len(self.all_articles),
            "n_interactions": len(self.train_interactions),
            "explained_variance_ratio": self.svd_model.explained_variance_ratio_.sum(),
            "matrix_density": self.interaction_matrix.nnz / (len(self.all_customers) * len(self.all_articles)) * 100
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
            'svd_model': self.svd_model,
            'customer_encoder': self.customer_encoder,
            'article_encoder': self.article_encoder,
            'customer_factors': self.customer_factors,
            'article_factors': self.article_factors,
            'all_customers': self.all_customers,
            'all_articles': self.all_articles,
            'train_interactions': self.train_interactions,
            'n_components': self.n_components,
            'random_state': self.random_state,
            'is_fitted': self.is_fitted
        }
        
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
        
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath: str) -> 'CollaborativeFilteringModel':
        """
        Load a fitted model from a file.
        
        Args:
            filepath: Path to load the model from
            
        Returns:
            Loaded model instance
        """
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
        
        self.svd_model = model_data['svd_model']
        self.customer_encoder = model_data['customer_encoder']
        self.article_encoder = model_data['article_encoder']
        self.customer_factors = model_data['customer_factors']
        self.article_factors = model_data['article_factors']
        self.all_customers = model_data['all_customers']
        self.all_articles = model_data['all_articles']
        self.train_interactions = model_data['train_interactions']
        self.n_components = model_data['n_components']
        self.random_state = model_data['random_state']
        self.is_fitted = model_data['is_fitted']
        
        print(f"Model loaded from {filepath}")
        return self
