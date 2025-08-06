# Data Understanding Report
**Generated on:** 2025-08-06 13:47:25
**File:** transactions_last_3_months.parquet

## 📄 File Information
- **File Path:** `..\data\processed\transactions_last_3_months.parquet`
- **File Type:** PARQUET
- **File Size:** 52.83 MB
- **Last Modified:** 2025-08-05 13:24:06

## 📊 Dataset Overview
- **Rows:** 3,904,391
- **Columns:** 5
- **Total Cells:** 19,521,955

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 327,155 (8.38%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | Date | 0 | 0.0% | 91 | 0.0% |
| customer_id | String | 0 | 0.0% | 525,075 | 13.45% |
| article_id | Int64 | 0 | 0.0% | 42,298 | 1.08% |
| price | Float64 | 0 | 0.0% | 5,622 | 0.14% |
| sales_channel_id | Int64 | 0 | 0.0% | 2 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| article_id | 3904391 | 791482176.6992 | N/A | 108775015 | N/A | N/A | N/A | 956217002 |
| price | 3904391 | 0.0266 | N/A | 0.00013559322033898305 | N/A | N/A | N/A | 0.5067796610169492 |
| sales_channel_id | 3904391 | 1.653 | N/A | 1 | N/A | N/A | N/A | 2 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `2c77f4f7d2823aacb8545d5cb745ea58650892947282175486bdeb6e6ba0e153`: 11 occurrences
  - `f41e7f5af89f365d06ed46bf5d68733a119f748f237680bb79d5a11880afd7dd`: 11 occurrences
  - `2fdb86688873a2d902489508b9f9eff8aa264c16f81db198e0870840b65e0629`: 3 occurrences
  - `5ebf70a3a7e1e18c199cd54f23d7ae4f6b06fdc61a42c30fc2ab95e4e71b76f2`: 4 occurrences
  - `d5347b0e0a11468707115d12d2174678ed85d2eeab213032e492e5889fc0d921`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 342.56 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 14.8941 |
| customer_id | 238.3051 |
| article_id | 29.7881 |
| price | 29.7881 |
| sales_channel_id | 29.7881 |

## 💡 Data Quality Recommendations
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** sales_channel_id - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*