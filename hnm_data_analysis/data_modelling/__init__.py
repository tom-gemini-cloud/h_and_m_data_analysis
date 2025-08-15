"""
Data Modelling Module

This module contains different recommendation system approaches for H&M customer data:
- Collaborative filtering with matrix factorization
- Content-based filtering using product features
- Purchase prediction classification models
- Hybrid recommendation systems

Each model type is implemented in separate modules for modularity and reusability.
"""

from .collaborative_filtering import CollaborativeFilteringModel
from .content_based_filtering import ContentBasedFilteringModel
from .purchase_prediction import PurchasePredictionModel
from .hybrid_recommender import HybridRecommenderModel

__all__ = [
    'CollaborativeFilteringModel',
    'ContentBasedFilteringModel', 
    'PurchasePredictionModel',
    'HybridRecommenderModel'
]