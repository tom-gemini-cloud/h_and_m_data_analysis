# Data Understanding Report
**Generated on:** 2025-08-09 15:12:52
**File:** transactions_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\transactions_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 53.69 MB
- **Last Modified:** 2025-08-09 15:12:45

## 📊 Dataset Overview
- **Rows:** 3,904,391
- **Columns:** 8
- **Total Cells:** 31,235,128

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 328,885 (8.42%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | Date | 0 | 0.0% | 91 | 0.0% |
| customer_id | String | 0 | 0.0% | 525,075 | 13.45% |
| article_id | Int64 | 0 | 0.0% | 42,298 | 1.08% |
| price | Float64 | 0 | 0.0% | 3,236 | 0.08% |
| sales_channel_id | Int64 | 0 | 0.0% | 2 | 0.0% |
| price_outlier_capped | Boolean | 0 | 0.0% | 2 | 0.0% |
| sales_channel_corrected | Boolean | 0 | 0.0% | 1 | 0.0% |
| price_percentile_calibrated | Boolean | 0 | 0.0% | 1 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| article_id | 3904391 | 791482176.6992 | N/A | 108775015 | N/A | N/A | N/A | 956217002 |
| price | 3904391 | 26.8386 | N/A | 2.39 | N/A | N/A | N/A | 149.99 |
| sales_channel_id | 3904391 | 1.653 | N/A | 1 | N/A | N/A | N/A | 2 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `0c4695d2766b226a58432f360bbc4aa40723bc554f886bdf95a39ae0440568bc`: 3 occurrences
  - `79860794c33f57ca07d0725bce4b3e6d1c0a5f8ea5ae0693d1b9502b67d34a3b`: 4 occurrences
  - `15649093cd2a4301c9c5fe9508e0c0766c332f1e20c1929102f0c57994ebb030`: 4 occurrences
  - `2768cbae0516e944af858c4c485a237b5cffddad911d0eda5508e0cd1167d8a5`: 7 occurrences
  - `c34e1baedbc3e9240fa18490ffe0c727daca59917f07d0d1c30de5ca160276ea`: 10 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 343.96 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 14.8941 |
| customer_id | 238.3051 |
| article_id | 29.7881 |
| price | 29.7881 |
| sales_channel_id | 29.7881 |
| price_outlier_capped | 0.4655 |
| sales_channel_corrected | 0.4655 |
| price_percentile_calibrated | 0.4655 |

## 💡 Data Quality Recommendations
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** sales_channel_id, price_outlier_capped - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*