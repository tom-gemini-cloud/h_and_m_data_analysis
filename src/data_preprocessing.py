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

# Import functions from data_examination module
from data_examination import initialise_spark_session, assess_data_quality


def preprocess_and_clean_data(df: object, quality_report: Dict[str, any], 
                             data_dir: str = './data') -> Tuple[object, Dict[str, any]]:
    """
    Data preprocessing and cleaning pipeline including duplicate removal, missing value imputation, and outlier handling.
    
    Args:
        df (DataFrame): Input DataFrame to preprocess
        quality_report (Dict): Quality assessment report from assess_data_quality()
        data_dir (str): Directory to save cleaned data
        
    Returns:
        Tuple[DataFrame, Dict]: Tuple containing (cleaned DataFrame, processing summary)
    """
    print(f"Starting data preprocessing and cleaning pipeline on {df.count():,} records...")
    
    missing_summary = quality_report['missing_summary']
    duplicate_count = quality_report['duplicate_count']
    
    # Step 1: Remove duplicates if any exist
    if duplicate_count > 0:
        print(f"\n• Removing Duplicates:")
        df_no_duplicates = df.dropDuplicates()
        final_count = df_no_duplicates.count()
        print(f"  - Removed {duplicate_count:,} duplicate records")
        print(f"  - Remaining records: {final_count:,}")
    else:
        df_no_duplicates = df
        print(f"\n• No duplicates found - proceeding with original dataset for preprocessing")
    
    # Step 2: Handle missing values if any exist
    if missing_summary:
        print(f"\n• Handling Missing Values:")
        
        # For numerical columns, use median imputation
        numerical_cols = [col_name for col_name, _, _ in missing_summary 
                         if df_no_duplicates.select(col_name).dtypes[0][1] in ['int', 'double', 'float']]
        
        for col_name in numerical_cols:
            # Calculate median excluding nulls
            median_val = df_no_duplicates.select(col_name).filter(col(col_name).isNotNull()) \
                                        .approxQuantile(col_name, [0.5], 0.01)[0]
            
            # Fill missing values with median
            df_no_duplicates = df_no_duplicates.fillna({col_name: median_val})
            print(f"  - {col_name}: filled with median value {median_val:.2f}")
        
        # For categorical columns, use mode imputation or default values
        categorical_cols = [col_name for col_name, _, _ in missing_summary 
                           if df_no_duplicates.select(col_name).dtypes[0][1] in ['string']]
        
        for col_name in categorical_cols:
            # Calculate mode (most frequent value) excluding nulls
            mode_result = df_no_duplicates.select(col_name).filter(col(col_name).isNotNull()) \
                                         .groupBy(col_name).count().orderBy(col('count').desc()).first()
            
            if mode_result:
                mode_val = mode_result[0]
                # Fill missing values with mode
                df_no_duplicates = df_no_duplicates.fillna({col_name: mode_val})
                print(f"  - {col_name}: filled with mode value '{mode_val}'")
            else:
                # If no mode available, use default value
                default_val = "Unknown"
                df_no_duplicates = df_no_duplicates.fillna({col_name: default_val})
                print(f"  - {col_name}: filled with default value '{default_val}'")
    
    # Step 3: Handle outliers in price column
    outlier_count = 0
    if 'price' in df_no_duplicates.columns:
        print(f"\n• Handling Outliers (IQR Method):")
        
        # Calculate quartiles for price
        quartiles = df_no_duplicates.select('price').approxQuantile('price', [0.25, 0.75], 0.01)
        Q1, Q3 = quartiles[0], quartiles[1]
        IQR = Q3 - Q1
        
        # Define outlier bounds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Count outliers before removal
        outlier_count = df_no_duplicates.filter(
            (col('price') < lower_bound) | (col('price') > upper_bound)
        ).count()
        
        # Cap outliers at bounds (keeping original data structure)
        df_no_duplicates = df_no_duplicates.withColumn(
            'price',
            when(col('price') < lower_bound, lower_bound)
            .when(col('price') > upper_bound, upper_bound)
            .otherwise(col('price'))
        )
        
        print(f"  - price: {outlier_count:,} outliers capped (bounds: {lower_bound:.1f} - {upper_bound:.1f})")
    
    # Data validation and final quality check
    print(f"\n• Final Data Quality Check:")
    final_record_count = df_no_duplicates.count()
    print(f"  - Final dataset size: {final_record_count:,} records")
    
    # Check for remaining missing values
    remaining_nulls = 0
    for col_name in df_no_duplicates.columns:
        null_count = df_no_duplicates.filter(col(col_name).isNull()).count()
        remaining_nulls += null_count
    
    print(f"  - Remaining missing values: {remaining_nulls}")
    print(f"  - Data integrity: {'✓ PASSED' if remaining_nulls == 0 else '✗ FAILED'}")
    
    # Save cleaned dataset
    output_path = os.path.join(data_dir, 'processed', 'hm_customer_data_cleaned.parquet')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_no_duplicates.write.mode('overwrite').parquet(output_path)
    print(f"✓ Saved preprocessed and cleaned dataset as Parquet file")
    
    # Create summary statistics
    print(f"\n• Dataset Summary Statistics:")
    
    # Show basic statistics for key numerical columns
    numerical_columns = [col for col, dtype in df_no_duplicates.dtypes if dtype in ['int', 'double', 'float']]
    if numerical_columns:
        print("Summary statistics for numerical columns:")
        summary_stats = df_no_duplicates.select(numerical_columns[:5]).describe()  # Limit to first 5 for readability
        summary_stats.show()
    
    # Cache cleaned dataframe for further analysis
    df_cleaned = df_no_duplicates.cache()
    
    processing_summary = {
        'final_record_count': final_record_count,
        'duplicates_removed': duplicate_count,
        'outliers_handled': outlier_count,
        'remaining_nulls': remaining_nulls,
        'data_integrity_passed': remaining_nulls == 0
    }
    
    return df_cleaned, processing_summary


def run_preprocessing_pipeline(integrated_df: object, data_dir: str = './data') -> Tuple[object, Dict[str, any]]:
    """
    Complete preprocessing pipeline that assesses quality and cleans data.
    
    Args:
        integrated_df (DataFrame): Integrated DataFrame from examination phase
        data_dir (str): Directory to save cleaned data
        
    Returns:
        Tuple[DataFrame, Dict]: Tuple containing (cleaned DataFrame, processing summary)
    """
    print("=== Data Preprocessing Pipeline ===")
    
    # Assess data quality
    print("\n1. Assessing Data Quality")
    print("-" * 30)
    quality_report = assess_data_quality(integrated_df)
    
    # Run preprocessing
    print("\n2. Preprocessing and Cleaning Data")
    print("-" * 40)
    df_cleaned, processing_summary = preprocess_and_clean_data(integrated_df, quality_report, data_dir)
    
    print(f"\n✓ Preprocessing Pipeline Complete")
    print(f"  - Final record count: {processing_summary['final_record_count']:,}")
    print(f"  - Data quality: {'High' if processing_summary['data_integrity_passed'] else 'Needs attention'}")
    print(f"  - Dataset ready for downstream analysis and modelling")
    
    return df_cleaned, processing_summary


def hm_data_preprocessing(data_dir: str = './data', sample_fraction: float = 0.1, 
                        random_seed: int = 42) -> Dict[str, any]:
    """
    Main function to control the complete H&M customer data preprocessing and cleaning pipeline.
    
    This function coordinates the entire data preprocessing workflow including:
    1. Spark session initialisation
    2. Data loading from CSV files (via examination module)
    3. Dataset integration and feature analysis (via examination module)
    4. Data quality assessment
    5. Data preprocessing and cleaning
    
    Args:
        data_dir (str): Directory containing the H&M dataset files
        sample_fraction (float): Fraction of transaction data to sample (0.0 to 1.0)
        random_seed (int): Random seed for reproducible sampling
        
    Returns:
        Dict[str, any]: Comprehensive preprocessing results including:
            - spark_session: Active Spark session
            - datasets: Dictionary of loaded DataFrames
            - integration_stats: Dataset integration statistics
            - quality_report: Data quality assessment results
            - processing_summary: Data preprocessing results
            
    Raises:
        FileNotFoundError: If required data files are not found
        Exception: If any step in the preprocessing pipeline fails
    """
    print("=== CONL722 Assignment 1: Customer Data Preprocessing and Cleaning Report ===")
    print("Using PySpark and PyArrow with H&M Kaggle Dataset\n")
    
    try:
        # Import examination functions to avoid code duplication
        from data_examination import examine_hm_data
        
        # First run the examination phase
        examination_results = examine_hm_data(data_dir, sample_fraction, random_seed)
        
        # Extract the integrated dataset
        df_integrated = examination_results['datasets']['integrated']
        spark = examination_results['spark_session']
        
        print("\n" + "=" * 60)
        print("2. DATA PREPROCESSING AND CLEANING")
        print("=" * 60)
        
        # Run preprocessing pipeline
        df_cleaned, processing_summary = run_preprocessing_pipeline(df_integrated, data_dir)
        
        # Compile results
        results = {
            'spark_session': spark,
            'datasets': {
                **examination_results['datasets'],
                'cleaned': df_cleaned
            },
            'counts': examination_results['counts'],
            'integration_stats': examination_results['integration_stats'],
            'quality_report': examination_results['quality_report'],
            'processing_summary': processing_summary
        }
        
        return results
        
    except Exception as e:
        print(f"\n⚠ Error during preprocessing: {str(e)}")
        if 'spark' in locals():
            spark.stop()
        raise


if __name__ == "__main__":
    """
    Main execution block - runs the H&M data preprocessing and cleaning pipeline.
    """
    try:
        preprocessing_results = hm_data_preprocessing(
            data_dir='./data',
            sample_fraction=0.1,  # Use 10% sample for demonstration
            random_seed=42
        )
        
        print("\n" + "=" * 60)
        print("PREPROCESSING PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)
        print(f"Results available in preprocessing_results dictionary")
        print(f"Access cleaned data with: preprocessing_results['datasets']['cleaned']")
        
    except Exception as e:
        print(f"\nPreprocessing failed: {e}")
        
    finally:
        # Clean up Spark session
        if 'preprocessing_results' in locals() and 'spark_session' in preprocessing_results:
            preprocessing_results['spark_session'].stop()
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