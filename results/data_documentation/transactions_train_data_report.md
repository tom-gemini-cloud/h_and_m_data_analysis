# Data Understanding Report
**Generated on:** 2025-08-05 14:23:50
**File:** transactions_train.csv
**Note:** Analysis based on sample of 10,000 records

## 📄 File Information
- **File Path:** `..\data\raw\transactions_train.csv`
- **File Type:** CSV
- **File Size:** 3326.42 MB
- **Last Modified:** 2022-01-17 22:14:08

## 📊 Dataset Overview
- **Rows:** 10,000
- **Columns:** 5
- **Total Cells:** 50,000

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | String | 0 | 0.0% | 734 | 7.34% |
| customer_id | String | 0 | 0.0% | 9,873 | 98.73% |
| article_id | Int64 | 0 | 0.0% | 7,817 | 78.17% |
| price | Float64 | 0 | 0.0% | 1,071 | 10.71% |
| sales_channel_id | Int64 | 0 | 0.0% | 2 | 0.02% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| article_id | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| price | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| sales_channel_id | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

## 📝 Categorical Column Analysis
### t_dat
- **Unique Values:** 734
- **Average Length:** 10.0 characters
- **Top Values:**
  - `2019-01-21`: 9 occurrences
  - `2020-07-04`: 15 occurrences
  - `2019-08-16`: 15 occurrences
  - `2019-08-26`: 14 occurrences
  - `2020-06-29`: 16 occurrences

### customer_id
- **Unique Values:** 9,873
- **Average Length:** 64.0 characters
- **Top Values:**
  - `7d9ebb98c6e63965b4d6060d808eba4a06fe1c5d5bc8dc62c8a6af7362291583`: 1 occurrences
  - `b8129f353e8cfa4610c803994b9d675655bf7697bb6ed136c84bd173092d16b6`: 1 occurrences
  - `10411ac70c80005a535783ede440e0de5df6a1d7ff25fde5f58ac00ca97d8e55`: 1 occurrences
  - `8080cb7a75d9b4aee609e498d22000c4f5e343e955123e70720757fbca8bedbf`: 1 occurrences
  - `5384b5e03b2c67670580dbe4338d00ef4d02337c9ce8fd5fef95c9b5dc1ea6bd`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 0.93 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 0.0954 |
| customer_id | 0.6104 |
| article_id | 0.0763 |
| price | 0.0763 |
| sales_channel_id | 0.0763 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** sales_channel_id - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*