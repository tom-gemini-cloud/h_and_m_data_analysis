"""
Filter H&M transaction data to keep only the final 3 months of transactions using Apache Spark.

This script loads the transactions_train.csv file with Spark and filters it to only include
transactions from the last 3 months of the dataset. It can save outputs as CSV (single file)
and/or Parquet. Designed for large-scale datasets.
"""

from __future__ import annotations

import os
import glob
import shutil
from datetime import timedelta
from typing import Optional, Dict, Any

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F


class TransactionFilterSpark:
    """
    A class to filter H&M transaction data to keep only the final 3 months of transactions using Spark.

    This class provides methods to load, filter, and save transaction data leveraging Spark for
    efficient processing of large datasets.
    """

    def __init__(self, input_path: str, spark: Optional[SparkSession] = None) -> None:
        """
        Initialise the TransactionFilterSpark with the input data path and optional Spark session.

        Args:
            input_path: Path to the input transactions_train.csv file
            spark: Optional pre-created SparkSession. If None, a default will be created.
        """
        self.input_path = input_path
        self.spark = spark or (
            SparkSession.builder.appName("HnM-Filter-Last-3-Months")
            .config("spark.sql.session.timeZone", "UTC")
            .getOrCreate()
        )

        self.original_df: Optional[DataFrame] = None
        self.filtered_df: Optional[DataFrame] = None
        self.max_date = None
        self.three_months_prior = None

    def load_data(self) -> None:
        """Load the transaction data from the input path using Spark."""
        print("Loading transaction data with Spark...")
        # Read CSV with header and infer schema. Adjust options if needed for your dataset.
        df = (
            self.spark.read.option("header", True)
            .option("inferSchema", True)
            .csv(self.input_path)
        )

        # Convert t_dat to date type if it's not already
        df = df.withColumn("t_dat", F.to_date(F.col("t_dat")))

        self.original_df = df

        # Basic info
        row_count = df.count()
        min_max = df.select(F.min("t_dat").alias("min"), F.max("t_dat").alias("max")).collect()[0]
        print(f"Original dataset rows: {row_count:,}")
        print(f"Date range: {min_max['min']} to {min_max['max']}")

    def calculate_date_range(self) -> None:
        """Calculate the date range for filtering (last ~3 months ≈ 90 days)."""
        if self.original_df is None:
            raise ValueError("Data must be loaded first. Call load_data() method.")

        max_row = self.original_df.select(F.max("t_dat").alias("max_date")).collect()[0]
        self.max_date = max_row["max_date"]
        # Use 90 days approximation to match the original Polars implementation
        self.three_months_prior = self.max_date - timedelta(days=90)

        print(f"Filtering for dates from {self.three_months_prior} to {self.max_date}")

    def filter_transactions(self) -> DataFrame:
        """
        Filter transactions to keep only the final 3 months.

        Returns:
            Spark DataFrame with filtered transactions
        """
        if self.original_df is None:
            raise ValueError("Data must be loaded first. Call load_data() method.")

        if self.three_months_prior is None:
            self.calculate_date_range()

        # Filter for the last ~3 months
        self.filtered_df = self.original_df.filter(F.col("t_dat") >= F.lit(self.three_months_prior))

        kept_rows = self.filtered_df.count()
        original_rows = self.original_df.count()
        pct = (kept_rows / original_rows * 100.0) if original_rows else 0.0
        print(f"Filtered dataset rows: {kept_rows:,}")
        print(f"Percentage of original data retained: {pct:.2f}%")

        return self.filtered_df

    def _write_csv_single_file(self, df: DataFrame, output_csv_path: str) -> None:
        """
        Write a single CSV file at the given file path by coalescing to 1 partition.

        Spark normally writes a directory for CSV output. This helper writes to a temporary
        directory, then renames the single part file to the requested destination path.
        """
        output_dir = os.path.dirname(output_csv_path)
        os.makedirs(output_dir, exist_ok=True)

        temp_dir = output_csv_path + "__spark_tmp"  # temp output directory
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

        (
            df.coalesce(1)
            .write.mode("overwrite")
            .option("header", True)
            .csv(temp_dir)
        )

        # Find the generated single CSV and move it to the final destination path
        part_files = glob.glob(os.path.join(temp_dir, "part-*.csv"))
        if not part_files:
            # Fallback: sometimes Spark may write with .csv extension under different name
            part_files = glob.glob(os.path.join(temp_dir, "**", "part-*.csv"), recursive=True)

        if not part_files:
            raise RuntimeError("Could not locate part CSV file produced by Spark.")

        # Move the first part file to the target path
        shutil.move(part_files[0], output_csv_path)
        # Cleanup the temporary directory
        shutil.rmtree(temp_dir, ignore_errors=True)

    def save_data(
        self,
        output_csv_path: Optional[str] = None,
        output_parquet_path: Optional[str] = None,
        single_csv_file: bool = True,
    ) -> None:
        """
        Save the filtered data to specified paths.

        Args:
            output_csv_path: Optional path to save the filtered data as a single CSV file
            output_parquet_path: Optional path to save the filtered data as Parquet (directory)
            single_csv_file: If True and CSV path provided, write a single CSV file (coalesce to 1)
        """
        if self.filtered_df is None:
            raise ValueError("Data must be filtered first. Call filter_transactions() method.")

        if output_csv_path:
            print(f"Saving filtered data as CSV to {output_csv_path}")
            if single_csv_file:
                self._write_csv_single_file(self.filtered_df, output_csv_path)
            else:
                # Write as a directory of CSV part-files
                out_dir = output_csv_path
                os.makedirs(out_dir, exist_ok=True)
                (
                    self.filtered_df.write.mode("overwrite").option("header", True).csv(out_dir)
                )

        if output_parquet_path:
            print(f"Saving filtered data as Parquet to {output_parquet_path}")
            out_dir = output_parquet_path
            os.makedirs(out_dir, exist_ok=True)
            self.filtered_df.write.mode("overwrite").parquet(out_dir)

    def get_statistics(self) -> Dict[str, Any]:
        """
        Get basic statistics about the filtered data.

        Returns:
            Dictionary containing basic statistics
        """
        if self.filtered_df is None:
            raise ValueError("Data must be filtered first. Call filter_transactions() method.")

        num_transactions = self.filtered_df.count()
        distinct_counts = self.filtered_df.agg(
            F.countDistinct("customer_id").alias("num_unique_customers"),
            F.countDistinct("article_id").alias("num_unique_articles"),
            F.min("t_dat").alias("date_range_start"),
            F.max("t_dat").alias("date_range_end"),
        ).collect()[0]

        return {
            "num_transactions": num_transactions,
            "num_unique_customers": distinct_counts["num_unique_customers"],
            "num_unique_articles": distinct_counts["num_unique_articles"],
            "date_range_start": distinct_counts["date_range_start"],
            "date_range_end": distinct_counts["date_range_end"],
        }

    def process(
        self,
        output_csv_path: Optional[str] = None,
        output_parquet_path: Optional[str] = None,
        single_csv_file: bool = True,
    ) -> DataFrame:
        """
        Complete processing pipeline: load, filter, and optionally save data.

        Args:
            output_csv_path: Optional path to save the filtered data as CSV
            output_parquet_path: Optional path to save the filtered data as Parquet
            single_csv_file: If True and CSV path provided, write a single CSV file

        Returns:
            Spark DataFrame with filtered transactions
        """
        self.load_data()
        filtered_df = self.filter_transactions()

        if output_csv_path or output_parquet_path:
            self.save_data(output_csv_path, output_parquet_path, single_csv_file=single_csv_file)

        return filtered_df


def main() -> None:
    """Main function to execute the filtering with Spark."""
    # Define paths
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    input_path = os.path.join(base_path, "data", "raw", "transactions_train.csv")
    output_csv_path = os.path.join(
        base_path, "data", "processed", "transactions_last_3_months_spark.csv"
    )
    output_parquet_path = os.path.join(
        base_path, "data", "processed", "transactions_last_3_months_spark.parquet"
    )

    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file not found at {input_path}")
        return

    try:
        # Create and use the TransactionFilterSpark class
        transaction_filter = TransactionFilterSpark(input_path)
        filtered_data = transaction_filter.process(
            output_csv_path=output_csv_path,
            output_parquet_path=output_parquet_path,
            single_csv_file=True,
        )

        print("\nFiltering completed successfully (Spark)!")
        print("Filtered data saved to:")
        print(f"  CSV: {output_csv_path}")
        print(f"  Parquet: {output_parquet_path}")

        # Report file sizes
        print("\nFile sizes:")
        if os.path.exists(output_csv_path):
            csv_size = os.path.getsize(output_csv_path)
            print(f"  CSV: {csv_size:,} bytes ({csv_size / (1024**2):.2f} MB)")

        # For Parquet, Spark writes a directory; compute total size of all files within
        if os.path.exists(output_parquet_path):
            parquet_size_total = 0
            for root, _dirs, files in os.walk(output_parquet_path):
                for f in files:
                    parquet_size_total += os.path.getsize(os.path.join(root, f))
            print(
                f"  Parquet: {parquet_size_total:,} bytes ({parquet_size_total / (1024**2):.2f} MB)"
            )

            if os.path.exists(output_csv_path):
                compression_ratio = (csv_size - parquet_size_total) / csv_size * 100
                print(f"  Compression: Parquet is {compression_ratio:.1f}% smaller than CSV")

        # Display statistics using the class method
        print("\nBasic statistics of filtered data:")
        stats = transaction_filter.get_statistics()
        print(f"Number of transactions: {stats['num_transactions']:,}")
        print(f"Number of unique customers: {stats['num_unique_customers']:,}")
        print(f"Number of unique articles: {stats['num_unique_articles']:,}")
        print(f"Date range: {stats['date_range_start']} to {stats['date_range_end']}")

    except Exception as e:
        print(f"Error processing data (Spark): {e}")
        raise
    finally:
        # Stop Spark to free resources
        try:
            transaction_filter.spark.stop()  # type: ignore[attr-defined]
        except Exception:
            pass


if __name__ == "__main__":
    main()



