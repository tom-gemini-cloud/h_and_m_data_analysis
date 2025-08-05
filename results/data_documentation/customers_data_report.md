# Data Understanding Report
**Generated on:** 2025-08-05 15:18:34
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
  - `30e5319264c2e4bdc93888d54ef436599cf60155f07f2a06c1c75db9f31a4871`: 1 occurrences
  - `03ff168e0e58f0a5f709e22e56fe0fda62c09457293a995f971ecb6ed3092724`: 1 occurrences
  - `d2d656b50033816c31e19f3bbd4ae5dc0a742e70d328d5a35c312fc899cb44ee`: 1 occurrences
  - `5c29aead4525e980d4ec6f12e3b495a1462d2b9e040b8ecdfdf65e8080da7de2`: 1 occurrences
  - `84da4dfd17274c42a0160c37b4a40e40c3a9a07b81959d578a863c38a6f1b960`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Average Length:** 6.27 characters
- **Top Values:**
  - `PRE-CREATE`: 92,960 occurrences
  - `ACTIVE`: 1,272,491 occurrences
  - `LEFT CLUB`: 467 occurrences
  - `None`: 6,062 occurrences

### fashion_news_frequency
- **Unique Values:** 5
- **Average Length:** 5.76 characters
- **Top Values:**
  - `None`: 16,009 occurrences
  - `Regularly`: 477,416 occurrences
  - `None`: 2 occurrences
  - `NONE`: 877,711 occurrences
  - `Monthly`: 842 occurrences

### postal_code
- **Unique Values:** 352,899
- **Average Length:** 64.0 characters
- **Top Values:**
  - `853f5013da4a15a3343dec33977682e0e414d3024940ae10efa972c01e284a2a`: 3 occurrences
  - `3c03ce31c44a44507368243e2bd4c1882c87b6c742a618c0cc39b96eb0dad514`: 9 occurrences
  - `245a0066011e4ed8682e47b6a85358358f20897c0bf6a8ac7b0d4478afcefbfb`: 1 occurrences
  - `c3440b83c00c5f92e5bd089b10723fec552bbb93445480ea7f1de47d9ed54f7a`: 7 occurrences
  - `87da887e3c2f248ce49feb76f9454dc8f3414485194934c569f3bb7f251178cb`: 3 occurrences

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