# Data Understanding Report
**Generated on:** 2025-08-14 20:33:53
**File:** transactions_train.csv

## 📄 File Information
- **File Path:** `data\raw\transactions_train.csv`
- **File Type:** CSV
- **File Size:** 3326.42 MB
- **Last Modified:** 2022-01-17 22:14:08

## 📊 Dataset Overview
- **Rows:** 31,788,324
- **Columns:** 5
- **Total Cells:** 158,941,620

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 2,974,905 (9.36%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | String | 0 | 0.0% | 734 | 0.0% |
| customer_id | String | 0 | 0.0% | 1,362,281 | 4.29% |
| article_id | Int64 | 0 | 0.0% | 104,547 | 0.33% |
| price | Float64 | 0 | 0.0% | 9,857 | 0.03% |
| sales_channel_id | Int64 | 0 | 0.0% | 2 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| price | 31788324 | 0.0278 | N/A | 1.694915254237288e-05 | N/A | N/A | N/A | 0.5915254237288136 |

## 📝 Categorical Column Analysis
### t_dat
- **Unique Values:** 734
- **Average Length:** 10.0 characters
- **Top Values:**
  - `2020-04-29`: 36,390 occurrences
  - `2020-05-16`: 41,721 occurrences
  - `2020-07-16`: 45,465 occurrences
  - `2020-09-07`: 37,913 occurrences
  - `2019-02-17`: 33,705 occurrences

### customer_id
- **Unique Values:** 1,362,281
- **Average Length:** 64.0 characters
- **Top Values:**
  - `7f3e7e3122fe81aca787a8e845689b355a63133594e7f87b16cc0461343140f6`: 7 occurrences
  - `cdebe6a50f3af43a9835ffb2471de1f03acf88b7ba6556ecdb6256f0c56c39ac`: 3 occurrences
  - `44aa42fb1408cefbb277cb4df922b2456fa22d9c853672b27e55b336452d62b6`: 58 occurrences
  - `fc3903a5a2701f40faac850a2adb9507495de1a796847d68c727238518850bae`: 11 occurrences
  - `13584d9164938974931df089beb1a76b3afffc75f9d9613ded99a245e026e498`: 13 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 2970.94 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 303.1571 |
| customer_id | 1940.2053 |
| article_id | 242.5257 |
| price | 242.5257 |
| sales_channel_id | 242.5257 |

## 💡 Data Quality Recommendations
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** sales_channel_id - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*