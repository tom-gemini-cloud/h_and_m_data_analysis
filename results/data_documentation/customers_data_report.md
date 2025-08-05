# Data Understanding Report
**Generated on:** 2025-08-05 15:28:41
**File:** customers.csv

## 📄 File Information
- **File Path:** `..\data\raw\customers.csv`
- **File Type:** CSV
- **File Size:** 197.54 MB
- **Last Modified:** 2022-01-17 21:12:24

## 📊 Dataset Overview
- **Rows:** 1,371,980
- **Columns:** 7
- **Total Cells:** 9,603,860

## 🔍 Data Quality Summary
- **Completeness Score:** 80.84%
- **Missing Values:** 1,840,558 (19.16%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| customer_id | String | 0 | 0.0% | 1,371,980 | 100.0% |
| FN | Float64 | 895,050 | 65.24% | 2 | 0.0% |
| Active | Float64 | 907,576 | 66.15% | 2 | 0.0% |
| club_member_status | String | 6,062 | 0.44% | 4 | 0.0% |
| fashion_news_frequency | String | 16,009 | 1.17% | 5 | 0.0% |
| age | Int64 | 15,861 | 1.16% | 85 | 0.01% |
| postal_code | String | 0 | 0.0% | 352,899 | 25.72% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| FN | 476930 | 1.0 | N/A | 1.0 | N/A | N/A | N/A | 1.0 |
| Active | 464404 | 1.0 | N/A | 1.0 | N/A | N/A | N/A | 1.0 |
| age | 1356119 | 36.387 | N/A | 16 | N/A | N/A | N/A | 99 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 1,371,980
- **Average Length:** 64.0 characters
- **Top Values:**
  - `a98cc371cdd4620875ed61c47934c6b47db41f4d40616f4953e1e2d512583ea9`: 1 occurrences
  - `a1e2070cc164a96c7c70d6c4535254fc3652f9c395004d9d2d26e0a564116c99`: 1 occurrences
  - `f966ad6b1fbe050187c49e2ef5c2eb240f9e02828304b9bf23b8a0a618e7eb57`: 1 occurrences
  - `93294b34cb74dbce19f503d2aecdf9db4e6c633e1c620991a580570b93fe7deb`: 1 occurrences
  - `e3fcd0c63af94d0324939c7b3b31f6b121d1dbd254917cc3a60c9326347e54df`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Average Length:** 6.27 characters
- **Top Values:**
  - `LEFT CLUB`: 467 occurrences
  - `ACTIVE`: 1,272,491 occurrences
  - `PRE-CREATE`: 92,960 occurrences
  - `None`: 6,062 occurrences

### fashion_news_frequency
- **Unique Values:** 5
- **Average Length:** 5.76 characters
- **Top Values:**
  - `None`: 16,009 occurrences
  - `Regularly`: 477,416 occurrences
  - `NONE`: 877,711 occurrences
  - `Monthly`: 842 occurrences
  - `None`: 2 occurrences

### postal_code
- **Unique Values:** 352,899
- **Average Length:** 64.0 characters
- **Top Values:**
  - `1d0fc42ff7299c4cf1a3c4c80b69b09bb0147d12e5f92cc3abdc315470169622`: 1 occurrences
  - `e01dc2f24d5d74305a15852d67a2db9eecc32f1b6084122ac24063b5106f3e72`: 2 occurrences
  - `05e4e2c30afb474c4212af8357345d42dd16c6c56fdde67f3e541f9a399e2590`: 4 occurrences
  - `b02f80f4328883258f61f3c7ea765c98c5a3b57ff4ba68d00c031c9da645aa98`: 6 occurrences
  - `1f5da2413ac11685fffdea0a2ae2c8deb7a21c98471cbc5922855e5bb1ad215a`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 214.99 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 83.739 |
| FN | 10.631 |
| Active | 10.631 |
| club_member_status | 8.1718 |
| fashion_news_frequency | 7.4515 |
| age | 10.631 |
| postal_code | 83.739 |

## 💡 Data Quality Recommendations
- **High missing values detected** - Consider imputation strategies or investigate data collection issues
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** FN, Active, club_member_status, fashion_news_frequency - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*