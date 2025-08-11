"""
Feature engineering module for H&M data analysis.

This package exposes feature construction utilities, including text-based
representations for articles that can be used in downstream modelling and
clustering.
"""

from .customer_features import *  # re-export existing public features if any

# Vectorisation utilities
from .articles_text_tfidf import ArticleDescriptionVectoriser

__all__ = [
    # keep wildcards minimal; explicitly list known public API
    "ArticleDescriptionVectoriser",
]

