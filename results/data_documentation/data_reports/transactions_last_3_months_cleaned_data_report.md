# Data Understanding Report
**Generated on:** 2025-08-09 15:00:02
**File:** transactions_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\transactions_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 53.69 MB
- **Last Modified:** 2025-08-09 14:59:54

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
  - `c2288ee31451147c3caf7eac259283eeb0585794661977793215c39e0a88c2f3`: 1 occurrences
  - `a60ff8145bb31f5408d4f00d7b7612d7125dc82300eb0e00769e040774277058`: 5 occurrences
  - `6d30b13c64d0f80e38ed78769e4efba0dd13120312539decd2ebbaf06e203e9b`: 9 occurrences
  - `43615f6f68c2f339ebb0cdd4d94cca82c5b70b1b3e13e099a8b960618595f665`: 1 occurrences
  - `a07cb5c4096fd4b78ef2d554ea5cffe2782f7e820541164b136d0229e681512d`: 3 occurrences

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