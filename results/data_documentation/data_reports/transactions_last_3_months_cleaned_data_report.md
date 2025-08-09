# Data Understanding Report
**Generated on:** 2025-08-09 14:55:08
**File:** transactions_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\transactions_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 53.69 MB
- **Last Modified:** 2025-08-09 14:55:01

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
  - `fa40c29f7d027ac5b389eab2eb44cc06066584d62e67b8660138512a304d1956`: 1 occurrences
  - `6724813e1297ef5301ecb500a0bac41ed2bff078877cc3169774dbf5919d3e62`: 2 occurrences
  - `4e241d5aa4a004adc82c8bac0664179f49d0b62304950e32a0101853d7706249`: 7 occurrences
  - `9b901dd1e49f5775d4327a599a99f88d21efcddd59a5afa22f32867a8c73fd25`: 6 occurrences
  - `dcb8c25a473c44cdaa54b50d60dca42cbec4d9ab5b017c8c92d93243c6f9232a`: 3 occurrences

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