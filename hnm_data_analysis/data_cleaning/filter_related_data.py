"""
Filter H&M articles and customers data to keep only those present in the last 3 months transactions.

This script loads the filtered transactions from the last 3 months and then filters
the articles.csv and customers.csv files to only include records that appear in
those transactions. Uses Polars for efficient processing.
"""

import polars as pl
import os


def filter_articles_and_customers(
    transactions_path: str,
    articles_path: str,
    customers_path: str,
    output_articles_csv: str = None,
    output_articles_parquet: str = None,
    output_customers_csv: str = None,
    output_customers_parquet: str = None
) -> tuple[pl.DataFrame, pl.DataFrame]:
    """
    Filter articles and customers based on transactions from the last 3 months.
    
    Args:
        transactions_path: Path to the filtered transactions file (last 3 months)
        articles_path: Path to the articles.csv file
        customers_path: Path to the customers.csv file
        output_articles_csv: Optional path to save filtered articles as CSV
        output_articles_parquet: Optional path to save filtered articles as Parquet
        output_customers_csv: Optional path to save filtered customers as CSV
        output_customers_parquet: Optional path to save filtered customers as Parquet
        
    Returns:
        Tuple of (filtered_articles_df, filtered_customers_df)
    """
    print("Loading transaction data (last 3 months)...")
    
    # Load the filtered transactions (try parquet first, then CSV)
    if transactions_path.endswith('.parquet'):
        transactions_df = pl.read_parquet(transactions_path)
    else:
        transactions_df = pl.read_csv(transactions_path)
    
    print(f"Transactions shape: {transactions_df.shape}")
    
    # Get unique article IDs and customer IDs from transactions
    unique_article_ids = transactions_df.select("article_id").unique()
    unique_customer_ids = transactions_df.select("customer_id").unique()
    
    print(f"Unique articles in transactions: {unique_article_ids.shape[0]:,}")
    print(f"Unique customers in transactions: {unique_customer_ids.shape[0]:,}")
    
    # Load and filter articles
    print("\nLoading and filtering articles data...")
    articles_df = pl.read_csv(articles_path)
    print(f"Original articles shape: {articles_df.shape}")
    
    filtered_articles = articles_df.join(
        unique_article_ids,
        on="article_id",
        how="inner"
    )
    print(f"Filtered articles shape: {filtered_articles.shape}")
    print(f"Articles retained: {(filtered_articles.shape[0] / articles_df.shape[0]) * 100:.2f}%")
    
    # Load and filter customers
    print("\nLoading and filtering customers data...")
    customers_df = pl.read_csv(customers_path)
    print(f"Original customers shape: {customers_df.shape}")
    
    filtered_customers = customers_df.join(
        unique_customer_ids,
        on="customer_id",
        how="inner"
    )
    print(f"Filtered customers shape: {filtered_customers.shape}")
    print(f"Customers retained: {(filtered_customers.shape[0] / customers_df.shape[0]) * 100:.2f}%")
    
    # Save filtered articles
    if output_articles_csv:
        print(f"\nSaving filtered articles as CSV to {output_articles_csv}")
        os.makedirs(os.path.dirname(output_articles_csv), exist_ok=True)
        filtered_articles.write_csv(output_articles_csv)
    
    if output_articles_parquet:
        print(f"Saving filtered articles as Parquet to {output_articles_parquet}")
        os.makedirs(os.path.dirname(output_articles_parquet), exist_ok=True)
        filtered_articles.write_parquet(output_articles_parquet)
    
    # Save filtered customers
    if output_customers_csv:
        print(f"Saving filtered customers as CSV to {output_customers_csv}")
        os.makedirs(os.path.dirname(output_customers_csv), exist_ok=True)
        filtered_customers.write_csv(output_customers_csv)
    
    if output_customers_parquet:
        print(f"Saving filtered customers as Parquet to {output_customers_parquet}")
        os.makedirs(os.path.dirname(output_customers_parquet), exist_ok=True)
        filtered_customers.write_parquet(output_customers_parquet)
    
    return filtered_articles, filtered_customers


def report_file_sizes(file_paths: list[str], labels: list[str]):
    """Report file sizes for given files."""
    print(f"\nFile sizes:")
    for path, label in zip(file_paths, labels):
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"  {label}: {size:,} bytes ({size / (1024**2):.2f} MB)")


def main():
    """Main function to execute the filtering."""
    # Define paths
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    # Input paths
    transactions_path = os.path.join(base_path, "data", "processed", "transactions_last_3_months.parquet")
    # Fallback to CSV if parquet doesn't exist
    if not os.path.exists(transactions_path):
        transactions_path = os.path.join(base_path, "data", "processed", "transactions_last_3_months.csv")
    
    articles_path = os.path.join(base_path, "data", "raw", "articles.csv")
    customers_path = os.path.join(base_path, "data", "raw", "customers.csv")
    
    # Output paths
    output_articles_csv = os.path.join(base_path, "data", "processed", "articles_last_3_months.csv")
    output_articles_parquet = os.path.join(base_path, "data", "processed", "articles_last_3_months.parquet")
    output_customers_csv = os.path.join(base_path, "data", "processed", "customers_last_3_months.csv")
    output_customers_parquet = os.path.join(base_path, "data", "processed", "customers_last_3_months.parquet")
    
    # Check if required input files exist
    required_files = [transactions_path, articles_path, customers_path]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print("Error: Required input files not found:")
        for f in missing_files:
            print(f"  {f}")
        print("\nPlease run the transaction filtering script first or ensure all data files are present.")
        return
    
    try:
        # Filter the data
        filtered_articles, filtered_customers = filter_articles_and_customers(
            transactions_path=transactions_path,
            articles_path=articles_path,
            customers_path=customers_path,
            output_articles_csv=output_articles_csv,
            output_articles_parquet=output_articles_parquet,
            output_customers_csv=output_customers_csv,
            output_customers_parquet=output_customers_parquet
        )
        
        print("\n" + "="*60)
        print("FILTERING COMPLETED SUCCESSFULLY!")
        print("="*60)
        
        print(f"\nFiltered data saved to:")
        print(f"Articles:")
        print(f"  CSV: {output_articles_csv}")
        print(f"  Parquet: {output_articles_parquet}")
        print(f"Customers:")
        print(f"  CSV: {output_customers_csv}")
        print(f"  Parquet: {output_customers_parquet}")
        
        # Report file sizes
        file_paths = [
            output_articles_csv, output_articles_parquet,
            output_customers_csv, output_customers_parquet
        ]
        labels = [
            "Articles CSV", "Articles Parquet",
            "Customers CSV", "Customers Parquet"
        ]
        report_file_sizes(file_paths, labels)
        
        # Calculate compression ratios
        print(f"\nCompression ratios:")
        if os.path.exists(output_articles_csv) and os.path.exists(output_articles_parquet):
            articles_csv_size = os.path.getsize(output_articles_csv)
            articles_parquet_size = os.path.getsize(output_articles_parquet)
            articles_compression = (articles_csv_size - articles_parquet_size) / articles_csv_size * 100
            print(f"  Articles: Parquet is {articles_compression:.1f}% smaller than CSV")
        
        if os.path.exists(output_customers_csv) and os.path.exists(output_customers_parquet):
            customers_csv_size = os.path.getsize(output_customers_csv)
            customers_parquet_size = os.path.getsize(output_customers_parquet)
            customers_compression = (customers_csv_size - customers_parquet_size) / customers_csv_size * 100
            print(f"  Customers: Parquet is {customers_compression:.1f}% smaller than CSV")
        
        # Final summary
        print(f"\nFinal Summary:")
        print(f"  Filtered articles: {filtered_articles.shape[0]:,} records")
        print(f"  Filtered customers: {filtered_customers.shape[0]:,} records")
        
    except Exception as e:
        print(f"Error processing data: {e}")
        raise


if __name__ == "__main__":
    main()