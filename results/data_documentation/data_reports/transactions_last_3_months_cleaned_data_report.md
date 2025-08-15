# Data Understanding Report
**Generated on:** 2025-08-12 10:58:47
**File:** transactions_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\transactions_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 53.69 MB
- **Last Modified:** 2025-08-12 10:58:40

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
| price | 3904391 | 26.8386 | N/A | 2.39 | N/A | N/A | N/A | 149.99 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `600d974a4d01a742d3329ed2b10af946ff414b10750f131252eca5b7c573fb84`: 1 occurrences
  - `b13394d440978f5e17e8d69f94764d1ca6c2f6d723b661042cfebbf5ce236726`: 8 occurrences
  - `babd128fd5791c8fbc12cf51549d31e4f0dd376c90778a9a7ed8fa857c4cb611`: 8 occurrences
  - `f495ffe5cf8d0873b058c02ea7eb87f366055a018d815a967dbcaca38fa5e543`: 3 occurrences
  - `e4966190604178d97bad9eaa1aaa419cfb863145e24d311932c23bfc4347e77a`: 4 occurrences

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