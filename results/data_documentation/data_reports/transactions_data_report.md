# Data Understanding Report
**Generated on:** 2025-08-14 20:28:23
**File:** transactions_train.csv
**Note:** Analysis based on sample of 200,000 records

## 📄 File Information
- **File Path:** `data\raw\transactions_train.csv`
- **File Type:** CSV
- **File Size:** 3326.42 MB
- **Last Modified:** 2022-01-17 22:14:08

## 📊 Dataset Overview
- **Rows:** 200,000
- **Columns:** 5
- **Total Cells:** 1,000,000

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 19,741 (9.87%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | String | 0 | 0.0% | 5 | 0.0% |
| customer_id | String | 0 | 0.0% | 51,527 | 25.76% |
| article_id | Int64 | 0 | 0.0% | 19,519 | 9.76% |
| price | Float64 | 0 | 0.0% | 1,677 | 0.84% |
| sales_channel_id | Int64 | 0 | 0.0% | 2 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| price | 200000 | 0.03 | N/A | 0.0007966101694915254 | N/A | N/A | N/A | 0.5915254237288136 |

## 📝 Categorical Column Analysis
### t_dat
- **Unique Values:** 5
- **Average Length:** 10.0 characters
- **Top Values:**
  - `2018-09-21`: 47,543 occurrences
  - `2018-09-22`: 17,635 occurrences
  - `2018-09-24`: 34,193 occurrences
  - `2018-09-20`: 48,399 occurrences
  - `2018-09-23`: 52,230 occurrences

### customer_id
- **Unique Values:** 51,527
- **Average Length:** 64.0 characters
- **Top Values:**
  - `d5fd4ecb882b5202e4950ecdaa3b02d5429b366e15255671bcd695ba9e2ee650`: 2 occurrences
  - `a4c9c34ba04ea176b19e3c86d02235cc2d36282b03da68d662fb62ef7c348351`: 1 occurrences
  - `b26bbbdccd102b5cabee4553924b3d0cb67977a1f9a9a1fea6229df908956fe7`: 2 occurrences
  - `13f7018e923aa0349e55fa4512e645b1e686eddf041369384a94f2c7a668e785`: 6 occurrences
  - `31c378258e43eabca454f1dc33b49efffac3d0792b9c42023e73155b33f7002a`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 18.69 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 1.9073 |
| customer_id | 12.207 |
| article_id | 1.5259 |
| price | 1.5259 |
| sales_channel_id | 1.5259 |

## 💡 Data Quality Recommendations
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** t_dat, sales_channel_id - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*