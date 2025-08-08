# Data Understanding Report
**Generated on:** 2025-08-07 16:44:34
**File:** transactions_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\transactions_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 52.6 MB
- **Last Modified:** 2025-08-07 16:44:27

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
  - `a8e1e22b3fa9eef9ce86feb31ef81ba6dfbaef1d98603db82e6e1b94d74fbb03`: 9 occurrences
  - `fc3cfa4d46c423f84ab9ce391335906e64e53ba9be51d9684c881b3f73730bed`: 13 occurrences
  - `5aba6562dc8b6a1f6f5e709e5f1d0927150a453d639e6b39296a135725457f23`: 3 occurrences
  - `65111c4198b2538354afa24d3dc170f5189efb1e9b7ecdf6849d01a6bad70571`: 4 occurrences
  - `961f465dc81e89e9b61cf80c4c173d177d688cf5694f9436ad480f3010512425`: 5 occurrences

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