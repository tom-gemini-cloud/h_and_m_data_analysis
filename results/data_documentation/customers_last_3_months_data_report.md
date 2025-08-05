# Data Understanding Report
**Generated on:** 2025-08-05 15:29:58
**File:** customers_last_3_months.parquet

## 📄 File Information
- **File Path:** `..\data\processed\customers_last_3_months.parquet`
- **File Type:** PARQUET
- **File Size:** 30.0 MB
- **Last Modified:** 2025-08-05 13:24:29

## 📊 Dataset Overview
- **Rows:** 525,075
- **Columns:** 7
- **Total Cells:** 3,675,525

## 🔍 Data Quality Summary
- **Completeness Score:** 83.18%
- **Missing Values:** 618,175 (16.82%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| customer_id | String | 0 | 0.0% | 525,075 | 100.0% |
| FN | Float64 | 304,417 | 57.98% | 2 | 0.0% |
| Active | Float64 | 308,036 | 58.67% | 2 | 0.0% |
| club_member_status | String | 745 | 0.14% | 4 | 0.0% |
| fashion_news_frequency | String | 2,024 | 0.39% | 4 | 0.0% |
| age | Int64 | 2,953 | 0.56% | 84 | 0.02% |
| postal_code | String | 0 | 0.0% | 246,741 | 46.99% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| FN | 220658 | 1.0 | N/A | 1.0 | N/A | N/A | N/A | 1.0 |
| Active | 217039 | 1.0 | N/A | 1.0 | N/A | N/A | N/A | 1.0 |
| age | 522122 | 35.0471 | N/A | 16 | N/A | N/A | N/A | 99 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `08af206b1835ff30691a8d51efffb1ebc46f43c9e905a9b69d3f2c5c764950d5`: 1 occurrences
  - `01d88ba133902647e3d0f99ceda43c83bba303c3667c5b509a054a199ab340f9`: 1 occurrences
  - `883503902aaafdd642df50471bdf34bcd5f301f58991ace72afda102b11c4688`: 1 occurrences
  - `d80ba8b62527322b03cf1e2435bc74211f0052899407cf338c8e770ebacd5547`: 1 occurrences
  - `fcf06a7bc387818e4c7f383776291e1283b7ab43da1c567944523b2ad93ce4ab`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Average Length:** 6.08 characters
- **Top Values:**
  - `LEFT CLUB`: 65 occurrences
  - `ACTIVE`: 513,558 occurrences
  - `PRE-CREATE`: 10,707 occurrences
  - `None`: 745 occurrences

### fashion_news_frequency
- **Unique Values:** 4
- **Average Length:** 6.11 characters
- **Top Values:**
  - `Regularly`: 221,089 occurrences
  - `NONE`: 301,797 occurrences
  - `Monthly`: 165 occurrences
  - `None`: 2,024 occurrences

### postal_code
- **Unique Values:** 246,741
- **Average Length:** 64.0 characters
- **Top Values:**
  - `76ce153b8fcb32ab09f7b1d2eeb53dea441810f52b98b9cbd9a59a33375c59d2`: 2 occurrences
  - `a671c4d610c78ebee9422283ffcb9b09bf5437372bbcd18eaa52fef3b71fe1af`: 2 occurrences
  - `65e46f3cdfb76910afbadcfadf1875328b4597c87b56b3562b66e8ab3b69edd0`: 1 occurrences
  - `2973abc54daa8a5f8ccfe9362140c63247c5eee03f1d93f4c830291c32bc3057`: 1 occurrences
  - `1c3318c269a6f343f2a4f950a4c40266cbc94fad7b4511e26a3a529b9dcb5c9a`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 82.41 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 32.048 |
| FN | 4.0686 |
| Active | 4.0686 |
| club_member_status | 3.0455 |
| fashion_news_frequency | 3.0618 |
| age | 4.0686 |
| postal_code | 32.048 |

## 💡 Data Quality Recommendations
- **High missing values detected** - Consider imputation strategies or investigate data collection issues
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** FN, Active, club_member_status, fashion_news_frequency - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*