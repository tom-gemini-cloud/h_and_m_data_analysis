"""
Filter H&M articles and customers data to keep only those present in the last 3 months transactions using Apache Spark.

This script loads the filtered transactions (from a prior last-3-months filter) and then filters
the articles.csv and customers.csv files to only include records that appear in those transactions.
"""

from __future__ import annotations

import os
import glob
import shutil
from typing import Optional, Tuple, Dict, Any

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F


class DataFilterSpark:
    """
    A class to filter H&M articles and customers data based on transaction data using Spark.
    """

    def __init__(
        self,
        transactions_path: str,
        articles_path: str,
        customers_path: str,
        spark: Optional[SparkSession] = None,
    ) -> None:
        self.transactions_path = transactions_path
        self.articles_path = articles_path
        self.customers_path = customers_path

        self.spark = spark or (
            SparkSession.builder.appName("HnM-Filter-Related-Data")
            .config("spark.sql.session.timeZone", "UTC")
            .getOrCreate()
        )

        self.transactions_df: Optional[DataFrame] = None
        self.articles_df: Optional[DataFrame] = None
        self.customers_df: Optional[DataFrame] = None
        self.filtered_articles: Optional[DataFrame] = None
        self.filtered_customers: Optional[DataFrame] = None
        self.unique_article_ids: Optional[DataFrame] = None
        self.unique_customer_ids: Optional[DataFrame] = None

    def _read_csv(self, path: str) -> DataFrame:
        return (
            self.spark.read.option("header", True)
            .option("inferSchema", True)
            .csv(path)
        )

    def load_transactions(self) -> None:
        """Load the transaction data (try parquet first, then CSV)."""
        print("Loading transaction data (last 3 months) with Spark...")

        if self.transactions_path.endswith(".parquet"):
            self.transactions_df = self.spark.read.parquet(self.transactions_path)
        else:
            self.transactions_df = self._read_csv(self.transactions_path)

        print(f"Transactions rows: {self.transactions_df.count():,}")

    def extract_unique_ids(self) -> None:
        """Extract unique article IDs and customer IDs from transactions."""
        if self.transactions_df is None:
            raise ValueError("Transactions data must be loaded first. Call load_transactions() method.")

        self.unique_article_ids = self.transactions_df.select("article_id").distinct()
        self.unique_customer_ids = self.transactions_df.select("customer_id").distinct()

        n_articles = self.unique_article_ids.count()
        n_customers = self.unique_customer_ids.count()
        print(f"Unique articles in transactions: {n_articles:,}")
        print(f"Unique customers in transactions: {n_customers:,}")

    def load_and_filter_articles(self) -> DataFrame:
        """Load and filter articles data based on unique article IDs from transactions."""
        if self.unique_article_ids is None:
            raise ValueError("Unique IDs must be extracted first. Call extract_unique_ids() method.")

        print("\nLoading and filtering articles data with Spark...")
        self.articles_df = self._read_csv(self.articles_path)
        original_rows = self.articles_df.count()

        self.filtered_articles = self.articles_df.join(self.unique_article_ids, on="article_id", how="inner")
        filtered_rows = self.filtered_articles.count()
        retained_pct = (filtered_rows / original_rows * 100.0) if original_rows else 0.0

        print(f"Original articles rows: {original_rows:,}")
        print(f"Filtered articles rows: {filtered_rows:,}")
        print(f"Articles retained: {retained_pct:.2f}%")

        return self.filtered_articles

    def load_and_filter_customers(self) -> DataFrame:
        """Load and filter customers data based on unique customer IDs from transactions."""
        if self.unique_customer_ids is None:
            raise ValueError("Unique IDs must be extracted first. Call extract_unique_ids() method.")

        print("\nLoading and filtering customers data with Spark...")
        self.customers_df = self._read_csv(self.customers_path)
        original_rows = self.customers_df.count()

        self.filtered_customers = self.customers_df.join(self.unique_customer_ids, on="customer_id", how="inner")
        filtered_rows = self.filtered_customers.count()
        retained_pct = (filtered_rows / original_rows * 100.0) if original_rows else 0.0

        print(f"Original customers rows: {original_rows:,}")
        print(f"Filtered customers rows: {filtered_rows:,}")
        print(f"Customers retained: {retained_pct:.2f}%")

        return self.filtered_customers

    def _write_csv_single_file(self, df: DataFrame, output_csv_path: str) -> None:
        """Write a single CSV file by coalescing to 1 partition, then moving the part file."""
        output_dir = os.path.dirname(output_csv_path)
        os.makedirs(output_dir, exist_ok=True)

        temp_dir = output_csv_path + "__spark_tmp"
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

        (
            df.coalesce(1)
            .write.mode("overwrite")
            .option("header", True)
            .csv(temp_dir)
        )

        part_files = glob.glob(os.path.join(temp_dir, "part-*.csv"))
        if not part_files:
            part_files = glob.glob(os.path.join(temp_dir, "**", "part-*.csv"), recursive=True)
        if not part_files:
            raise RuntimeError("Could not locate part CSV file produced by Spark.")

        shutil.move(part_files[0], output_csv_path)
        shutil.rmtree(temp_dir, ignore_errors=True)

    def save_articles(self, output_csv_path: Optional[str] = None, output_parquet_path: Optional[str] = None) -> None:
        if self.filtered_articles is None:
            raise ValueError("Articles must be filtered first. Call load_and_filter_articles() method.")

        if output_csv_path:
            print(f"\nSaving filtered articles as CSV to {output_csv_path}")
            self._write_csv_single_file(self.filtered_articles, output_csv_path)

        if output_parquet_path:
            print(f"Saving filtered articles as Parquet to {output_parquet_path}")
            out_dir = output_parquet_path
            os.makedirs(out_dir, exist_ok=True)
            self.filtered_articles.write.mode("overwrite").parquet(out_dir)

    def save_customers(self, output_csv_path: Optional[str] = None, output_parquet_path: Optional[str] = None) -> None:
        if self.filtered_customers is None:
            raise ValueError("Customers must be filtered first. Call load_and_filter_customers() method.")

        if output_csv_path:
            print(f"Saving filtered customers as CSV to {output_csv_path}")
            self._write_csv_single_file(self.filtered_customers, output_csv_path)

        if output_parquet_path:
            print(f"Saving filtered customers as Parquet to {output_parquet_path}")
            out_dir = output_parquet_path
            os.makedirs(out_dir, exist_ok=True)
            self.filtered_customers.write.mode("overwrite").parquet(out_dir)

    def get_statistics(self) -> Dict[str, Any]:
        if self.filtered_articles is None or self.filtered_customers is None:
            raise ValueError("Both articles and customers must be filtered first.")

        counts = {}
        if self.articles_df is not None and self.filtered_articles is not None:
            counts["original_articles_count"] = self.articles_df.count()
            counts["filtered_articles_count"] = self.filtered_articles.count()
            counts["articles_retention_rate"] = (
                (counts["filtered_articles_count"] / counts["original_articles_count"] * 100.0)
                if counts["original_articles_count"]
                else 0.0
            )
        if self.customers_df is not None and self.filtered_customers is not None:
            counts["original_customers_count"] = self.customers_df.count()
            counts["filtered_customers_count"] = self.filtered_customers.count()
            counts["customers_retention_rate"] = (
                (counts["filtered_customers_count"] / counts["original_customers_count"] * 100.0)
                if counts["original_customers_count"]
                else 0.0
            )

        if self.unique_article_ids is not None:
            counts["unique_articles_in_transactions"] = self.unique_article_ids.count()
        if self.unique_customer_ids is not None:
            counts["unique_customers_in_transactions"] = self.unique_customer_ids.count()

        return counts

    def process(
        self,
        output_articles_csv: Optional[str] = None,
        output_articles_parquet: Optional[str] = None,
        output_customers_csv: Optional[str] = None,
        output_customers_parquet: Optional[str] = None,
    ) -> Tuple[DataFrame, DataFrame]:
        self.load_transactions()
        self.extract_unique_ids()

        filtered_articles = self.load_and_filter_articles()
        filtered_customers = self.load_and_filter_customers()

        if output_articles_csv or output_articles_parquet:
            self.save_articles(output_articles_csv, output_articles_parquet)

        if output_customers_csv or output_customers_parquet:
            self.save_customers(output_customers_csv, output_customers_parquet)

        return filtered_articles, filtered_customers


def _report_file_sizes(file_paths: list[str], labels: list[str]) -> None:
    print("\nFile sizes:")
    for path, label in zip(file_paths, labels):
        if os.path.exists(path):
            if os.path.isdir(path):
                total = 0
                for root, _dirs, files in os.walk(path):
                    for f in files:
                        total += os.path.getsize(os.path.join(root, f))
                print(f"  {label}: {total:,} bytes ({total / (1024**2):.2f} MB)")
            else:
                size = os.path.getsize(path)
                print(f"  {label}: {size:,} bytes ({size / (1024**2):.2f} MB)")


def main() -> None:
    # Define paths
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    # Prefer Spark parquet outputs first, then fall back to non-spark ones, then CSV
    candidates = [
        os.path.join(base_path, "data", "processed", "transactions_last_3_months_spark.parquet"),
        os.path.join(base_path, "data", "processed", "transactions_last_3_months.parquet"),
        os.path.join(base_path, "data", "processed", "transactions_last_3_months_spark.csv"),
        os.path.join(base_path, "data", "processed", "transactions_last_3_months.csv"),
    ]
    transactions_path = next((p for p in candidates if os.path.exists(p)), candidates[0])

    articles_path = os.path.join(base_path, "data", "raw", "articles.csv")
    customers_path = os.path.join(base_path, "data", "raw", "customers.csv")

    # Output paths (Spark variants)
    output_articles_csv = os.path.join(base_path, "data", "processed", "articles_last_3_months_spark.csv")
    output_articles_parquet = os.path.join(base_path, "data", "processed", "articles_last_3_months_spark.parquet")
    output_customers_csv = os.path.join(base_path, "data", "processed", "customers_last_3_months_spark.csv")
    output_customers_parquet = os.path.join(base_path, "data", "processed", "customers_last_3_months_spark.parquet")

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
        # Create and use the DataFilterSpark class
        data_filter = DataFilterSpark(transactions_path, articles_path, customers_path)
        filtered_articles, filtered_customers = data_filter.process(
            output_articles_csv=output_articles_csv,
            output_articles_parquet=output_articles_parquet,
            output_customers_csv=output_customers_csv,
            output_customers_parquet=output_customers_parquet,
        )

        print("\n" + "=" * 60)
        print("FILTERING COMPLETED SUCCESSFULLY (Spark)!")
        print("=" * 60)

        print(f"\nFiltered data saved to:")
        print(f"Articles:")
        print(f"  CSV: {output_articles_csv}")
        print(f"  Parquet: {output_articles_parquet}")
        print(f"Customers:")
        print(f"  CSV: {output_customers_csv}")
        print(f"  Parquet: {output_customers_parquet}")

        _report_file_sizes(
            [
                output_articles_csv,
                output_articles_parquet,
                output_customers_csv,
                output_customers_parquet,
            ],
            [
                "Articles CSV",
                "Articles Parquet",
                "Customers CSV",
                "Customers Parquet",
            ],
        )

        print(f"\nFinal Summary:")
        stats = data_filter.get_statistics()
        print(f"  Filtered articles: {stats['filtered_articles_count']:,} records")
        print(f"  Filtered customers: {stats['filtered_customers_count']:,} records")
        print(f"  Article retention rate: {stats['articles_retention_rate']:.2f}%")
        print(f"  Customer retention rate: {stats['customers_retention_rate']:.2f}%")

    except Exception as e:
        print(f"Error processing data (Spark): {e}")
        raise
    finally:
        try:
            data_filter.spark.stop()  # type: ignore[attr-defined]
        except Exception:
            pass


if __name__ == "__main__":
    main()


