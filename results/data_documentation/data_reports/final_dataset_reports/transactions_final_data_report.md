# Data Understanding Report
**Generated on:** 2025-08-20 11:03:02
**File:** transactions_final.parquet

## 📄 File Information
- **File Path:** `data/modelling_data/transactions_final.parquet`
- **File Type:** PARQUET
- **File Size:** 53.52 MB
- **Last Modified:** 2025-08-20 10:59:51

## 📊 Dataset Overview
- **Rows:** 3,904,391
- **Columns:** 5
- **Total Cells:** 19,521,955

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

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| price | 3904391 | 26.8386 | N/A | 2.39 | N/A | N/A | N/A | 149.99 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `3b5ce6e82acc38e85f037391ce227802788207e5ae90b20a0daa7e99a02552a8`: 6 occurrences
  - `7dccf8ad631ff31c86665fee7146bab577f07fdf17b87b55f6cecde4621ae9b3`: 9 occurrences
  - `b5d861f46d722cec309b37556f188046254f2f2b058266592c71d70d99a40a7f`: 3 occurrences
  - `ce77bcd6f8231514d08f3831247701c2f77b30e8133daded7b4e153543db07b8`: 16 occurrences
  - `436288b8f818d4b2efe0be5458c9a445908051183fd393aaaa1019f129bd5225`: 7 occurrences

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