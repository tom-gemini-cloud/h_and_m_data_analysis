# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an H&M customer data analytics project using Polars for high-performance data processing and analysis. The project performs customer data examination, preprocessing, cleaning, and analysis on the H&M Kaggle dataset containing transactions, customer demographics, and product information.

## Dataset Structure

The project works with the H&M dataset components:
- `data/raw/transactions_train.csv` - Transaction records (31M+ records)
- `data/raw/customers.csv` - Customer demographic data (1.37M customers)  
- `data/raw/articles.csv` - Product/article metadata (105K products)
- `data/raw/images/` - Product image folders (organised by article ID prefixes)
- `data/processed/` - Cleaned and preprocessed datasets

## Development Commands

### Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Core dependencies include:
# - polars (high-performance data processing)
# - pandas, numpy (data manipulation)
# - matplotlib, seaborn, plotly (visualisation)
# - scikit-learn (machine learning)
# - jupyter, ipykernel (notebook support)
```

### Running Analysis Scripts
```bash
# Primary analysis workflow (run notebooks in sequence):
# 1. notebooks/data_understanding.ipynb - Data exploration and automated report generation
# 2. notebooks/feature_engineering.ipynb - TF-IDF, categorical, and combined feature engineering
# 3. notebooks/data_cleaning.ipynb - Polars-based preprocessing pipeline
# 4. notebooks/categorical_clustering.ipynb - K-means clustering with categorical features
# 5. notebooks/svd_clustering.ipynb - Clustering with TF-IDF SVD features

# Data processing pipeline scripts (run from Python):
python -m hnm_data_analysis.data_preprocessing.filter_last_3_months
python -m hnm_data_analysis.data_preprocessing.filter_related_data
```

### Memory Configuration & Performance
Scripts are optimised for local development with Polars configurations:
- Streaming chunk size: 100,000 rows for transaction processing
- Memory-efficient processing with lazy evaluation and chunked operations
- 12GB+ RAM recommended for full datasets (up from 8GB due to feature engineering)
- 10% sampling available for development mode via sampling parameters
- Feature engineering uses 50K customer batches to manage memory usage
- Parquet format provides 60-80% compression over CSV

### Development & Testing
```bash
# Run individual notebooks for interactive development
jupyter lab notebooks/

# Execute module scripts directly
python -c "from hnm_data_analysis.data_understanding.data_report_generator import generate_data_report; generate_data_report('data/processed/transactions_last_3_months.parquet')"

# Validation approaches used in the codebase:
# - Statistical validation in cleaning reports (results/cleaning/)
# - Data consistency checks in preprocessing modules
# - Feature distribution analysis in notebooks
# - Clustering quality metrics (silhouette, Calinski-Harabasz scores)
```

## Code Architecture

### Primary Analysis Workflow

**`notebooks/data_understanding.ipynb`**
- Comprehensive data exploration using Polars
- Quality assessment (missing values, duplicates, distributions)
- Cross-dataset integration and validation
- Statistical summaries and business insights

**`notebooks/feature_engineering.ipynb`**
- Advanced feature engineering producing 68+ features across categories:
  - RFM Analysis (Recency, Frequency, Monetary)
  - Product Preferences (category affinity, brand loyalty)
  - Demographics (age groups, club membership)
  - Temporal patterns (seasonality, shopping frequency)
  - Text Analysis (TF-IDF with PCA dimensionality reduction)
- Memory-optimised batch processing (50K customer batches)

**`notebooks/data_preprocessing_cleaning.ipynb`**
- Polars-based preprocessing pipeline
- Systematic missing value handling with business logic
- IQR-based outlier detection with capping
- Comprehensive data validation and consistency checks
- Parquet export for optimised downstream processing

### Data Processing Pipeline Architecture

The codebase implements a 4-stage data processing pipeline:

**Stage 1: Temporal Filtering (`hnm_data_analysis.data_preprocessing`)**
- `filter_last_3_months.py`: Filters transactions to last 90 days (2020-06-23 to 2020-09-22)
- `filter_related_data.py`: Filters customers/articles to only those present in filtered transactions
- Both support Polars implementation with Spark alternatives available

**Stage 2: Data Understanding & Quality (`hnm_data_analysis.data_understanding`)**
- `data_report_generator.py`: Generates comprehensive Markdown reports with schema analysis
- `outlier_analysis.py`: IQR-based outlier detection with business context
- Automated report generation to `results/data_documentation/`

**Stage 3: Data Cleaning (`hnm_data_analysis.data_cleaning`)**
- `data_cleaner.py`: Systematic missing value imputation, outlier capping, duplicate removal
- Produces cleaning reports with before/after statistics

**Stage 4: Feature Engineering (`hnm_data_analysis.feature_engineering`)**
- `customer_features.py`: RFM analysis, demographic features, shopping patterns  
- `articles_text_tfidf.py`: TF-IDF vectorisation with PCA compression (200 components)
- `categorical_features.py`: Mixed encoding strategy (one-hot + label encoding)

### Data Processing Pipeline

1. **Data Loading**: Polars CSV reading with schema inference and sampling support
2. **Integration**: Left joins preserve all transaction records while enriching with customer/product data
3. **Quality Assessment**: Systematic analysis of missing values (65% in customer data), duplicates, and outlier patterns
4. **Feature Engineering**: Multi-dimensional feature creation across behavioural, demographic, and product dimensions
5. **Preprocessing**: Missing value imputation, outlier handling, data validation
6. **Output**: Cleaned datasets saved as Parquet files for efficient downstream processing

### Feature Engineering Capabilities

The codebase implements sophisticated feature categorisation:
- **Customer Demographics**: age groups, club membership status, fashion engagement
- **Transaction Behaviour**: RFM metrics, purchase patterns, seasonal preferences
- **Product Information**: category hierarchies, price positioning, style preferences
- **Customer Preferences**: garment affinity, colour preferences, brand loyalty
- **Temporal Features**: seasonality, shopping frequency, trend adoption
- **Text Analysis**: TF-IDF vectorisation of product descriptions with PCA compression

### Polars Optimisations

- Lazy evaluation with streaming processing capabilities
- Efficient join operations with automatic optimisation
- Memory-conscious aggregations and window functions
- Built-in parallelisation for multi-core processing
- Native Parquet I/O for columnar data efficiency

## Important Notes

- **Memory Requirements**: Scripts require significant memory (12GB+ recommended) due to feature engineering complexity
- **Sampling**: Default 10% sampling available for memory optimisation during development
- **Data Quality**: H&M dataset has inherent missing values (65% in customer demographics) handled systematically
- **Feature Scale**: 68+ engineered features across multiple analytical dimensions including TF-IDF (200 components)
- **Performance**: Polars provides superior performance over Spark for single-machine workloads
- **Output Formats**: Parquet primary format (60-80% compression), CSV for compatibility
- **Data Flow**: Raw → Processed → Cleaned → Features → Results (each stage validates previous)

## Troubleshooting

### Common Issues
- **Memory errors**: Use sampling parameters in notebooks and scripts (sample_size=100000)
- **Missing data files**: Ensure raw data is in `data/raw/` directory
- **Path issues in notebooks**: Add `sys.path.append('../')` to access modules
- **Parquet compatibility**: All modules support CSV fallback if Parquet files unavailable
- **Feature engineering timeouts**: Reduce batch size from 50K to 10K customers in feature scripts

### File Dependencies
- Stage 1: Requires `data/raw/*.csv` files
- Stage 2: Requires Stage 1 output in `data/processed/`
- Stage 3: Requires Stage 2 output for cleaning
- Stage 4: Requires cleaned data from Stage 3
- Notebooks: Can work with any stage outputs but optimised for processed/cleaned data

## Business Context

This codebase supports advanced retail analytics applications:
- **Customer Segmentation**: K-means, hierarchical clustering with rich feature sets
- **Recommendation Systems**: Collaborative filtering with comprehensive user-item features
- **Predictive Analytics**: Temporal features support forecasting and trend analysis
- **Business Intelligence**: Customer behaviour analysis for fashion retail insights

## Documentation

Additional project documentation in `docs/`:
- `project_design_notes.md` - Comprehensive academic strategy and advanced technical approaches
- `segmentation_ideas.md` - Customer segmentation methodologies and business applications
- `sparkml_vs_traditional_comparison.md` - Technology comparison analysis
- `cleaning_notes.md` - Data cleaning strategies and missing value handling approaches

## Technical Excellence Features

- **Academic Rigour**: Publication-quality analysis following retail analytics best practices
- **Business Relevance**: Features directly applicable to fashion retail scenarios
- **Statistical Validation**: Proper methodology justification and comprehensive validation
- **Memory Optimisation**: Efficient processing of large datasets with intelligent sampling
- **Performance Monitoring**: Built-in memory usage tracking and optimisation guidance

## Module Structure & Key Classes

### `hnm_data_analysis.data_preprocessing`
- `TransactionFilter`: Filters transaction data to last 3 months with temporal windowing
- `DataFilter`: Filters articles and customers based on transaction presence
- Both classes support CSV and Parquet I/O with compression ratio reporting
- Spark alternatives available for distributed processing

### `hnm_data_analysis.data_understanding`
- `DataReportGenerator`: Generates comprehensive Markdown reports for data understanding
- `OutlierAnalyser`: IQR-based outlier detection with business context
- Supports both CSV and Parquet files with optional sampling
- Automatically saves reports to `results/data_documentation/`
- Includes schema analysis, quality metrics, statistical summaries, and recommendations

### `hnm_data_analysis.data_cleaning`
- `DataCleaner`: Systematic cleaning pipeline with missing value imputation and outlier handling
- Follows specifications from `docs/cleaning_notes.md`
- Produces detailed cleaning reports with before/after statistics

### `hnm_data_analysis.feature_engineering`
- `CustomerFeatures`: RFM analysis, demographic encoding, temporal patterns (50K customer batches)
- `ArticlesTextTfIdf`: TF-IDF vectorisation with PCA compression to 200 components
- `CategoricalFeatures`: Mixed encoding strategy optimised for fashion retail data

### `hnm_data_analysis.clustering`
- `ArticleClustering`: K-means and hierarchical clustering with combined features
- Supports both categorical and TF-IDF SVD features for multi-modal analysis

### Usage Patterns for Data Understanding Reports
```python
from hnm_data_analysis.data_understanding.data_report_generator import generate_data_report

# Generate comprehensive data report (saves to results/data_documentation/)
generate_data_report("data/processed/customers_last_3_months.parquet")

# With sampling for large datasets
generate_data_report("data/raw/transactions_train.csv", sample_size=100000)
```

### Notebook Integration
When working in notebooks, add project root to Python path:
```python
import sys
sys.path.append('../')  # From notebooks/ directory
from hnm_data_analysis.data_understanding.data_report_generator import generate_data_report
```

## Code Style Guidelines

- **UK Spellings**: All comments, docstrings, identifiers, and Markdown files use UK spellings (analyse, initialise, optimise, etc.)
- **Polars First**: Prefer Polars over pandas for data processing due to performance advantages
- **Memory Awareness**: Always consider memory usage and provide sampling options for large datasets
- **Documentation**: Detailed docstrings with business context and technical implementation details
- **Error Handling**: Robust error handling with informative messages for data quality issues
- **Language Preferences**: Avoid the word "comprehensive" in documentation and comments