"""
Filter H&M transaction data to keep only the final 3 months of transactions.

This script loads the transactions_train.csv file and filters it to only include
transactions from the last 3 months of the dataset (2020-06-23 to 2020-09-22).
Uses Polars for efficient processing of the large dataset.
"""

import polars as pl
from datetime import datetime, timedelta
import os


def filter_last_3_months_transactions(input_path: str, output_csv_path: str = None, output_parquet_path: str = None) -> pl.DataFrame:
    """
    Filter transactions to keep only the final 3 months.
    
    Args:
        input_path: Path to the input transactions_train.csv file
        output_csv_path: Optional path to save the filtered data as CSV
        output_parquet_path: Optional path to save the filtered data as Parquet
        
    Returns:
        Polars DataFrame with filtered transactions
    """
    print("Loading transaction data...")
    
    # Load the transaction data
    df = pl.read_csv(input_path)
    
    print(f"Original dataset shape: {df.shape}")
    print(f"Date range: {df['t_dat'].min()} to {df['t_dat'].max()}")
    
    # Convert t_dat to date type if it's not already
    df = df.with_columns(
        pl.col("t_dat").str.to_date().alias("t_dat")
    )
    
    # Get the maximum date and calculate 3 months prior
    max_date = df['t_dat'].max()
    three_months_prior = max_date - timedelta(days=90)  # Approximately 3 months
    
    print(f"Filtering for dates from {three_months_prior} to {max_date}")
    
    # Filter for the last 3 months
    filtered_df = df.filter(pl.col("t_dat") >= three_months_prior)
    
    print(f"Filtered dataset shape: {filtered_df.shape}")
    print(f"Percentage of original data retained: {(filtered_df.shape[0] / df.shape[0]) * 100:.2f}%")
    
    # Save to output paths if provided
    if output_csv_path:
        print(f"Saving filtered data as CSV to {output_csv_path}")
        os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
        filtered_df.write_csv(output_csv_path)
    
    if output_parquet_path:
        print(f"Saving filtered data as Parquet to {output_parquet_path}")
        os.makedirs(os.path.dirname(output_parquet_path), exist_ok=True)
        filtered_df.write_parquet(output_parquet_path)
    
    return filtered_df


def main():
    """Main function to execute the filtering."""
    # Define paths
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    input_path = os.path.join(base_path, "data", "raw", "transactions_train.csv")
    output_csv_path = os.path.join(base_path, "data", "processed", "transactions_last_3_months.csv")
    output_parquet_path = os.path.join(base_path, "data", "processed", "transactions_last_3_months.parquet")
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file not found at {input_path}")
        return
    
    try:
        # Filter the data
        filtered_data = filter_last_3_months_transactions(input_path, output_csv_path, output_parquet_path)
        
        print("\nFiltering completed successfully!")
        print(f"Filtered data saved to:")
        print(f"  CSV: {output_csv_path}")
        print(f"  Parquet: {output_parquet_path}")
        
        # Report file sizes
        print(f"\nFile sizes:")
        if os.path.exists(output_csv_path):
            csv_size = os.path.getsize(output_csv_path)
            print(f"  CSV: {csv_size:,} bytes ({csv_size / (1024**2):.2f} MB)")
        
        if os.path.exists(output_parquet_path):
            parquet_size = os.path.getsize(output_parquet_path)
            print(f"  Parquet: {parquet_size:,} bytes ({parquet_size / (1024**2):.2f} MB)")
            
            if os.path.exists(output_csv_path):
                compression_ratio = (csv_size - parquet_size) / csv_size * 100
                print(f"  Compression: Parquet is {compression_ratio:.1f}% smaller than CSV")
        
        # Display some basic statistics
        print("\nBasic statistics of filtered data:")
        print(f"Number of transactions: {filtered_data.shape[0]:,}")
        print(f"Number of unique customers: {filtered_data['customer_id'].n_unique():,}")
        print(f"Number of unique articles: {filtered_data['article_id'].n_unique():,}")
        print(f"Date range: {filtered_data['t_dat'].min()} to {filtered_data['t_dat'].max()}")
        
    except Exception as e:
        print(f"Error processing data: {e}")


if __name__ == "__main__":
    main()