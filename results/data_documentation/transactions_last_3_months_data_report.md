# Data Understanding Report
**Generated on:** 2025-08-05 15:19:47
**File:** transactions_last_3_months.csv

## 📄 File Information
- **File Path:** `..\data\processed\transactions_last_3_months.csv`
- **File Type:** CSV
- **File Size:** 405.02 MB
- **Last Modified:** 2025-08-05 13:24:05

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
| t_dat | String | 0 | 0.0% | 91 | 0.0% |
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
### t_dat
- **Unique Values:** 91
- **Average Length:** 10.0 characters
- **Top Values:**
  - `2020-09-01`: 38,060 occurrences
  - `2020-09-21`: 32,130 occurrences
  - `2020-07-04`: 46,408 occurrences
  - `2020-09-08`: 36,415 occurrences
  - `2020-08-28`: 39,546 occurrences

### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `e8be97af1301a1bdcda9d554c6f3c7259c6d3ab2c902c81239ab4910a2d0b6fb`: 2 occurrences
  - `dd7cde075ac488534e5e834ac163cacdc949a232c40fc14da5c002aca95c8cc0`: 2 occurrences
  - `952c16e5653973942b3d29b805ee68adaba5ad4f8006b052a7283301733acc64`: 4 occurrences
  - `546ded77ba74020f3e565becdd5b953be61442d36a0eceb687261717fa88fc04`: 22 occurrences
  - `24ae6de3a284047ac6a7815627feab468ae5c3c50d947ff92aa3576a07a7545b`: 2 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 364.9 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 37.2352 |
| customer_id | 238.3051 |
| article_id | 29.7881 |
| price | 29.7881 |
| sales_channel_id | 29.7881 |

## 💡 Data Quality Recommendations
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** sales_channel_id - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*