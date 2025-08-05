# Data Understanding Report
**Generated on:** 2025-08-05 15:29:56
**File:** transactions_train.csv

## 📄 File Information
- **File Path:** `..\data\raw\transactions_train.csv`
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
| article_id | 31788324 | 696227219.1338 | N/A | 108775015 | N/A | N/A | N/A | 956217002 |
| price | 31788324 | 0.0278 | N/A | 1.694915254237288e-05 | N/A | N/A | N/A | 0.5915254237288136 |
| sales_channel_id | 31788324 | 1.704 | N/A | 1 | N/A | N/A | N/A | 2 |

## 📝 Categorical Column Analysis
### t_dat
- **Unique Values:** 734
- **Average Length:** 10.0 characters
- **Top Values:**
  - `2019-04-20`: 55,558 occurrences
  - `2020-02-02`: 31,387 occurrences
  - `2019-12-14`: 32,329 occurrences
  - `2020-04-21`: 30,862 occurrences
  - `2019-09-02`: 33,078 occurrences

### customer_id
- **Unique Values:** 1,362,281
- **Average Length:** 64.0 characters
- **Top Values:**
  - `671bd8c4b63812bb2ee58a782d8229604c0b89908304c3bbceb1d2337062dda5`: 4 occurrences
  - `d56eb02e60f33e093f06ad72cf70a35995a3324ee5277af2856dc7c901802d3e`: 5 occurrences
  - `20ef28241bf2323bfa53abe85be41b5f461afd6f09b4480eb6501f9432b9cda4`: 89 occurrences
  - `6564c1ba88c6b456933805b4cd1cacd29bd94ba841a2c6371b380661911ade54`: 4 occurrences
  - `4ab8207b174baec7ad438d067b82fbf215793903e183246b4c2d8a98d1266a70`: 2 occurrences

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