#!/usr/bin/env python3
"""
Quick script to create integrated dataset for H&M data analysis.
This creates the same integrated dataset that the exploration notebook would create.
"""

import polars as pl
import pandas as pd
import os
import time

def create_integrated_dataset():
    """Create integrated H&M dataset from raw CSV files."""
    
    # Configuration
    data_dir = 'data'
    use_full_dataset = False  # Start with sample for testing
    sample_fraction = 0.1 if not use_full_dataset else 1.0
    random_seed = 42

    # File paths
    transactions_path = os.path.join(data_dir, 'raw', 'transactions_train.csv')
    customers_path = os.path.join(data_dir, 'raw', 'customers.csv')
    articles_path = os.path.join(data_dir, 'raw', 'articles.csv')
    
    print("H&M Data Integration Script")
    print("=" * 40)
    
    # Verify files exist
    for path, name in [(transactions_path, 'transactions'), (customers_path, 'customers'), (articles_path, 'articles')]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"{name.title()} file not found: {path}")
        print(f"✓ Found {name} file: {path}")
    
    print(f"\nConfiguration:")
    print(f"• Using full dataset: {use_full_dataset}")
    print(f"• Sample fraction: {sample_fraction*100:.0f}%")
    
    # Load datasets
    print(f"\nLoading datasets...")
    start_time = time.time()
    
    # Load transactions (with sampling if needed)
    print("  Loading transactions...")
    if use_full_dataset:
        df_transactions = pl.read_csv(transactions_path)
    else:
        df_transactions = pl.read_csv(transactions_path).sample(fraction=sample_fraction, seed=random_seed)
    print(f"    ✓ Loaded {df_transactions.height:,} transaction records")
    
    # Load customers
    print("  Loading customers...")
    df_customers = pl.read_csv(customers_path)
    print(f"    ✓ Loaded {df_customers.height:,} customer records")
    
    # Load articles
    print("  Loading articles...")
    df_articles = pl.read_csv(articles_path)
    print(f"    ✓ Loaded {df_articles.height:,} article records")
    
    # Create integrated dataset
    print(f"\nCreating integrated dataset...")
    df_integrated = (
        df_transactions
        .join(df_customers, on="customer_id", how="left")
        .join(df_articles, on="article_id", how="left")
    )
    
    integration_time = time.time() - start_time
    print(f"✓ Integration completed in {integration_time:.2f} seconds")
    print(f"✓ Final dataset: {df_integrated.height:,} records with {len(df_integrated.columns)} columns")
    print(f"✓ Memory usage: {df_integrated.estimated_size('mb'):.1f} MB")
    
    # Create output directory
    output_dir = os.path.join(data_dir, 'processed')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save integrated dataset
    print(f"\nSaving integrated dataset...")
    output_path = os.path.join(output_dir, 'hm_integrated_dataset.parquet')
    df_integrated.write_parquet(output_path)
    
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✓ Saved to: {output_path}")
    print(f"✓ File size: {file_size_mb:.1f} MB")
    
    # Quick validation
    print(f"\nDataset Summary:")
    print(f"• Unique customers: {df_integrated['customer_id'].n_unique():,}")
    print(f"• Unique articles: {df_integrated['article_id'].n_unique():,}")
    
    if 't_dat' in df_integrated.columns:
        date_range = df_integrated.select([
            pl.col('t_dat').min().alias('min_date'),
            pl.col('t_dat').max().alias('max_date')
        ]).to_pandas().iloc[0]
        print(f"• Date range: {date_range['min_date']} to {date_range['max_date']}")
    
    print(f"\n✅ Integrated dataset ready for visualisation notebooks!")
    print(f"You can now run the visualisation notebooks.")
    
    return df_integrated

if __name__ == "__main__":
    try:
        create_integrated_dataset()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please ensure you're running this script from the project root directory")
        print("and that all required CSV files exist in data/raw/")