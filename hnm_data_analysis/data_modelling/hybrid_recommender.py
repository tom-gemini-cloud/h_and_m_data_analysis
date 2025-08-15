"""
Hybrid Recommender Model

Combines collaborative filtering and content-based approaches for improved
recommendations using weighted ensemble methods.

Author: Claude Code
Date: 2025-08-15
"""

import numpy as np
import pandas as pd
from typing import List, Tuple, Optional, Dict, Any, Union
from .collaborative_filtering import CollaborativeFilteringModel
from .content_based_filtering import ContentBasedFilteringModel
from .purchase_prediction import PurchasePredictionModel
import pickle


class HybridRecommenderModel:
    """
    Hybrid recommendation system combining multiple approaches.
    
    This model combines collaborative filtering, content-based filtering,
    and purchase prediction models to generate improved recommendations.
    """
    
    def __init__(self, cf_weight: float = 0.4, cb_weight: float = 0.4, pp_weight: float = 0.2):
        """
        Initialise the hybrid recommender model.
        
        Args:
            cf_weight: Weight for collaborative filtering scores
            cb_weight: Weight for content-based filtering scores  
            pp_weight: Weight for purchase prediction scores
        """
        if abs(cf_weight + cb_weight + pp_weight - 1.0) > 1e-6:
            raise ValueError("Weights must sum to 1.0")
        
        self.cf_weight = cf_weight
        self.cb_weight = cb_weight
        self.pp_weight = pp_weight
        
        # Component models
        self.cf_model = None
        self.cb_model = None
        self.pp_model = None
        
        # Model fitted flag
        self.is_fitted = False
    
    def fit(self, train_df: pd.DataFrame, 
            cf_params: Optional[Dict] = None,
            cb_params: Optional[Dict] = None,
            pp_params: Optional[Dict] = None) -> 'HybridRecommenderModel':
        """
        Fit all component models on training data.
        
        Args:
            train_df: Training dataframe
            cf_params: Parameters for collaborative filtering model
            cb_params: Parameters for content-based filtering model
            pp_params: Parameters for purchase prediction model
            
        Returns:
            Fitted hybrid model instance
        """
        print("=== Training Hybrid Recommender Model ===")
        
        # Default parameters
        cf_params = cf_params or {}
        cb_params = cb_params or {}
        pp_params = pp_params or {}
        
        # Train collaborative filtering model
        print("\n1. Training Collaborative Filtering Model...")
        self.cf_model = CollaborativeFilteringModel(**cf_params)
        self.cf_model.fit(train_df)
        
        # Train content-based filtering model
        print("\n2. Training Content-Based Filtering Model...")
        self.cb_model = ContentBasedFilteringModel(**cb_params)
        self.cb_model.fit(train_df)
        
        # Train purchase prediction model
        print("\n3. Training Purchase Prediction Model...")
        self.pp_model = PurchasePredictionModel(**pp_params)
        self.pp_model.fit(train_df)
        
        self.is_fitted = True
        print("\nHybrid recommender model training complete")
        
        return self
    
    def normalise_scores(self, scores: Dict[int, float]) -> Dict[int, float]:
        """
        Normalise scores to 0-1 range.
        
        Args:
            scores: Dictionary of article_id -> score
            
        Returns:
            Dictionary with normalised scores
        """
        if not scores:
            return scores
        
        min_score = min(scores.values())
        max_score = max(scores.values())
        
        if max_score == min_score:
            return {k: 1.0 for k in scores.keys()}
        
        return {
            k: (v - min_score) / (max_score - min_score)
            for k, v in scores.items()
        }
    
    def get_recommendations(self, customer_id: str, n_recommendations: int = 10, 
                          expand_factor: int = 3) -> List[Tuple[int, float]]:
        """
        Get hybrid recommendations combining all component models.
        
        Args:
            customer_id: Customer identifier
            n_recommendations: Number of recommendations to return
            expand_factor: Factor to expand intermediate recommendations
            
        Returns:
            List of tuples (article_id, combined_score) sorted by score descending
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before making recommendations")
        
        expanded_recs = n_recommendations * expand_factor
        
        # Get recommendations from each component
        cf_recommendations = []
        cb_recommendations = []
        pp_scores = {}
        
        # Collaborative filtering recommendations
        if self.cf_model and self.cf_weight > 0:
            try:
                cf_recommendations = self.cf_model.get_recommendations(customer_id, expanded_recs)
            except Exception as e:
                print(f"Warning: CF recommendations failed: {e}")
        
        # Content-based recommendations
        if self.cb_model and self.cb_weight > 0:
            try:
                cb_recommendations = self.cb_model.get_recommendations(customer_id, expanded_recs)
            except Exception as e:
                print(f"Warning: CB recommendations failed: {e}")
        
        # Convert to score dictionaries
        cf_scores = {article_id: score for article_id, score in cf_recommendations}
        cb_scores = {article_id: score for article_id, score in cb_recommendations}
        
        # Purchase prediction scores (for articles from CF and CB)
        all_articles = set(cf_scores.keys()) | set(cb_scores.keys())
        
        if self.pp_model and self.pp_weight > 0 and all_articles:
            print(f"Computing purchase prediction scores for {len(all_articles)} articles...")
            # This is simplified - would need customer and article features in practice
            for article_id in list(all_articles)[:100]:  # Limit for performance
                try:
                    # Simplified prediction - would need proper feature extraction
                    score = np.random.random()  # Placeholder
                    pp_scores[article_id] = score
                except Exception as e:
                    print(f"Warning: PP score failed for article {article_id}: {e}")
        
        # Normalise all scores
        cf_scores_norm = self.normalise_scores(cf_scores)
        cb_scores_norm = self.normalise_scores(cb_scores)
        pp_scores_norm = self.normalise_scores(pp_scores)
        
        # Combine scores with weights
        all_articles = set(cf_scores_norm.keys()) | set(cb_scores_norm.keys()) | set(pp_scores_norm.keys())
        hybrid_scores = {}
        
        for article_id in all_articles:
            cf_score = cf_scores_norm.get(article_id, 0.0)
            cb_score = cb_scores_norm.get(article_id, 0.0)
            pp_score = pp_scores_norm.get(article_id, 0.0)
            
            combined_score = (
                self.cf_weight * cf_score +
                self.cb_weight * cb_score +
                self.pp_weight * pp_score
            )
            
            hybrid_scores[article_id] = combined_score
        
        # Sort and return top recommendations
        sorted_recommendations = sorted(
            hybrid_scores.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        return sorted_recommendations[:n_recommendations]
    
    def get_recommendation_explanation(self, customer_id: str, article_id: int) -> Dict[str, float]:
        """
        Get explanation of recommendation scores from each component.
        
        Args:
            customer_id: Customer identifier
            article_id: Article identifier
            
        Returns:
            Dictionary with component scores and combined score
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before explaining recommendations")
        
        explanation = {
            'cf_score': 0.0,
            'cb_score': 0.0,
            'pp_score': 0.0,
            'combined_score': 0.0
        }
        
        # Get collaborative filtering score
        if self.cf_model and self.cf_weight > 0:
            try:
                explanation['cf_score'] = self.cf_model.predict_score(customer_id, article_id)
            except Exception as e:
                print(f"Warning: CF score failed: {e}")
        
        # Get content-based score
        if self.cb_model and self.cb_weight > 0:
            try:
                explanation['cb_score'] = self.cb_model.predict_score(customer_id, article_id)
            except Exception as e:
                print(f"Warning: CB score failed: {e}")
        
        # Get purchase prediction score (simplified)
        if self.pp_model and self.pp_weight > 0:
            try:
                # This would need proper feature extraction in practice
                explanation['pp_score'] = np.random.random()  # Placeholder
            except Exception as e:
                print(f"Warning: PP score failed: {e}")
        
        # Calculate combined score
        explanation['combined_score'] = (
            self.cf_weight * explanation['cf_score'] +
            self.cb_weight * explanation['cb_score'] +
            self.pp_weight * explanation['pp_score']
        )
        
        return explanation
    
    def get_model_weights(self) -> Dict[str, float]:
        """
        Get the weights used for combining models.
        
        Returns:
            Dictionary with model weights
        """
        return {
            'collaborative_filtering': self.cf_weight,
            'content_based': self.cb_weight,
            'purchase_prediction': self.pp_weight
        }
    
    def set_model_weights(self, cf_weight: float = None, cb_weight: float = None, 
                         pp_weight: float = None) -> None:
        """
        Update the weights for combining models.
        
        Args:
            cf_weight: New weight for collaborative filtering
            cb_weight: New weight for content-based filtering
            pp_weight: New weight for purchase prediction
        """
        # Keep current weights if not specified
        new_cf = cf_weight if cf_weight is not None else self.cf_weight
        new_cb = cb_weight if cb_weight is not None else self.cb_weight
        new_pp = pp_weight if pp_weight is not None else self.pp_weight
        
        # Check weights sum to 1
        if abs(new_cf + new_cb + new_pp - 1.0) > 1e-6:
            raise ValueError("Weights must sum to 1.0")
        
        self.cf_weight = new_cf
        self.cb_weight = new_cb
        self.pp_weight = new_pp
        
        print(f"Updated weights: CF={self.cf_weight}, CB={self.cb_weight}, PP={self.pp_weight}")
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the hybrid model and its components.
        
        Returns:
            Dictionary with model information
        """
        info = {
            "fitted": self.is_fitted,
            "weights": self.get_model_weights()
        }
        
        if self.is_fitted:
            info.update({
                "cf_model_info": self.cf_model.get_model_info() if self.cf_model else None,
                "cb_model_info": self.cb_model.get_model_info() if self.cb_model else None,
                "pp_model_info": self.pp_model.get_model_info() if self.pp_model else None
            })
        
        return info
    
    def save_model(self, filepath: str) -> None:
        """
        Save the hybrid model and all components to a file.
        
        Args:
            filepath: Path to save the model
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before saving")
        
        model_data = {
            'cf_model': self.cf_model,
            'cb_model': self.cb_model,
            'pp_model': self.pp_model,
            'cf_weight': self.cf_weight,
            'cb_weight': self.cb_weight,
            'pp_weight': self.pp_weight,
            'is_fitted': self.is_fitted
        }
        
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
        
        print(f"Hybrid model saved to {filepath}")
    
    def load_model(self, filepath: str) -> 'HybridRecommenderModel':
        """
        Load a hybrid model from a file.
        
        Args:
            filepath: Path to load the model from
            
        Returns:
            Loaded model instance
        """
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
        
        self.cf_model = model_data['cf_model']
        self.cb_model = model_data['cb_model']
        self.pp_model = model_data['pp_model']
        self.cf_weight = model_data['cf_weight']
        self.cb_weight = model_data['cb_weight']
        self.pp_weight = model_data['pp_weight']
        self.is_fitted = model_data['is_fitted']
        
        print(f"Hybrid model loaded from {filepath}")
        return self
