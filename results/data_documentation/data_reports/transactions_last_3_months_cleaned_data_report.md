# Data Understanding Report
**Generated on:** 2025-08-09 11:20:41
**File:** transactions_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\transactions_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 52.6 MB
- **Last Modified:** 2025-08-09 11:20:33

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
  - `1b8ac63273d6405d16421451d55cdeec57be2ece3639286c62d8d09d6d74c38e`: 1 occurrences
  - `9dd24c07abd3cf5a91280c2cca62e2f47ef85c275955fc0def6c568b40e67639`: 8 occurrences
  - `8a8a93d92395cea147abaa1479b8ef698a9c222b3f5d8e043d58afda4364a8ba`: 2 occurrences
  - `f9fe07e4685446e2e41af2b4ecbc864f034b6da6ab20b034249a9ad969dbbb03`: 1 occurrences
  - `cb791824fda0f57baad04dc940eabeef5e6f5f4dce17b415aca82c2e1d105185`: 2 occurrences

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