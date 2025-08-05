# Data Understanding Report
**Generated on:** 2025-08-05 15:19:41
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
  - `2019-09-06`: 38,762 occurrences
  - `2019-01-22`: 36,878 occurrences
  - `2019-03-07`: 44,575 occurrences
  - `2019-02-03`: 45,259 occurrences
  - `2019-10-08`: 37,840 occurrences

### customer_id
- **Unique Values:** 1,362,281
- **Average Length:** 64.0 characters
- **Top Values:**
  - `accf866263abe85a4dbe7e15ff60e00631ef6782512b9ba7e7305d16071166bc`: 18 occurrences
  - `32239b7324a9215ba5fe6b84c73c4d094e8fb3d748d00d1acd6a17ca73246060`: 1 occurrences
  - `3a9dc3761f618f1efa30c13ffd35c316ce47ab2d07c02385e1712cacb6a0a135`: 1 occurrences
  - `efe2ca69575ff7db3249a058169108b98c7d6546133c220bfd5ff13433df7ff2`: 3 occurrences
  - `4f877e1f3769cb78010923f8e95a0e4ad48fd694faccb60d3514b8ef401710c1`: 86 occurrences

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