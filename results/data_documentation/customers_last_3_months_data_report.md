# Data Understanding Report
**Generated on:** 2025-08-05 14:28:30
**File:** customers_last_3_months.parquet

## 📄 File Information
- **File Path:** `data\processed\customers_last_3_months.parquet`
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
| FN | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Active | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| age | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `0a5a9438171930351d57348cc68d9f00193bbb221de851e6b207c999f8b31fab`: 1 occurrences
  - `3c6631e7161ffc984e6fa9eba80ca8c8f70d4da740caf4470b2601b6c87366e9`: 1 occurrences
  - `1dbb0603d74b4d181bd213432ca660dea5ef638711fcf006d4e9db51b1cef840`: 1 occurrences
  - `4048164699c2e564a603334a5761f53c5a010e53459b892fa0c29998e1b04480`: 1 occurrences
  - `35be01d11ee76d27685a06a46ee6c9c98ccd0218f9d234121fcd3a204320a576`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Average Length:** 6.08 characters
- **Top Values:**
  - `None`: 745 occurrences
  - `PRE-CREATE`: 10,707 occurrences
  - `LEFT CLUB`: 65 occurrences
  - `ACTIVE`: 513,558 occurrences

### fashion_news_frequency
- **Unique Values:** 4
- **Average Length:** 6.11 characters
- **Top Values:**
  - `None`: 2,024 occurrences
  - `Regularly`: 221,089 occurrences
  - `NONE`: 301,797 occurrences
  - `Monthly`: 165 occurrences

### postal_code
- **Unique Values:** 246,741
- **Average Length:** 64.0 characters
- **Top Values:**
  - `33b06b036fe46559c9fa47273c57919fca18139aff5949da3aa1eb4a8dbe0326`: 5 occurrences
  - `b14f34d69261b568d867f127121337c63711af3fc9105b1ea53d8124e5a507c2`: 4 occurrences
  - `a191b0a8e448c8ca4f0c663fc6c48ff839e437a3aa30a9edd4dc2c34ce6c3feb`: 3 occurrences
  - `15c89f529956a05ebaf6b43bf4e412b4c41280ff25b8e40a35f2c73e0fc23bef`: 4 occurrences
  - `849ac0c73165bb4c3f51d34fde5f32473fa191a846dc7e9447144304b616f450`: 2 occurrences

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