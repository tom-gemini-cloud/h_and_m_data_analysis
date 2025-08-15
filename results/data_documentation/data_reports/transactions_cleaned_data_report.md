# Data Understanding Report
**Generated on:** 2025-08-15 11:53:22
**File:** transactions_cleaned.parquet

## 📄 File Information
- **File Path:** `data\cleaned\transactions_cleaned.parquet`
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
  - `07e20248d6d430dc9643ee43e644723cfb27b7eb62fc3bb60140f352fc40a5e7`: 1 occurrences
  - `37e4da73fd00c0185fe98326388cbb8c667540ecc86389bb952eac36b99a7ebe`: 3 occurrences
  - `3fd29ca941b309c8a17b43fb0d323d453e35868a3400e9d7e4cdd11194cac72e`: 27 occurrences
  - `ac66c147be9ce24c772a3a28a61b58c1e816e414336876aeb41e2643eca17495`: 31 occurrences
  - `f7a17647d72f244c242bc982aadce5a800e94e25ce9c2b624d0c6a1d0efe20a7`: 11 occurrences

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