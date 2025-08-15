# Data Understanding Report
**Generated on:** 2025-08-14 20:31:07
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
  - `2018-09-24`: 34,193 occurrences
  - `2018-09-20`: 48,399 occurrences
  - `2018-09-23`: 52,230 occurrences
  - `2018-09-21`: 47,543 occurrences
  - `2018-09-22`: 17,635 occurrences

### customer_id
- **Unique Values:** 51,527
- **Average Length:** 64.0 characters
- **Top Values:**
  - `22cb9c9540719f63bed43c04af71f39940a592a8599abd37aedd94fbe47dc44a`: 1 occurrences
  - `d88d28d006de45673169141d0b38f2ceda81fd764d289e0f8683ef359612ebb1`: 6 occurrences
  - `d9ed43e250bb7bfdb52dd7195f42791cdcd3db456dd4bb2171a289da4a731b45`: 3 occurrences
  - `2b702fe0e99bc73716d8f68784827dbaa4718628bdc84608beb249967a300ee5`: 2 occurrences
  - `21f5141942826254261cde2933508e035d0f6d7d7bd4bec9b28004ab757166d1`: 3 occurrences

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