import sys
import warnings
warnings.filterwarnings('ignore')

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.stat import Correlation
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time
from typing import Tuple, List, Dict, Optional


def initialise_spark_session(app_name: str = "HMDataExamination") -> SparkSession:
    """
    Initialise and configure Spark session with optimised memory settings for data examination.
    
    Args:
        app_name (str): Name of the Spark data examination application
        
    Returns:
        SparkSession: Configured Spark session with performance optimisations
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.driver.memory", "8g") \
        .config("spark.driver.maxResultSize", "4g") \
        .config("spark.sql.adaptive.skewJoin.enabled", "true") \
        .config("spark.sql.adaptive.localShuffleReader.enabled", "true") \
        .config("spark.sql.shuffle.partitions", "200") \
        .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "128MB") \
        .getOrCreate()
    
    print("Spark Session initialised successfully")
    print(f"Spark Version: {spark.version}")
    
    return spark


def load_transactions_data(spark: SparkSession, file_path: str, sample_fraction: float = 0.1, 
                          random_seed: int = 42) -> Tuple[object, int]:
    """
    Load and sample transaction data from CSV file for examination.
    
    Args:
        spark (SparkSession): Active Spark session
        file_path (str): Path to transactions CSV file
        sample_fraction (float): Fraction of data to sample (0.0 to 1.0)
        random_seed (int): Random seed for reproducible sampling
        
    Returns:
        Tuple[DataFrame, int]: Tuple containing (sampled DataFrame, record count)
        
    Raises:
        FileNotFoundError: If the specified file path doesn't exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Transaction file not found: {file_path}")
    
    print("• Loading transactions data...")
    
    # Load full dataset
    df_transactions_full = spark.read.option("header", "true").option("inferSchema", "true").csv(file_path)
    
    # Apply sampling
    df_transactions = df_transactions_full.sample(fraction=sample_fraction, seed=random_seed)
    transaction_count = df_transactions.count()
    
    print(f"  ✓ Transactions: {transaction_count:,} records loaded")
    print("  - Schema:")
    df_transactions.printSchema()
    
    return df_transactions, transaction_count


def load_customers_data(spark: SparkSession, file_path: str) -> Tuple[object, int]:
    """
    Load customer demographic and preference data from CSV file for examination.
    
    Args:
        spark (SparkSession): Active Spark session
        file_path (str): Path to customers CSV file
        
    Returns:
        Tuple[DataFrame, int]: Tuple containing (DataFrame, record count)
        
    Raises:
        FileNotFoundError: If the specified file path doesn't exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Customers file not found: {file_path}")
    
    print("\n• Loading customer data...")
    
    df_customers = spark.read.option("header", "true").option("inferSchema", "true").csv(file_path)
    customer_count = df_customers.count()
    
    print(f"  ✓ Customers: {customer_count:,} records loaded")
    print("  - Schema:")
    df_customers.printSchema()
    
    return df_customers, customer_count


def load_articles_data(spark: SparkSession, file_path: str) -> Tuple[object, int]:
    """
    Load product/article information and metadata from CSV file for examination.
    
    Args:
        spark (SparkSession): Active Spark session
        file_path (str): Path to articles CSV file
        
    Returns:
        Tuple[DataFrame, int]: Tuple containing (DataFrame, record count)
        
    Raises:
        FileNotFoundError: If the specified file path doesn't exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Articles file not found: {file_path}")
    
    print("\n• Loading articles data...")
    
    df_articles = spark.read.option("header", "true").option("inferSchema", "true").csv(file_path)
    article_count = df_articles.count()
    
    print(f"  ✓ Articles: {article_count:,} records loaded")
    print("  - Schema:")
    df_articles.printSchema()
    
    return df_articles, article_count


def integrate_datasets(df_transactions: object, df_customers: object, df_articles: object) -> Tuple[object, Dict[str, int]]:
    """
    Integrate transaction, customer, and article datasets into a single dataset for examination.

    Also analyses the integrated dataset structure and categorises features.
    
    Args:
        df_transactions (DataFrame): Transaction data with customer and article IDs
        df_customers (DataFrame): Customer demographic data
        df_articles (DataFrame): Article/product metadata
        
    Returns:
        Tuple[DataFrame, Dict]: Tuple containing (integrated DataFrame, dataset statistics)
    """
    print("Creating integrated customer interaction dataset...")
    
    # Perform left joins to preserve all transaction records
    df_customer_transactions = df_transactions.join(df_customers, "customer_id", "left")
    df_full = df_customer_transactions.join(df_articles, "article_id", "left")
    
    # Cache and repartition for efficient processing
    df_full_optimised = df_full.repartition(20)
    df_full_cached = df_full_optimised.persist()
    
    # Calculate dataset statistics
    integrated_count = df_full_cached.count()
    unique_customers = df_full_cached.select('customer_id').distinct().count()
    unique_articles = df_full_cached.select('article_id').distinct().count()
    
    stats = {
        'total_records': integrated_count,
        'unique_customers': unique_customers,
        'unique_articles': unique_articles
    }
    
    print(f"✓ Integrated dataset created with {integrated_count:,} transaction records")
    
    # Show sample of integrated data
    print(f"\nSample of integrated dataset:")
    sample_cols = ["customer_id", "article_id", "price", "sales_channel_id", "age", "club_member_status", "product_type_name"]
    available_cols = [col for col in sample_cols if col in df_full_cached.columns]
    df_full_cached.select(available_cols).show(5)
    
    # Analyse the dataset structure
    print(f"\nDataset Structure Analysis:")
    print(f"• Total unique customers: {unique_customers:,}")
    print(f"• Total unique articles: {unique_articles:,}")
    
    # Check if date column exists and show range
    if 't_dat' in df_full_cached.columns:
        date_range = df_full_cached.agg(min('t_dat'), max('t_dat')).collect()[0]
        print(f"• Date range: {date_range[0]} to {date_range[1]}")
    
    # Create feature categories for H&M dataset
    all_columns = df_full_cached.columns
    feature_categories = {
        'Customer Demographics': [col for col in ['customer_id', 'age', 'club_member_status', 'fashion_news_frequency'] if col in all_columns],
        'Transaction Behaviour': [col for col in ['t_dat', 'price', 'sales_channel_id'] if col in all_columns],
        'Product Information': [col for col in ['article_id', 'product_type_name', 'product_group_name', 'colour_group_name'] if col in all_columns],
        'Customer Preferences': [col for col in ['garment_group_name', 'index_name', 'section_name'] if col in all_columns]
    }
    
    print(f"\nDataset Features by Category:")
    for category, features in feature_categories.items():
        if features:  # Only show categories with available features
            print(f"  {category}: {', '.join(features)}")
    
    print(f"\n✓ Dataset repartitioned and cached for efficient processing")
    
    return df_full_cached, stats


def assess_data_quality(df: object) -> Dict[str, any]:
    """
    Perform comprehensive data quality assessment including missing values, duplicates, and outliers.
    
    Args:
        df (DataFrame): Input DataFrame to assess
        
    Returns:
        Dict[str, any]: Dictionary containing quality assessment results including:
            - missing_summary: List of (column_name, missing_count, missing_percentage)
            - duplicate_count: Number of duplicate records
            - price_stats: Price distribution statistics if price column exists
    """
    print("Analysing existing data quality issues in H&M dataset...")
    
    # Check for missing values
    print(f"\n• Missing Values Analysis:")
    missing_summary = []
    
    columns_to_check = df.columns
    for col_name in columns_to_check:
        missing_count = df.filter(col(col_name).isNull()).count()
        total_count = df.count()
        if missing_count > 0:
            missing_percentage = (missing_count / total_count) * 100
            missing_summary.append((col_name, missing_count, missing_percentage))
    
    if missing_summary:
        for col_name, missing_count, missing_percentage in missing_summary:
            print(f"  {col_name}: {missing_count:,} ({missing_percentage:.2f}%)")
    else:
        print("  ✓ No missing values found in original dataset")
    
    # Analyse duplicates
    print(f"\n• Duplicate Analysis:")
    duplicate_count = df.count() - df.dropDuplicates().count()
    print(f"  Duplicate records: {duplicate_count:,}")
    
    # Check for potential outliers in price data
    price_stats = None
    if 'price' in df.columns:
        print(f"\n• Price Distribution Analysis:")
        price_stats = df.select('price').describe().collect()
        for row in price_stats:
            print(f"  {row['summary']}: {row['price']}")
    
    quality_report = {
        'missing_summary': missing_summary,
        'duplicate_count': duplicate_count,
        'price_stats': price_stats
    }
    
    return quality_report


def examine_hm_data(data_dir: str = './data', sample_fraction: float = 0.1, 
                   random_seed: int = 42) -> Dict[str, any]:
    """
    Main function to examine the H&M dataset structure and quality.
    
    This function coordinates the data examination workflow including:
    1. Spark session initialisation
    2. Data loading from CSV files
    3. Dataset integration and feature analysis
    4. Data quality assessment
    
    Args:
        data_dir (str): Directory containing the H&M dataset files
        sample_fraction (float): Fraction of transaction data to sample (0.0 to 1.0)
        random_seed (int): Random seed for reproducible sampling
        
    Returns:
        Dict[str, any]: Comprehensive examination results including:
            - spark_session: Active Spark session
            - datasets: Dictionary of loaded DataFrames
            - integration_stats: Dataset integration statistics
            - quality_report: Data quality assessment results
            
    Raises:
        FileNotFoundError: If required data files are not found
        Exception: If any step in the examination pipeline fails
    """
    print("=== H&M Data Examination Report ===")
    print("Using PySpark and PyArrow with H&M Kaggle Dataset\n")
    
    try:
        # Initialise Spark session
        spark = initialise_spark_session()
        
        print("\n" + "=" * 60)
        print("1. DATA LOADING AND EXAMINATION")
        print("=" * 60)
        
        print("\n1.1 Loading H&M Dataset Files")
        print("-" * 35)
        
        # Set up file paths
        transactions_path = os.path.join(data_dir, 'raw', 'transactions_train.csv')
        customers_path = os.path.join(data_dir, 'raw', 'customers.csv')
        articles_path = os.path.join(data_dir, 'raw', 'articles.csv')
        
        print("Loading dataset components:")
        print(f"  🔬 Using {sample_fraction*100:.0f}% sample for memory optimisation")
        
        # Load all datasets for examination
        df_transactions, transaction_count = load_transactions_data(spark, transactions_path, sample_fraction, random_seed)
        df_customers, customer_count = load_customers_data(spark, customers_path)
        df_articles, article_count = load_articles_data(spark, articles_path)
        
        print(f"\n1.2 Dataset Overview and Integration")
        print("-" * 42)
        
        # Integrate datasets for examination
        df_integrated, integration_stats = integrate_datasets(df_transactions, df_customers, df_articles)
        
        print(f"\n1.3 Data Quality Assessment")
        print("-" * 35)
        
        # Assess data quality
        quality_report = assess_data_quality(df_integrated)
        
        print(f"\n✓ Data Examination Complete")
        print(f"  - Total transaction records: {transaction_count:,}")
        print(f"  - Integrated records: {integration_stats['total_records']:,}")
        print(f"  - Unique customers: {integration_stats['unique_customers']:,}")
        print(f"  - Unique articles: {integration_stats['unique_articles']:,}")
        
        # Compile results
        results = {
            'spark_session': spark,
            'datasets': {
                'transactions': df_transactions,
                'customers': df_customers,
                'articles': df_articles,
                'integrated': df_integrated
            },
            'counts': {
                'transactions': transaction_count,
                'customers': customer_count,
                'articles': article_count
            },
            'integration_stats': integration_stats,
            'quality_report': quality_report
        }
        
        return results
        
    except Exception as e:
        print(f"\n⚠ Error during examination: {str(e)}")
        if 'spark' in locals():
            spark.stop()
        raise


if __name__ == "__main__":
    """
    Main execution block - runs the H&M data examination pipeline.
    """
    try:
        examination_results = examine_hm_data(
            data_dir='./data',
            sample_fraction=0.1,  # Use 10% sample for demonstration
            random_seed=42
        )
        
        print("\n" + "=" * 60)
        print("DATA EXAMINATION COMPLETED SUCCESSFULLY")
        print("=" * 60)
        print(f"Results available in examination_results dictionary")
        print(f"Access integrated data with: examination_results['datasets']['integrated']")
        
    except Exception as e:
        print(f"\nExamination failed: {e}")
        
    finally:
        # Clean up Spark session
        if 'examination_results' in locals() and 'spark_session' in examination_results:
            examination_results['spark_session'].stop()
            print("\n✓ Spark session stopped")
        else:
            # Fallback cleanup
            try:
                spark = SparkSession.getActiveSession()
                if spark:
                    spark.stop()
                    print("\n✓ Spark session stopped")
            except:
                pass