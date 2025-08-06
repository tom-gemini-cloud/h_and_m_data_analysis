# Data Understanding Report
**Generated on:** 2025-08-06 13:47:22
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
  - `50f4713d609cad682a67dcc61aa07dccef64a6d6356897e965a89669f644332d`: 1 occurrences
  - `edc289546ac7eb31043cad21e67ae8c04ca605eee5108d09051bffc6dfa080ee`: 1 occurrences
  - `3841c97a8c78eb9db47274f682104794864010ac2b39c3df3f541f52a13290c7`: 1 occurrences
  - `923d170dcbf526c9e94b3310dc543aa116705bbcb540162a708f512d7bab90b3`: 1 occurrences
  - `2f0591d62d7d4c3a5908ef63fdb744ac18ec6d2ae06b92f05c2b247aa323f064`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Average Length:** 6.08 characters
- **Top Values:**
  - `None`: 745 occurrences
  - `ACTIVE`: 513,558 occurrences
  - `LEFT CLUB`: 65 occurrences
  - `PRE-CREATE`: 10,707 occurrences

### fashion_news_frequency
- **Unique Values:** 4
- **Average Length:** 6.11 characters
- **Top Values:**
  - `Monthly`: 165 occurrences
  - `NONE`: 301,797 occurrences
  - `Regularly`: 221,089 occurrences
  - `None`: 2,024 occurrences

### postal_code
- **Unique Values:** 246,741
- **Average Length:** 64.0 characters
- **Top Values:**
  - `e9f109175452cb8057124fa2576ba5b4dc4cc43cb4b6ff7882387d54af4beb21`: 2 occurrences
  - `6c0a05f4e0aa4bcb37cec38782a47d808a9fd2d05ef968f1bc26b87d792ffe76`: 1 occurrences
  - `81a1f27dbc73292a0739967580271d73ce5ea8b9d38058391f1547c1266f62f1`: 1 occurrences
  - `8a98be5ce9d80eb4c02a432aeb04806455e840377d0f30596a85ff9a869a0d0d`: 2 occurrences
  - `717c182043c9f3aa1b6b991845ae82b5cde3bb40891f779cf9f104a7a23af126`: 2 occurrences

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