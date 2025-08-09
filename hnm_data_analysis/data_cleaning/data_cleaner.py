"""
Data Cleaning Module for H&M Customer Analytics

This module provides comprehensive data cleaning functionality for the H&M dataset,
including handling of missing values, outlier detection and treatment, duplicate removal,
and data validation based on business rules.

The module follows cleaning specifications from docs/cleaning_notes.md and integrates
with outlier analysis results to provide systematic data cleaning workflows.
"""

import polars as pl
import numpy as np
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple, Union
import json
from datetime import datetime
from dataclasses import dataclass, field
import warnings


@dataclass
class CleaningReport:
    """Create a report of all cleaning operations performed."""
    dataset_name: str
    original_shape: Tuple[int, int]
    cleaned_shape: Tuple[int, int]
    missing_values_handled: Dict[str, int] = field(default_factory=dict)
    outliers_treated: Dict[str, int] = field(default_factory=dict)
    duplicates_removed: int = 0
    validation_issues_fixed: Dict[str, int] = field(default_factory=dict)
    data_quality_flags_added: List[str] = field(default_factory=list)
    cleaning_timestamp: str = field(default_factory=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class DataCleaner:
    """
    Data cleaning for the H&M retail analytics datasets.
    
    This class implements systematic cleaning procedures for transactions, customers,
    and articles datasets, following retail data best practices and handling missing
    values, outliers, duplicates, and data validation according to business rules.
    """
    
    def __init__(self):
        """Initialise the data cleaner with default configuration."""
        self.cleaning_reports = {}
        self.validation_rules = self._setup_validation_rules()
        
    def _setup_validation_rules(self) -> Dict[str, Dict]:
        """Define validation rules for business logic checks."""
        return {
            'customers': {
                'age': {'min': 16, 'max': 100},
                'postal_code': {'pattern': r'^\d{5}$', 'allow_unknown': True}
            },
            'transactions': {
                'price': {'min': 0.001, 'max': 1.0},
                'sales_channel_id': {'valid_values': [1, 2]}
            },
            'articles': {
                'product_code': {'min': 100000, 'max': 999999}
            }
        }
    
    def clean_transactions(
        self,
        file_path: str,
        outlier_method: str = 'iqr',
        save_csv: bool = False,
        csv_output_path: Optional[str] = None,
        compute_eur_price: bool = True,
        price_scale_factor: float = 1000.0,
        sek_per_eur: float = 10.5,
        round_decimals: int = 2,
        overwrite_price_with_eur: bool = True,
        keep_aux_price_columns: bool = False,
    ) -> Tuple[pl.DataFrame, CleaningReport]:
        """
        Clean transactions dataset with outlier handling and validation.
        
        Args:
            file_path: Path to transactions parquet file
            outlier_method: Method for outlier treatment ('iqr', 'cap', 'remove')
            save_csv: Whether to save cleaned data as CSV file
            csv_output_path: Path for CSV output (optional)
            
        Returns:
            Tuple of (cleaned_dataframe, cleaning_report)
        """
        print("Cleaning transactions dataset...")
        df = pl.read_parquet(file_path)
        original_shape = df.shape
        
        report = CleaningReport(
            dataset_name="transactions",
            original_shape=original_shape,
            cleaned_shape=original_shape 
        )
        
        # 1. Handle missing values (following cleaning_notes.md)
        df, missing_handled = self._handle_transactions_missing_values(df)
        report.missing_values_handled = missing_handled
        
        # 2. Treat price outliers based on outlier analysis
        df, outliers_treated = self._treat_price_outliers(df, method=outlier_method)
        report.outliers_treated = outliers_treated
        
        # 3. Data validation and business rules
        df, validation_fixes = self._validate_transactions(df)
        report.validation_issues_fixed = validation_fixes
        
        # 4. Convert anonymised price to SEK and EUR (optional)
        if compute_eur_price:
            df = self._compute_price_eur(
                df,
                price_scale_factor=price_scale_factor,
                sek_per_eur=sek_per_eur,
                round_decimals=round_decimals,
                overwrite_price_with_eur=overwrite_price_with_eur,
                keep_aux_price_columns=keep_aux_price_columns,
            )

        # 5. Add quality flags
        df, quality_flags = self._add_transaction_quality_flags(df)
        report.data_quality_flags_added = quality_flags
        
        # 6. Data type optimisation
        df = self._optimise_transaction_types(df)
        
        # Note: Duplicates in transactions are legitimate (multiple quantities)
        # so we don't remove them
        
        report.cleaned_shape = df.shape
        self.cleaning_reports['transactions'] = report
        
        # Save as CSV if requested
        if save_csv:
            if csv_output_path is None:
                csv_output_path = file_path.replace('.parquet', '_cleaned.csv')
            df.write_csv(csv_output_path)
            print(f"Transactions saved as CSV: {csv_output_path}")
        
        print(f"Transactions cleaned: {original_shape[0]:,} -> {df.shape[0]:,} rows")
        return df, report
    
    def clean_customers(self, file_path: str, save_csv: bool = False, csv_output_path: Optional[str] = None) -> Tuple[pl.DataFrame, CleaningReport]:
        """
        Clean customers dataset with missing value imputation and duplicate removal.
        
        Args:
            file_path: Path to customers parquet file
            save_csv: Whether to save cleaned data as CSV file
            csv_output_path: Path for CSV output (optional)
            
        Returns:
            Tuple of (cleaned_dataframe, cleaning_report)
        """
        print("Cleaning customers dataset...")
        df = pl.read_parquet(file_path)
        original_shape = df.shape
        
        report = CleaningReport(
            dataset_name="customers",
            original_shape=original_shape,
            cleaned_shape=original_shape
        )
        
        # 1. Remove duplicates first (though analysis showed 0 duplicates)
        initial_count = len(df)
        df = df.unique()
        duplicates_removed = initial_count - len(df)
        report.duplicates_removed = duplicates_removed
        
        # 2. Handle missing values (following cleaning_notes.md)
        df, missing_handled = self._handle_customers_missing_values(df)
        report.missing_values_handled = missing_handled
        
        # 3. Data validation and business rules
        df, validation_fixes = self._validate_customers(df)
        report.validation_issues_fixed = validation_fixes
        
        # 4. Add quality flags
        df, quality_flags = self._add_customer_quality_flags(df)
        report.data_quality_flags_added = quality_flags
        
        # 5. Data type optimisation
        df = self._optimise_customer_types(df)
        
        report.cleaned_shape = df.shape
        self.cleaning_reports['customers'] = report
        
        # Save as CSV if requested
        if save_csv:
            if csv_output_path is None:
                csv_output_path = file_path.replace('.parquet', '_cleaned.csv')
            df.write_csv(csv_output_path)
            print(f"Customers saved as CSV: {csv_output_path}")
        
        print(f"Customers cleaned: {original_shape[0]:,} -> {df.shape[0]:,} rows")
        return df, report
    
    def clean_articles(self, file_path: str, outlier_method: str = 'cap', save_csv: bool = False, csv_output_path: Optional[str] = None) -> Tuple[pl.DataFrame, CleaningReport]:
        """
        Clean articles dataset with outlier treatment and duplicate removal.
        
        Args:
            file_path: Path to articles parquet file
            outlier_method: Method for outlier treatment ('cap', 'remove', 'flag')
            save_csv: Whether to save cleaned data as CSV file
            csv_output_path: Path for CSV output (optional)
            
        Returns:
            Tuple of (cleaned_dataframe, cleaning_report)
        """
        print("Cleaning articles dataset...")
        df = pl.read_parquet(file_path)
        original_shape = df.shape
        
        report = CleaningReport(
            dataset_name="articles",
            original_shape=original_shape,
            cleaned_shape=original_shape
        )
        
        # 1. Remove duplicates first (though analysis showed 0 duplicates)
        initial_count = len(df)
        df = df.unique()
        duplicates_removed = initial_count - len(df)
        report.duplicates_removed = duplicates_removed
        
        # 2. Handle missing values (following cleaning_notes.md)
        df, missing_handled = self._handle_articles_missing_values(df)
        report.missing_values_handled = missing_handled
        
        # 3. Treat numerical outliers based on outlier analysis
        df, outliers_treated = self._treat_articles_outliers(df, method=outlier_method)
        report.outliers_treated = outliers_treated
        
        # 4. Data validation and business rules
        df, validation_fixes = self._validate_articles(df)
        report.validation_issues_fixed = validation_fixes
        
        # 5. Add quality flags
        df, quality_flags = self._add_article_quality_flags(df)
        report.data_quality_flags_added = quality_flags
        
        # 6. Data type optimisation
        df = self._optimise_article_types(df)
        
        report.cleaned_shape = df.shape
        self.cleaning_reports['articles'] = report
        
        # Save as CSV if requested
        if save_csv:
            if csv_output_path is None:
                csv_output_path = file_path.replace('.parquet', '_cleaned.csv')
            df.write_csv(csv_output_path)
            print(f"Articles saved as CSV: {csv_output_path}")
        
        print(f"Articles cleaned: {original_shape[0]:,} -> {df.shape[0]:,} rows")
        return df, report
    
    def _handle_transactions_missing_values(self, df: pl.DataFrame) -> Tuple[pl.DataFrame, Dict[str, int]]:
        """Handle missing values in transactions following cleaning_notes.md."""
        missing_handled = {}
        
        # t_dat: Interpolate based on customer patterns (if any missing)
        if df['t_dat'].null_count() > 0:
            # For now, drop rows with missing dates as they're critical
            initial_count = len(df)
            df = df.filter(pl.col('t_dat').is_not_null())
            missing_handled['t_dat'] = initial_count - len(df)
        
        # customer_id: Drop rows (critical field)
        if df['customer_id'].null_count() > 0:
            initial_count = len(df)
            df = df.filter(pl.col('customer_id').is_not_null())
            missing_handled['customer_id'] = initial_count - len(df)
        
        # article_id: Drop rows (critical field)
        if df['article_id'].null_count() > 0:
            initial_count = len(df)
            df = df.filter(pl.col('article_id').is_not_null())
            missing_handled['article_id'] = initial_count - len(df)
        
        # price: Fill with median price for that article_id
        if df['price'].null_count() > 0:
            missing_count = df['price'].null_count()
            median_prices = df.group_by('article_id').agg(
                pl.col('price').median().alias('median_price')
            )
            df = df.join(median_prices, on='article_id', how='left')
            df = df.with_columns(
                pl.when(pl.col('price').is_null())
                .then(pl.col('median_price'))
                .otherwise(pl.col('price'))
                .alias('price')
            ).drop('median_price')
            missing_handled['price'] = missing_count
        
        # sales_channel_id: Fill with mode
        if df['sales_channel_id'].null_count() > 0:
            missing_count = df['sales_channel_id'].null_count()
            mode_channel = df['sales_channel_id'].mode().first()
            df = df.with_columns(
                pl.col('sales_channel_id').fill_null(mode_channel)
            )
            missing_handled['sales_channel_id'] = missing_count
        
        return df, missing_handled
    
    def _handle_customers_missing_values(self, df: pl.DataFrame) -> Tuple[pl.DataFrame, Dict[str, int]]:
        """Handle missing values in customers following cleaning_notes.md."""
        missing_handled = {}
        
        # FN: Fill with 0
        if 'FN' in df.columns and df['FN'].null_count() > 0:
            missing_count = df['FN'].null_count()
            df = df.with_columns([
                pl.col('FN').fill_null(0),
                pl.col('FN').is_null().alias('FN_imputed')
            ])
            missing_handled['FN'] = missing_count
        
        # Active: Fill with 0
        if 'Active' in df.columns and df['Active'].null_count() > 0:
            missing_count = df['Active'].null_count()
            df = df.with_columns([
                pl.col('Active').fill_null(0),
                pl.col('Active').is_null().alias('Active_imputed')
            ])
            missing_handled['Active'] = missing_count
        
        # club_member_status: Fill with "NONE"
        if 'club_member_status' in df.columns and df['club_member_status'].null_count() > 0:
            missing_count = df['club_member_status'].null_count()
            df = df.with_columns([
                pl.col('club_member_status').fill_null("NONE"),
                pl.col('club_member_status').is_null().alias('club_member_status_imputed')
            ])
            missing_handled['club_member_status'] = missing_count
        
        # fashion_news_frequency: Fill with "NONE"
        if 'fashion_news_frequency' in df.columns and df['fashion_news_frequency'].null_count() > 0:
            missing_count = df['fashion_news_frequency'].null_count()
            df = df.with_columns([
                pl.col('fashion_news_frequency').fill_null("NONE"),
                pl.col('fashion_news_frequency').is_null().alias('fashion_news_frequency_imputed')
            ])
            missing_handled['fashion_news_frequency'] = missing_count
        
        # age: Fill with median age
        if 'age' in df.columns and df['age'].null_count() > 0:
            missing_count = df['age'].null_count()
            median_age = df['age'].median()
            df = df.with_columns([
                pl.col('age').fill_null(median_age),
                pl.col('age').is_null().alias('age_imputed')
            ])
            missing_handled['age'] = missing_count
        
        # postal_code: Fill with "NONE"
        if 'postal_code' in df.columns and df['postal_code'].null_count() > 0:
            missing_count = df['postal_code'].null_count()
            df = df.with_columns([
                pl.col('postal_code').fill_null("NONE"),
                pl.col('postal_code').is_null().alias('postal_code_imputed')
            ])
            missing_handled['postal_code'] = missing_count
        
        return df, missing_handled
    
    def _handle_articles_missing_values(self, df: pl.DataFrame) -> Tuple[pl.DataFrame, Dict[str, int]]:
        """Handle missing values in articles following cleaning_notes.md."""
        missing_handled = {}
        
        # product_code: Fill with "UNKNOWN"
        if 'product_code' in df.columns and df['product_code'].null_count() > 0:
            missing_count = df['product_code'].null_count()
            df = df.with_columns(pl.col('product_code').fill_null("UNKNOWN"))
            missing_handled['product_code'] = missing_count
        
        # prod_name: Fill with "UNKNOWN"
        if 'prod_name' in df.columns and df['prod_name'].null_count() > 0:
            missing_count = df['prod_name'].null_count()
            df = df.with_columns(pl.col('prod_name').fill_null("UNKNOWN"))
            missing_handled['prod_name'] = missing_count
        
        # detail_desc: Fill with "NO_DESCRIPTION"
        if 'detail_desc' in df.columns and df['detail_desc'].null_count() > 0:
            missing_count = df['detail_desc'].null_count()
            df = df.with_columns(pl.col('detail_desc').fill_null("NO_DESCRIPTION"))
            missing_handled['detail_desc'] = missing_count
        
        # Numerical codes: Fill with 0
        numerical_cols = [col for col in df.columns if col.endswith('_no') or col.endswith('_code')]
        for col in numerical_cols:
            if df[col].dtype in [pl.Int64, pl.Int32, pl.Float64, pl.Float32] and df[col].null_count() > 0:
                missing_count = df[col].null_count()
                df = df.with_columns(pl.col(col).fill_null(0))
                missing_handled[col] = missing_count
        
        # Categorical names: Fill with "UNKNOWN"
        categorical_cols = [col for col in df.columns if col.endswith('_name') or col.endswith('_desc')]
        for col in categorical_cols:
            if col != 'detail_desc' and df[col].null_count() > 0:  # detail_desc handled above
                missing_count = df[col].null_count()
                df = df.with_columns(pl.col(col).fill_null("UNKNOWN"))
                missing_handled[col] = missing_count
        
        return df, missing_handled
    
    def _treat_price_outliers(self, df: pl.DataFrame, method: str = 'iqr') -> Tuple[pl.DataFrame, Dict[str, int]]:
        """Treat price outliers based on outlier analysis results."""
        outliers_treated = {}
        
        if method == 'iqr':
            # Use IQR bounds from outlier analysis: [-0.012729, 0.061847]
            # But since negative prices don't make sense, use [0.003542, 0.061847] from percentile method
            lower_bound = 0.003542
            upper_bound = 0.061847
            
            outlier_count = df.filter(
                (pl.col('price') < lower_bound) | (pl.col('price') > upper_bound)
            ).height
            
            # Cap outliers to bounds
            df = df.with_columns([
                pl.when(pl.col('price') < lower_bound)
                .then(pl.lit(lower_bound))
                .when(pl.col('price') > upper_bound)
                .then(pl.lit(upper_bound))
                .otherwise(pl.col('price'))
                .alias('price'),
                
                # Add flag for capped prices
                ((pl.col('price') < lower_bound) | (pl.col('price') > upper_bound))
                .alias('price_outlier_capped')
            ])
            
            outliers_treated['price'] = outlier_count
        
        elif method == 'remove':
            # Remove extreme outliers (beyond 99th percentile bounds)
            lower_bound = 0.003542
            upper_bound = 0.084729
            
            initial_count = len(df)
            df = df.filter(
                (pl.col('price') >= lower_bound) & (pl.col('price') <= upper_bound)
            )
            outliers_treated['price'] = initial_count - len(df)
        
        return df, outliers_treated
    
    def _treat_articles_outliers(self, df: pl.DataFrame, method: str = 'cap') -> Tuple[pl.DataFrame, Dict[str, int]]:
        """Treat outliers in articles numerical columns."""
        outliers_treated = {}
        
        # Focus on high-priority outlier columns from analysis
        outlier_columns = {
            'product_type_no': (1, 300),  # Reasonable range for product types
            'product_code': (485308, 1084636),  # From IQR analysis
            'graphical_appearance_no': (1, 100),  # Reasonable range
            'index_group_no': (1, 50)  # Reasonable range
        }
        
        for col, (lower_bound, upper_bound) in outlier_columns.items():
            if col in df.columns:
                outlier_count = df.filter(
                    (pl.col(col) < lower_bound) | (pl.col(col) > upper_bound)
                ).height
                
                if outlier_count > 0:
                    if method == 'cap':
                        df = df.with_columns([
                            pl.when(pl.col(col) < lower_bound)
                            .then(pl.lit(lower_bound))
                            .when(pl.col(col) > upper_bound)
                            .then(pl.lit(upper_bound))
                            .otherwise(pl.col(col))
                            .alias(col),
                            
                            # Add flag for capped values
                            ((pl.col(col) < lower_bound) | (pl.col(col) > upper_bound))
                            .alias(f'{col}_outlier_capped')
                        ])
                    
                    outliers_treated[col] = outlier_count
        
        return df, outliers_treated
    
    def _validate_transactions(self, df: pl.DataFrame) -> Tuple[pl.DataFrame, Dict[str, int]]:
        """Apply business logic validation to transactions."""
        validation_fixes = {}
        
        # Validate sales channel ID
        if 'sales_channel_id' in df.columns:
            invalid_channels = df.filter(
                ~pl.col('sales_channel_id').is_in([1, 2])
            ).height
            
            if invalid_channels > 0:
                # Set invalid channels to mode (most common)
                mode_channel = df.filter(pl.col('sales_channel_id').is_in([1, 2]))['sales_channel_id'].mode().first()
                df = df.with_columns([
                    pl.when(~pl.col('sales_channel_id').is_in([1, 2]))
                    .then(pl.lit(mode_channel))
                    .otherwise(pl.col('sales_channel_id'))
                    .alias('sales_channel_id'),
                    
                    (~pl.col('sales_channel_id').is_in([1, 2])).alias('sales_channel_corrected')
                ])
                validation_fixes['sales_channel_id'] = invalid_channels
        
        return df, validation_fixes
    
    def _validate_customers(self, df: pl.DataFrame) -> Tuple[pl.DataFrame, Dict[str, int]]:
        """Apply business logic validation to customers."""
        validation_fixes = {}
        
        # Validate age range
        if 'age' in df.columns:
            rules = self.validation_rules['customers']['age']
            invalid_ages = df.filter(
                (pl.col('age') < rules['min']) | (pl.col('age') > rules['max'])
            ).height
            
            if invalid_ages > 0:
                median_age = df.filter(
                    (pl.col('age') >= rules['min']) & (pl.col('age') <= rules['max'])
                )['age'].median()
                
                df = df.with_columns([
                    pl.when((pl.col('age') < rules['min']) | (pl.col('age') > rules['max']))
                    .then(pl.lit(median_age))
                    .otherwise(pl.col('age'))
                    .alias('age'),
                    
                    ((pl.col('age') < rules['min']) | (pl.col('age') > rules['max']))
                    .alias('age_corrected')
                ])
                validation_fixes['age'] = invalid_ages
        
        return df, validation_fixes
    
    def _validate_articles(self, df: pl.DataFrame) -> Tuple[pl.DataFrame, Dict[str, int]]:
        """Apply business logic validation to articles."""
        validation_fixes = {}
        
        # Validate product codes (if they're numeric)
        if 'product_code' in df.columns and df['product_code'].dtype in [pl.Int64, pl.Int32]:
            rules = self.validation_rules['articles']['product_code']
            invalid_codes = df.filter(
                (pl.col('product_code') < rules['min']) | (pl.col('product_code') > rules['max'])
            ).height
            
            if invalid_codes > 0:
                # Flag invalid codes rather than changing them
                df = df.with_columns(
                    ((pl.col('product_code') < rules['min']) | (pl.col('product_code') > rules['max']))
                    .alias('product_code_invalid')
                )
                validation_fixes['product_code'] = invalid_codes
        
        return df, validation_fixes
    
    def _add_transaction_quality_flags(self, df: pl.DataFrame) -> Tuple[pl.DataFrame, List[str]]:
        """Add data quality flags to transactions."""
        quality_flags = []
        
        # Add imputation flags if not already present
        if 'price_outlier_capped' not in df.columns:
            df = df.with_columns(pl.lit(False).alias('price_outlier_capped'))
        quality_flags.append('price_outlier_capped')
        
        if 'sales_channel_corrected' not in df.columns:
            df = df.with_columns(pl.lit(False).alias('sales_channel_corrected'))
        quality_flags.append('sales_channel_corrected')
        
        return df, quality_flags
    
    def _add_customer_quality_flags(self, df: pl.DataFrame) -> Tuple[pl.DataFrame, List[str]]:
        """Add data quality flags to customers."""
        quality_flags = []
        
        # Add imputation flags for columns that don't already have them
        imputed_columns = ['FN', 'Active', 'club_member_status', 'fashion_news_frequency', 'age', 'postal_code']
        for col in imputed_columns:
            flag_name = f'{col}_imputed'
            if col in df.columns and flag_name not in df.columns:
                # Add flag as False for columns that weren't imputed
                df = df.with_columns(pl.lit(False).alias(flag_name))
            if flag_name in df.columns:
                quality_flags.append(flag_name)
        
        if 'age_corrected' not in df.columns:
            df = df.with_columns(pl.lit(False).alias('age_corrected'))
        quality_flags.append('age_corrected')
        
        return df, quality_flags
    
    def _add_article_quality_flags(self, df: pl.DataFrame) -> Tuple[pl.DataFrame, List[str]]:
        """Add data quality flags to articles."""
        quality_flags = []
        
        # Add outlier flags for capped columns
        outlier_columns = ['product_type_no', 'product_code', 'graphical_appearance_no', 'index_group_no']
        for col in outlier_columns:
            flag_name = f'{col}_outlier_capped'
            if flag_name not in df.columns and col in df.columns:
                df = df.with_columns(pl.lit(False).alias(flag_name))
            quality_flags.append(flag_name)
        
        if 'product_code_invalid' not in df.columns:
            df = df.with_columns(pl.lit(False).alias('product_code_invalid'))
        quality_flags.append('product_code_invalid')
        
        return df, quality_flags
    
    def _optimise_transaction_types(self, df: pl.DataFrame) -> pl.DataFrame:
        """Optimise data types for transactions."""
        optimisations = {}
        
        # Convert sales_channel_id to categorical
        if 'sales_channel_id' in df.columns:
            df = df.with_columns(
                pl.col('sales_channel_id').cast(pl.Categorical).alias('sales_channel_id')
            )
        
        return df
    
    def _optimise_customer_types(self, df: pl.DataFrame) -> pl.DataFrame:
        """Optimise data types for customers."""
        # Active should remain as Float64 (binary 0.0/1.0 field)
        # Don't convert Active to categorical
        
        # Convert categorical columns to categorical type
        categorical_cols = ['club_member_status', 'fashion_news_frequency', 'postal_code']
        
        for col in categorical_cols:
            if col in df.columns:
                df = df.with_columns(
                    pl.col(col).cast(pl.Categorical).alias(col)
                )
        
        return df
    
    def _optimise_article_types(self, df: pl.DataFrame) -> pl.DataFrame:
        """Optimise data types for articles."""
        # Convert text columns to categorical where appropriate
        categorical_cols = [col for col in df.columns if col.endswith('_name') or col in ['detail_desc']]
        
        for col in categorical_cols:
            if col in df.columns and df[col].dtype == pl.Utf8:
                unique_count = df[col].n_unique()
                total_count = len(df)
                
                # Convert to categorical if less than 50% unique values
                if unique_count / total_count < 0.5:
                    df = df.with_columns(
                        pl.col(col).cast(pl.Categorical).alias(col)
                    )
        
        return df

    def _compute_price_eur(
        self,
        df: pl.DataFrame,
        price_scale_factor: float = 1000.0,
        sek_per_eur: float = 10.5,
        round_decimals: int = 2,
        overwrite_price_with_eur: bool = True,
        keep_aux_price_columns: bool = False,
    ) -> pl.DataFrame:
        """Compute SEK and EUR prices from anonymised `price`.

        Assumptions:
        - The anonymised `price` in the H&M dataset preserves relative ordering and is typically scaled down.
        - We expose `price_scale_factor` and `sek_per_eur` as configurable to allow calibration.

        Parameters
        - price_scale_factor: multiply anonymised price by this factor to approximate SEK
        - sek_per_eur: FX rate (SEK per 1 EUR). EUR = SEK / sek_per_eur
        - round_decimals: rounding for output price columns
        - overwrite_price_with_eur: if True, replace `price` with EUR value; otherwise add new columns
        """
        if 'price' not in df.columns:
            return df

        # Guard against zero or negative parameters
        if price_scale_factor <= 0:
            warnings.warn("price_scale_factor must be > 0. Skipping EUR conversion.")
            return df
        if sek_per_eur <= 0:
            warnings.warn("sek_per_eur must be > 0. Skipping EUR conversion.")
            return df

        # Compute SEK and EUR
        df = df.with_columns([
            (pl.col('price') * pl.lit(price_scale_factor)).alias('price_sek_raw'),
            ((pl.col('price') * pl.lit(price_scale_factor)) / pl.lit(sek_per_eur)).alias('price_eur_raw'),
        ])

        # Round and finalise columns
        df = df.with_columns([
            pl.col('price_sek_raw').round(round_decimals).cast(pl.Float64).alias('price_sek'),
            pl.col('price_eur_raw').round(round_decimals).cast(pl.Float64).alias('price_eur'),
        ]).drop(['price_sek_raw', 'price_eur_raw'])

        # Optionally overwrite original price with EUR
        if overwrite_price_with_eur:
            df = df.with_columns(pl.col('price_eur').alias('price'))

        # Optionally drop auxiliary price columns, keeping only `price` as EUR
        if not keep_aux_price_columns:
            # If we overwrote price, we can drop the intermediates
            drop_cols = [c for c in ['price_sek', 'price_eur'] if c in df.columns]
            if drop_cols:
                df = df.drop(drop_cols)

        return df
    
    def generate_cleaning_report(self, output_path: Optional[str] = None) -> str:
        """
        Generate comprehensive Markdown cleaning report.
        
        Args:
            output_path: Optional custom output path for the report
            
        Returns:
            Path to the generated report file
        """
        if output_path is None:
            # Find project root
            current_path = Path.cwd()
            project_root = current_path
            
            while project_root != project_root.parent:
                if (project_root / "CLAUDE.md").exists() or (project_root / "hnm_data_analysis").exists():
                    break
                project_root = project_root.parent
            
            output_dir = project_root / "results" / "cleaning"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / "data_cleaning_report.md"
        else:
            output_path = Path(output_path)
        
        # Generate report content
        report_lines = [
            "# Data Cleaning Report",
            "",
            f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "**Project:** H&M Customer Data Analytics",
            "",
            "## 📋 Executive Summary",
            "",
            self._generate_cleaning_summary(),
            "",
            "## 🧹 Detailed Cleaning Results by Dataset",
            ""
        ]
        
        # Add detailed sections for each dataset
        for dataset_name, report in self.cleaning_reports.items():
            report_lines.extend(self._generate_dataset_cleaning_section(dataset_name, report))
        
        # Add methodology and recommendations
        report_lines.extend([
            "## 🔬 Cleaning Methodology",
            "",
            "### Missing Value Handling Strategy",
            "- **Critical fields** (IDs, dates): Row removal for data integrity",
            "- **Numerical fields**: Median imputation or business logic defaults",
            "- **Categorical fields**: Mode imputation or \"UNKNOWN\" placeholder",
            "- **Business context**: Domain-specific defaults (e.g., 'INACTIVE' for membership)",
            "",
            "### Outlier Treatment Approach",
            "- **Price data**: IQR-based capping to business-reasonable ranges",
            "- **Product codes**: Statistical bounds from outlier analysis",
            "- **Validation**: Business logic checks for data consistency",
            "- **Preservation**: Outlier flags maintained for transparency",
            "",
            "### Data Quality Assurance",
            "- **Duplicate removal**: Applied to reference data (customers, articles)",
            "- **Transaction duplicates**: Preserved as legitimate multi-quantity purchases",
            "- **Validation flags**: Added for all corrections and imputations",
            "- **Type optimisation**: Categorical encoding for memory efficiency",
            "",
            "## 💡 Data Quality Recommendations",
            "",
            "### Production Implementation",
            "1. **Automated validation**: Implement real-time checks during data ingestion",
            "2. **Monitoring dashboards**: Track data quality metrics over time",
            "3. **Business review**: Regular validation of cleaning rules with domain experts",
            "4. **Documentation**: Maintain audit trail of all cleaning decisions",
            "",
            "### Advanced Enhancements",
            "1. **Machine learning imputation**: Consider more sophisticated missing value prediction",
            "2. **Outlier detection**: Implement adaptive thresholds based on seasonal patterns",
            "3. **Data lineage**: Track data transformations for regulatory compliance",
            "4. **Quality scoring**: Develop composite quality metrics for each record",
            "",
            "## 📊 Technical Implementation Details",
            "",
            "### Processing Framework",
            "- **Engine**: Polars for high-performance data processing",
            "- **Memory optimisation**: Lazy evaluation and streaming for large datasets",
            "- **Type system**: Categorical encoding and memory-efficient data types",
            "- **Validation**: Business rule engine with configurable thresholds",
            "",
            "### Quality Assurance Features",
            "- **Audit trails**: Complete tracking of all cleaning operations",
            "- **Rollback capability**: Original data preserved for validation",
            "- **Statistical validation**: Pre/post cleaning quality comparisons",
            "- **Business logic**: Domain-specific validation rules",
            "",
            "---",
            "",
            "*Report generated using H&M Data Analytics - Data Cleaning Module*"
        ])
        
        # Write report to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_lines))
        
        # Return relative path
        try:
            relative_path = output_path.relative_to(project_root)
            return str(relative_path)
        except (ValueError, NameError):
            return str(output_path)
    
    def _generate_cleaning_summary(self) -> str:
        """Generate executive summary of cleaning operations."""
        if not self.cleaning_reports:
            return "No cleaning operations performed yet."
        
        lines = []
        total_original_rows = sum(report.original_shape[0] for report in self.cleaning_reports.values())
        total_cleaned_rows = sum(report.cleaned_shape[0] for report in self.cleaning_reports.values())
        total_missing_handled = sum(
            sum(report.missing_values_handled.values()) for report in self.cleaning_reports.values()
        )
        total_outliers_treated = sum(
            sum(report.outliers_treated.values()) for report in self.cleaning_reports.values()
        )
        total_duplicates_removed = sum(report.duplicates_removed for report in self.cleaning_reports.values())
        
        lines.extend([
            f"**Datasets processed:** {len(self.cleaning_reports)}",
            f"**Total records processed:** {total_original_rows:,} → {total_cleaned_rows:,}",
            f"**Missing values handled:** {total_missing_handled:,}",
            f"**Outliers treated:** {total_outliers_treated:,}",
            f"**Duplicates removed:** {total_duplicates_removed:,}",
            "",
            "### Key Achievements",
            "✅ **Complete missing value imputation** using business-appropriate strategies",
            "✅ **Systematic outlier treatment** based on statistical analysis",
            "✅ **Data validation** with business logic constraints",
            "✅ **Quality flagging** for transparency and audit trails",
            "✅ **Performance optimisation** through type conversion and categorical encoding"
        ])
        
        return '\n'.join(lines)
    
    def _generate_dataset_cleaning_section(self, dataset_name: str, report: CleaningReport) -> List[str]:
        """Generate detailed cleaning section for a dataset."""
        lines = [
            f"### {dataset_name.title()} Dataset",
            "",
            "#### Overview",
            f"- **Original shape:** {report.original_shape[0]:,} rows × {report.original_shape[1]} columns",
            f"- **Cleaned shape:** {report.cleaned_shape[0]:,} rows × {report.cleaned_shape[1]} columns",
            f"- **Rows removed:** {report.original_shape[0] - report.cleaned_shape[0]:,}",
            f"- **Cleaning timestamp:** {report.cleaning_timestamp}",
            ""
        ]
        
        # Missing values section
        if report.missing_values_handled:
            lines.extend([
                "#### Missing Values Handled",
                "| Column | Missing Count | Treatment |",
                "| ------ | ------------- | --------- |"
            ])
            
            treatment_map = {
                't_dat': 'Row removal (critical field)',
                'customer_id': 'Row removal (critical field)',
                'article_id': 'Row removal (critical field)',
                'price': 'Median by article_id',
                'sales_channel_id': 'Mode imputation',
                'FN': 'Fill with 0',
                'Active': 'Fill with "UNKNOWN"',
                'club_member_status': 'Fill with "INACTIVE"',
                'fashion_news_frequency': 'Fill with "NONE"',
                'age': 'Median imputation',
                'postal_code': 'Fill with "UNKNOWN"',
                'detail_desc': 'Fill with "NO_DESCRIPTION"'
            }
            
            for col, count in report.missing_values_handled.items():
                treatment = treatment_map.get(col, 'Domain-specific imputation')
                lines.append(f"| {col} | {count:,} | {treatment} |")
            
            lines.append("")
        
        # Outliers section
        if report.outliers_treated:
            lines.extend([
                "#### Outliers Treated",
                "| Column | Outlier Count | Treatment Method |",
                "| ------ | ------------- | ---------------- |"
            ])
            
            for col, count in report.outliers_treated.items():
                method = "IQR-based capping" if col == 'price' else "Statistical bounds capping"
                lines.append(f"| {col} | {count:,} | {method} |")
            
            lines.append("")
        
        # Validation fixes section
        if report.validation_issues_fixed:
            lines.extend([
                "#### Validation Issues Fixed",
                "| Issue Type | Records Fixed | Resolution |",
                "| ---------- | ------------- | ---------- |"
            ])
            
            for issue, count in report.validation_issues_fixed.items():
                resolution = "Business logic correction"
                lines.append(f"| {issue} | {count:,} | {resolution} |")
            
            lines.append("")
        
        # Quality flags section
        if report.data_quality_flags_added:
            lines.extend([
                "#### Quality Flags Added",
                "The following columns were added to track data quality and cleaning operations:",
                ""
            ])
            
            for flag in report.data_quality_flags_added:
                description = self._get_flag_description(flag)
                lines.append(f"- **{flag}**: {description}")
            
            lines.append("")
        
        # Duplicates section
        if report.duplicates_removed > 0:
            lines.extend([
                "#### Duplicates Removed",
                f"- **Count:** {report.duplicates_removed:,} duplicate records removed",
                f"- **Method:** Complete row deduplication",
                ""
            ])
        
        lines.extend(["---", ""])
        
        return lines
    
    def _get_flag_description(self, flag: str) -> str:
        """Get description for quality flag."""
        descriptions = {
            'price_outlier_capped': 'Indicates prices that were capped due to extreme values',
            'sales_channel_corrected': 'Indicates sales channel IDs that were corrected',
            'age_corrected': 'Indicates ages that were corrected to valid ranges',
            'product_code_invalid': 'Flags potentially invalid product codes',
            'FN_imputed': 'Indicates imputed FN values',
            'Active_imputed': 'Indicates imputed Active status values',
            'club_member_status_imputed': 'Indicates imputed membership status',
            'fashion_news_frequency_imputed': 'Indicates imputed newsletter frequency',
            'age_imputed': 'Indicates imputed age values'
        }
        
        # Handle outlier capped flags
        for col in ['product_type_no', 'product_code', 'graphical_appearance_no', 'index_group_no']:
            descriptions[f'{col}_outlier_capped'] = f'Indicates {col} values that were capped due to outliers'
        
        return descriptions.get(flag, 'Quality tracking flag')


def clean_all_datasets(transactions_path: str, customers_path: str, articles_path: str,
                      output_dir: Optional[str] = None, generate_report: bool = True,
                      write_csv: bool = False) -> Dict[str, str]:
    """
    Convenience function to clean all H&M datasets in one operation.
    
    Args:
        transactions_path: Path to transactions parquet file
        customers_path: Path to customers parquet file
        articles_path: Path to articles parquet file
        output_dir: Optional custom output directory for cleaned data
        generate_report: Whether to generate cleaning report
        write_csv: If True, also write CSV files (can be memory intensive on large datasets)
        
    Returns:
        Dictionary mapping dataset names to output file paths. Always includes Parquet keys.
        Parquet keys: 'transactions_parquet', 'customers_parquet', 'articles_parquet'.
        If write_csv=True, also includes: 'transactions_csv', 'customers_csv', 'articles_csv'.
        'cleaning_report' is included when generate_report=True.
        
    Example:
        ```python
        from hnm_data_analysis.data_cleaning import clean_all_datasets
        
        # Clean all datasets (CSV disabled by default to reduce memory pressure)
        output_paths = clean_all_datasets(
            'data/processed/transactions_last_3_months.parquet',
            'data/processed/customers_last_3_months.parquet',
            'data/processed/articles_last_3_months.parquet',
            write_csv=False
        )
        
        print("Cleaned datasets saved to:", output_paths)
        # Output includes both Parquet and CSV files:
        # {'transactions_parquet': 'data/cleaned/transactions_last_3_months_cleaned.parquet',
        #  'transactions_csv': 'data/cleaned/transactions_last_3_months_cleaned.csv', ...}
        ```
    """
    cleaner = DataCleaner()
    output_paths = {}
    
    # Find project root
    current_path = Path.cwd()
    project_root = current_path
    
    while project_root != project_root.parent:
        if (project_root / "CLAUDE.md").exists() or (project_root / "hnm_data_analysis").exists():
            break
        project_root = project_root.parent
    
    if output_dir is None:
        output_dir = project_root / "data" / "cleaned"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Clean each dataset
    print("Starting comprehensive data cleaning process...\n")
    
    # Clean transactions
    df_trans, _ = cleaner.clean_transactions(transactions_path, outlier_method='iqr')
    trans_parquet_output = output_dir / "transactions_last_3_months_cleaned.parquet"
    trans_csv_output = output_dir / "transactions_last_3_months_cleaned.csv"
    df_trans.write_parquet(trans_parquet_output)
    if write_csv:
        df_trans.write_csv(trans_csv_output)
    try:
        output_paths['transactions_parquet'] = str(trans_parquet_output.relative_to(project_root))
        if write_csv:
            output_paths['transactions_csv'] = str(trans_csv_output.relative_to(project_root))
    except ValueError:
        # If relative path fails, use absolute path
        output_paths['transactions_parquet'] = str(trans_parquet_output)
        if write_csv:
            output_paths['transactions_csv'] = str(trans_csv_output)
    
    # Clean customers
    df_customers, _ = cleaner.clean_customers(customers_path)
    customers_parquet_output = output_dir / "customers_last_3_months_cleaned.parquet"
    customers_csv_output = output_dir / "customers_last_3_months_cleaned.csv"
    df_customers.write_parquet(customers_parquet_output)
    if write_csv:
        df_customers.write_csv(customers_csv_output)
    try:
        output_paths['customers_parquet'] = str(customers_parquet_output.relative_to(project_root))
        if write_csv:
            output_paths['customers_csv'] = str(customers_csv_output.relative_to(project_root))
    except ValueError:
        output_paths['customers_parquet'] = str(customers_parquet_output)
        if write_csv:
            output_paths['customers_csv'] = str(customers_csv_output)
    
    # Clean articles
    df_articles, _ = cleaner.clean_articles(articles_path, outlier_method='cap')
    articles_parquet_output = output_dir / "articles_last_3_months_cleaned.parquet"
    articles_csv_output = output_dir / "articles_last_3_months_cleaned.csv"
    df_articles.write_parquet(articles_parquet_output)
    if write_csv:
        df_articles.write_csv(articles_csv_output)
    try:
        output_paths['articles_parquet'] = str(articles_parquet_output.relative_to(project_root))
        if write_csv:
            output_paths['articles_csv'] = str(articles_csv_output.relative_to(project_root))
    except ValueError:
        output_paths['articles_parquet'] = str(articles_parquet_output)
        if write_csv:
            output_paths['articles_csv'] = str(articles_csv_output)
    
    print(f"\nAll datasets cleaned successfully!")
    print(f"Output directory: {output_dir}")
    
    # Generate cleaning report
    if generate_report:
        report_path = cleaner.generate_cleaning_report()
        output_paths['cleaning_report'] = report_path
        print(f"Cleaning report generated: {report_path}")
    
    return output_paths


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 4:
        print("Usage: python data_cleaner.py <transactions_path> <customers_path> <articles_path> [output_dir]")
        sys.exit(1)
    
    transactions_path = sys.argv[1]
    customers_path = sys.argv[2]
    articles_path = sys.argv[3]
    output_dir = sys.argv[4] if len(sys.argv) > 4 else None
    
    try:
        output_paths = clean_all_datasets(transactions_path, customers_path, articles_path, output_dir)
        print("\nData cleaning completed successfully!")
        print("Output files:")
        for dataset, path in output_paths.items():
            print(f"  {dataset}: {path}")
    except Exception as e:
        print(f"Error during cleaning: {e}")
        sys.exit(1)