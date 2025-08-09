# Data Understanding Report
**Generated on:** 2025-08-09 11:48:59
**File:** transactions_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\transactions_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 52.42 MB
- **Last Modified:** 2025-08-09 11:48:52

## 📊 Dataset Overview
- **Rows:** 3,904,391
- **Columns:** 7
- **Total Cells:** 27,330,737

## 🔍 Data Quality Summary
- **Completeness Score:** 85.71%
- **Missing Values:** 3,904,391 (14.29%)
- **Duplicate Rows:** 335,131 (8.58%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | Date | 0 | 0.0% | 91 | 0.0% |
| customer_id | String | 0 | 0.0% | 525,075 | 13.45% |
| article_id | Int64 | 0 | 0.0% | 42,298 | 1.08% |
| price | Float64 | 0 | 0.0% | 556 | 0.01% |
| sales_channel_id | Categorical | 3,904,391 | 100.0% | 1 | 0.0% |
| price_outlier_capped | Boolean | 0 | 0.0% | 2 | 0.0% |
| sales_channel_corrected | Boolean | 0 | 0.0% | 1 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| article_id | 3904391 | 791482176.6992 | N/A | 108775015 | N/A | N/A | N/A | 956217002 |
| price | 3904391 | 2.4585 | N/A | 0.34 | N/A | N/A | N/A | 5.89 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `cc0281139f4f608b6bbc9c6af09da3a9f18aefe42c6bb7425cf29b19fe2ab77f`: 4 occurrences
  - `a726071db3d1b6e6283410345ae931d4c2f19702d8fe5f9d7e6f3f200398551c`: 2 occurrences
  - `a21ef83a47f218bd13c25c9aa382cb27810195ce3cfcf34f2eaba8805d0f8d5b`: 21 occurrences
  - `a97d5297c7bbd101797e5c68fdfbabc9212c06f261cda8d8cf105207cd22894c`: 22 occurrences
  - `f047b23a3049abf5c8618b2ad76ecdcfabc9ecc8ab228e13e9b2262d0efb5140`: 11 occurrences

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