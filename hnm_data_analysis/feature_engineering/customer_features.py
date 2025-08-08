"""
Customer Feature Engineering Module

This module provides comprehensive feature engineering capabilities for H&M customer data,
focusing on RFM analysis (Recency, Frequency, Monetary), demographic features, and core
shopping metrics using Polars for high-performance data processing.

Classes:
    CustomerFeatureEngineer: Main class for creating customer features from transaction data
"""

import polars as pl
from datetime import datetime, timedelta
from typing import Tuple, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CustomerFeatureEngineer:
    """
    Feature engineering class for creating comprehensive customer features from H&M data.
    
    Produces RFM analysis features, demographic features, and core shopping metrics
    optimised for retail analytics applications.
    """
    
    def __init__(self, analysis_date: Optional[datetime] = None):
        """
        Initialise the CustomerFeatureEngineer.
        
        Args:
            analysis_date: Reference date for recency calculations. Defaults to latest transaction date.
        """
        self.analysis_date = analysis_date
        
    def load_datasets(self, 
                     customers_path: str,
                     transactions_path: str, 
                     articles_path: str) -> Tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
        """
        Load the three cleaned datasets efficiently using Polars.
        
        Args:
            customers_path: Path to cleaned customers dataset
            transactions_path: Path to cleaned transactions dataset  
            articles_path: Path to cleaned articles dataset
            
        Returns:
            Tuple of (customers, transactions, articles) DataFrames
        """
        logger.info("Loading datasets...")
        
        customers = pl.read_parquet(customers_path)
        transactions = pl.read_parquet(transactions_path) 
        articles = pl.read_parquet(articles_path)
        
        logger.info(f"Loaded {customers.height:,} customers, {transactions.height:,} transactions, {articles.height:,} articles")
        
        # Set analysis date if not provided
        if self.analysis_date is None:
            self.analysis_date = transactions["t_dat"].max()
            logger.info(f"Analysis date set to latest transaction date: {self.analysis_date}")
            
        return customers, transactions, articles
    
    def create_rfm_features(self, transactions: pl.DataFrame) -> pl.DataFrame:
        """
        Create comprehensive RFM (Recency, Frequency, Monetary) analysis features.
        
        Args:
            transactions: Transactions DataFrame with columns t_dat, customer_id, price
            
        Returns:
            DataFrame with customer_id and RFM features
        """
        logger.info("Creating RFM features...")
        
        # Calculate RFM metrics per customer
        rfm_features = (
            transactions
            .group_by("customer_id")
            .agg([
                # Recency: Days since last purchase
                (pl.lit(self.analysis_date).cast(pl.Date) - pl.col("t_dat").max()).dt.total_days().alias("recency_days"),
                
                # Frequency: Number of transactions and unique purchase days
                pl.len().alias("transaction_count"),
                pl.col("t_dat").n_unique().alias("unique_purchase_days"),
                
                # Monetary: Total spent, average transaction value, spending patterns
                pl.col("price").sum().alias("total_spent"),
                pl.col("price").mean().alias("avg_transaction_value"),
                pl.col("price").median().alias("median_transaction_value"),
                pl.col("price").std().alias("spending_variability"),
                pl.col("price").min().alias("min_purchase_value"),
                pl.col("price").max().alias("max_purchase_value"),
                
                # Additional temporal features
                (pl.col("t_dat").max() - pl.col("t_dat").min()).dt.total_days().alias("customer_lifespan_days"),
                pl.col("t_dat").dt.month().mode().first().alias("preferred_purchase_month"),
                pl.col("t_dat").dt.weekday().mode().first().alias("preferred_purchase_day_of_week")
            ])
            .with_columns([
                # Derived metrics
                (pl.col("total_spent") / pl.col("unique_purchase_days")).alias("avg_daily_spend"),
                (pl.col("transaction_count") / pl.col("unique_purchase_days")).alias("avg_transactions_per_day"),
                (pl.col("customer_lifespan_days") / pl.col("unique_purchase_days")).alias("purchase_frequency_ratio"),
                
                # RFM scores (quintile ranking)
                pl.col("recency_days").qcut(5, labels=["5", "4", "3", "2", "1"]).alias("recency_score"),
                pl.col("transaction_count").qcut(5, labels=["1", "2", "3", "4", "5"]).alias("frequency_score"), 
                pl.col("total_spent").qcut(5, labels=["1", "2", "3", "4", "5"]).alias("monetary_score")
            ])
        )
        
        # Create combined RFM score
        rfm_features = rfm_features.with_columns([
            (pl.col("recency_score").cast(pl.Int32) + 
             pl.col("frequency_score").cast(pl.Int32) + 
             pl.col("monetary_score").cast(pl.Int32)).alias("rfm_combined_score"),
            
            # Create RFM segment labels
            (pl.col("recency_score").cast(pl.Utf8) + "-" + 
             pl.col("frequency_score").cast(pl.Utf8) + "-" + 
             pl.col("monetary_score").cast(pl.Utf8)).alias("rfm_segment")
        ])
        
        logger.info(f"Created RFM features for {rfm_features.height:,} customers")
        return rfm_features
    
    def create_product_preference_features(self, 
                                         transactions: pl.DataFrame, 
                                         articles: pl.DataFrame) -> pl.DataFrame:
        """
        Create product preference features based on customer purchasing behaviour.
        
        Args:
            transactions: Transactions DataFrame
            articles: Articles DataFrame with product information
            
        Returns:
            DataFrame with customer product preference features
        """
        logger.info("Creating product preference features...")
        
        # Join transactions with articles to get product information
        trans_with_products = transactions.join(articles, on="article_id", how="left")
        
        # Calculate product preference features
        product_features = (
            trans_with_products
            .group_by("customer_id")
            .agg([
                # Product category preferences
                pl.col("product_group_name").mode().first().alias("preferred_product_group"),
                pl.col("product_group_name").n_unique().alias("product_group_diversity"),
                
                # Colour preferences
                pl.col("colour_group_name").mode().first().alias("preferred_colour_group"),
                pl.col("colour_group_name").n_unique().alias("colour_diversity"),
                
                # Department preferences  
                pl.col("department_name").mode().first().alias("preferred_department"),
                pl.col("department_name").n_unique().alias("department_diversity"),
                
                # Garment preferences
                pl.col("garment_group_name").mode().first().alias("preferred_garment_group"),
                pl.col("garment_group_name").n_unique().alias("garment_diversity"),
                
                # Price segment analysis
                pl.col("price").mean().alias("avg_price_preference"),
                (pl.col("price") > pl.col("price").quantile(0.75)).sum().alias("premium_purchases"),
                (pl.col("price") < pl.col("price").quantile(0.25)).sum().alias("budget_purchases"),
                
                # Unique article counts
                pl.col("article_id").n_unique().alias("unique_articles_purchased")
            ])
        )
        
        logger.info(f"Created product preference features for {product_features.height:,} customers")
        return product_features
    
    def create_demographic_features(self, customers: pl.DataFrame) -> pl.DataFrame:
        """
        Create enhanced demographic features from customer data.
        
        Args:
            customers: Customers DataFrame with demographic information
            
        Returns:
            DataFrame with enhanced demographic features
        """
        logger.info("Creating demographic features...")
        
        demographic_features = (
            customers
            .with_columns([
                # Age group categorisation
                pl.when(pl.col("age") < 25).then(pl.lit("18-24"))
                .when(pl.col("age") < 35).then(pl.lit("25-34"))
                .when(pl.col("age") < 45).then(pl.lit("35-44")) 
                .when(pl.col("age") < 55).then(pl.lit("45-54"))
                .when(pl.col("age") < 65).then(pl.lit("55-64"))
                .otherwise(pl.lit("65+")).alias("age_group"),
                
                # Life stage classification
                pl.when(pl.col("age") < 25).then(pl.lit("Young_Adult"))
                .when(pl.col("age") < 45).then(pl.lit("Adult"))
                .when(pl.col("age") < 65).then(pl.lit("Middle_Aged"))
                .otherwise(pl.lit("Senior")).alias("life_stage"),
                
                # Club membership features
                pl.when(pl.col("club_member_status") == "ACTIVE").then(pl.lit(1))
                .otherwise(pl.lit(0)).alias("is_club_member"),
                
                # Fashion engagement level
                pl.when(pl.col("fashion_news_frequency") == "Regularly").then(pl.lit("High"))
                .when(pl.col("fashion_news_frequency") == "Monthly").then(pl.lit("Medium"))
                .when(pl.col("fashion_news_frequency").is_in(["None", "NONE"])).then(pl.lit("Low"))
                .otherwise(pl.lit("Medium")).alias("fashion_engagement"),
                
                # Data completeness score
                ((~pl.col("FN_imputed").cast(pl.Int32)) +
                 (~pl.col("Active_imputed").cast(pl.Int32)) +
                 (~pl.col("club_member_status_imputed").cast(pl.Int32)) +
                 (~pl.col("fashion_news_frequency_imputed").cast(pl.Int32)) +
                 (~pl.col("age_imputed").cast(pl.Int32))).alias("data_completeness_score")
            ])
            .select([
                "customer_id", "age", "age_group", "life_stage", 
                "is_club_member", "fashion_engagement", "data_completeness_score",
                "club_member_status", "fashion_news_frequency"
            ])
        )
        
        logger.info(f"Created demographic features for {demographic_features.height:,} customers")
        return demographic_features
    
    def create_core_shopping_metrics(self, 
                                   transactions: pl.DataFrame,
                                   articles: pl.DataFrame) -> pl.DataFrame:
        """
        Create core shopping behaviour metrics.
        
        Args:
            transactions: Transactions DataFrame
            articles: Articles DataFrame
            
        Returns:
            DataFrame with core shopping metrics
        """
        logger.info("Creating core shopping metrics...")
        
        # Join with articles for enriched metrics
        trans_with_products = transactions.join(articles, on="article_id", how="left")
        
        shopping_metrics = (
            trans_with_products
            .group_by("customer_id")
            .agg([
                # Basic metrics requested
                pl.col("price").sum().alias("total_spent"),
                pl.len().alias("transaction_count"),
                
                # Shopping behaviour patterns
                pl.col("article_id").n_unique().alias("unique_items_purchased"),
                (pl.col("price").sum() / pl.col("article_id").n_unique()).alias("avg_spend_per_unique_item"),
                
                # Purchase timing patterns
                pl.col("t_dat").dt.weekday().mean().alias("avg_purchase_day_of_week"),
                pl.col("t_dat").dt.month().std().alias("seasonal_purchase_variability"),
                
                # Channel preferences
                pl.col("sales_channel_id").mode().first().alias("preferred_sales_channel"),
                
                # Purchase value distribution
                (pl.col("price") > pl.col("price").mean() * 1.5).sum().alias("high_value_purchases"),
                pl.col("price").quantile(0.25).alias("price_p25"),
                pl.col("price").quantile(0.75).alias("price_p75")
            ])
            .with_columns([
                # Derived shopping behaviour metrics
                (pl.col("high_value_purchases") / pl.col("transaction_count")).alias("high_value_purchase_rate"),
                (pl.col("price_p75") - pl.col("price_p25")).alias("price_range_preference")
            ])
        )
        
        logger.info(f"Created core shopping metrics for {shopping_metrics.height:,} customers")
        return shopping_metrics
    
    def create_customer_features(self,
                               customers_path: str,
                               transactions_path: str,
                               articles_path: str,
                               output_dir: str = "data/features") -> pl.DataFrame:
        """
        Create comprehensive customer features combining all feature types.
        
        Args:
            customers_path: Path to cleaned customers dataset
            transactions_path: Path to cleaned transactions dataset
            articles_path: Path to cleaned articles dataset
            output_dir: Directory to save feature outputs
            
        Returns:
            DataFrame with all customer features combined
        """
        logger.info("Starting comprehensive customer feature engineering...")
        
        # Load datasets
        customers, transactions, articles = self.load_datasets(
            customers_path, transactions_path, articles_path
        )
        
        # Create feature sets
        rfm_features = self.create_rfm_features(transactions)
        product_features = self.create_product_preference_features(transactions, articles)
        demographic_features = self.create_demographic_features(customers)
        shopping_metrics = self.create_core_shopping_metrics(transactions, articles)
        
        # Combine all features
        logger.info("Combining all feature sets...")
        
        customer_features = (
            demographic_features
            .join(rfm_features, on="customer_id", how="left")
            .join(product_features, on="customer_id", how="left") 
            .join(shopping_metrics, on="customer_id", how="left")
        )
        
        # Fill null values for customers without transactions
        customer_features = customer_features.fill_null(0)
        
        # Optimise memory by collecting result
        customer_features = customer_features.rechunk()
        
        logger.info(f"Created comprehensive features for {customer_features.height:,} customers with {len(customer_features.columns)} features")
        
        # Create output directory
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # Save as both Parquet and CSV
        parquet_path = f"{output_dir}/customer_features.parquet"
        csv_path = f"{output_dir}/customer_features.csv"
        
        customer_features.write_parquet(parquet_path)
        customer_features.write_csv(csv_path)
        
        logger.info(f"Saved customer features to {parquet_path} and {csv_path}")
        
        return customer_features