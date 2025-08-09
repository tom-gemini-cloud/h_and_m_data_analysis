# Data Understanding Report
**Generated on:** 2025-08-09 11:24:36
**File:** transactions_last_3_months.parquet

## 📄 File Information
- **File Path:** `..\data\processed\transactions_last_3_months.parquet`
- **File Type:** PARQUET
- **File Size:** 52.83 MB
- **Last Modified:** 2025-08-09 11:18:04

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
  - `dd09bb5f8bb45148ec3782d285c9ee529fac6f716d2b5fc49c347a29bf5d16b0`: 1 occurrences
  - `2fc8bd6e99b38abab0738e562e5cd39fc178ac7ad61b88a2af3535d08f787333`: 9 occurrences
  - `47404ea70bede3acf49f92c79155108c069e1b555f6f16ccb754f1daa10a95ca`: 7 occurrences
  - `e513d2e65838bd77daa1ddf1032522f369189195507e705d80b9927d018ce3e8`: 3 occurrences
  - `5a77b64a0b103ce1ba742d5a62345b7c28e4e8bbd88d46a6dbe26c6fc278ec16`: 28 occurrences

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