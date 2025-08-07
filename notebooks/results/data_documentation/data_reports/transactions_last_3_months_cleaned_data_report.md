# Data Understanding Report
**Generated on:** 2025-08-07 10:35:48
**File:** transactions_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `../data/cleaned/transactions_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 52.6 MB
- **Last Modified:** 2025-08-07 10:35:45

## 📊 Dataset Overview
- **Rows:** 3,904,391
- **Columns:** 7
- **Total Cells:** 27,330,737

## 🔍 Data Quality Summary
- **Completeness Score:** 85.71%
- **Missing Values:** 3,904,391 (14.29%)
- **Duplicate Rows:** 329,004 (8.43%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | Date | 0 | 0.0% | 91 | 0.0% |
| customer_id | String | 0 | 0.0% | 525,075 | 13.45% |
| article_id | Int64 | 0 | 0.0% | 42,298 | 1.08% |
| price | Float64 | 0 | 0.0% | 3,306 | 0.08% |
| sales_channel_id | Categorical | 3,904,391 | 100.0% | 1 | 0.0% |
| price_outlier_capped | Boolean | 0 | 0.0% | 2 | 0.0% |
| sales_channel_corrected | Boolean | 0 | 0.0% | 1 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| article_id | 3904391 | 791482176.6992 | N/A | 108775015 | N/A | N/A | N/A | 956217002 |
| price | 3904391 | 0.0258 | N/A | 0.003542 | N/A | N/A | N/A | 0.061847 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `d858499e511e19f3bed3a8b4d2a9749ba16688f9ea14497c2e2f8314aa1689de`: 3 occurrences
  - `8652b7f560875cb12324c3e3dda6b4645760832eb8bed4425bb828dc6d9c496a`: 18 occurrences
  - `ffc8b04d453c3e4246c7321fa00537cc78efa02db00e7113385bd4dc594e3a3e`: 5 occurrences
  - `06bc17bae59f98f06224ff29c5fede2f520b9dc060db18bf4e1d0519503d1f0b`: 2 occurrences
  - `f35e98c1771a275db51c3f8cfd48fac9310cb46c42fb3b522585835ebe8216a5`: 3 occurrences

### sales_channel_id
- **Unique Values:** 1
- **Top Values:**
  - `None`: 3,904,391 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 329.07 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 14.8941 |
| customer_id | 238.3051 |
| article_id | 29.7881 |
| price | 29.7881 |
| sales_channel_id | 15.3595 |
| price_outlier_capped | 0.4655 |
| sales_channel_corrected | 0.4655 |

## 💡 Data Quality Recommendations
- **High missing values detected** - Consider imputation strategies or investigate data collection issues
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** price_outlier_capped - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*