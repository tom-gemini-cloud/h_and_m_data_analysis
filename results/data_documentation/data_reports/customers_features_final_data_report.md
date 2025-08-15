# Data Understanding Report
**Generated on:** 2025-08-15 10:36:07
**File:** customers_features_final.parquet
**Note:** Analysis based on sample of 50,000 records

## 📄 File Information
- **File Path:** `../data/features/final/customers_features_final.parquet`
- **File Type:** PARQUET
- **File Size:** 81.96 MB
- **Last Modified:** 2025-08-15 10:36:07

## 📊 Dataset Overview
- **Rows:** 50,000
- **Columns:** 16
- **Total Cells:** 800,000

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| customer_id | String | 0 | 0.0% | 50,000 | 100.0% |
| FN | Float64 | 0 | 0.0% | 2 | 0.0% |
| Active | Float64 | 0 | 0.0% | 2 | 0.0% |
| club_member_status | Categorical | 0 | 0.0% | 4 | 0.01% |
| fashion_news_frequency | Categorical | 0 | 0.0% | 3 | 0.01% |
| age | Float64 | 0 | 0.0% | 72 | 0.14% |
| postal_code | Categorical | 0 | 0.0% | 43,606 | 87.21% |
| recency | Int64 | 0 | 0.0% | 91 | 0.18% |
| frequency | UInt32 | 0 | 0.0% | 126 | 0.25% |
| monetary | Float64 | 0 | 0.0% | 26,050 | 52.1% |
| purchase_diversity_score | Float64 | 0 | 0.0% | 4,313 | 8.63% |
| price_sensitivity_index | Float64 | 0 | 0.0% | 31,061 | 62.12% |
| colour_preference_entropy | Float64 | 0 | 0.0% | 4,689 | 9.38% |
| style_consistency_score | Float64 | 0 | 0.0% | 5,068 | 10.14% |
| dataset_created_at | String | 0 | 0.0% | 1 | 0.0% |
| created_by | String | 0 | 0.0% | 1 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| FN | 50000 | 0.4206 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| Active | 50000 | 0.4131 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| age | 50000 | 35.0329 | N/A | 16.0 | N/A | N/A | N/A | 92.0 |
| recency | 50000 | 38.2717 | N/A | 1 | N/A | N/A | N/A | 91 |
| monetary | 50000 | 204.6296 | N/A | 2.39 | N/A | N/A | N/A | 10500.579999999987 |
| purchase_diversity_score | 50000 | 0.9613 | N/A | -0.0 | N/A | N/A | N/A | 3.0945884966423414 |
| price_sensitivity_index | 50000 | 0.4689 | N/A | 0.0 | N/A | N/A | N/A | 2.502406831175997 |
| colour_preference_entropy | 50000 | 1.4587 | N/A | -0.0 | N/A | N/A | N/A | 4.249743855419998 |
| style_consistency_score | 50000 | 0.3288 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 50,000
- **Average Length:** 64.0 characters
- **Top Values:**
  - `8f63eefa9fc3494d2f3f928f844d82bb90ec67228e5f1936130bcc25f3314029`: 1 occurrences
  - `da407fd151ba400c4a862cb288c1bf23dc194657bc5624b734995f188e45b7ef`: 1 occurrences
  - `841debe23f0814c72889f2d06860a0c03b0ba83bdcb8acc0b77a3ceb95f875d6`: 1 occurrences
  - `30bc92b2be8b8bac4ed7e13ed792c81e9f817c4966eba86ac5a8dbf20594318b`: 1 occurrences
  - `19124a9a81b38a6613616530fc8641f022afeb69ad806e93b3ac377d57788d54`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `PRE-CREATE`: 1,032 occurrences
  - `NONE`: 71 occurrences
  - `ACTIVE`: 48,891 occurrences
  - `LEFT CLUB`: 6 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `NONE`: 28,921 occurrences
  - `Regularly`: 21,065 occurrences
  - `Monthly`: 14 occurrences

### postal_code
- **Unique Values:** 43,606
- **Top Values:**
  - `3fd2eda3b3f66968326c67880a29ab535292bcf0e0936bfb600578a2e00da574`: 1 occurrences
  - `b5abadfee071957e251067b7107cd53fca8550c6e3eab4756a2f7682fec05e33`: 1 occurrences
  - `6538541e5bd329c67e6760ecc086fc67f888e799d57f6b314ee4f3989c03fc89`: 1 occurrences
  - `b4f4a1cf68d98daebc3351c17c761c0f71847bf88d54845c8ffcb88ffaa5c666`: 1 occurrences
  - `0075c1895df52a4aa06d72e904f18bac2fa36277d55855dc28ab3576412122cf`: 1 occurrences

### dataset_created_at
- **Unique Values:** 1
- **Average Length:** 26.0 characters
- **Top Values:**
  - `2025-08-15T10:36:06.677491`: 50,000 occurrences

### created_by
- **Unique Values:** 1
- **Average Length:** 34.0 characters
- **Top Values:**
  - `customer_feature_engineering.ipynb`: 50,000 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 10.11 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 3.0518 |
| FN | 0.3815 |
| Active | 0.3815 |
| club_member_status | 0.1907 |
| fashion_news_frequency | 0.1907 |
| age | 0.3815 |
| postal_code | 0.1907 |
| recency | 0.3815 |
| frequency | 0.1907 |
| monetary | 0.3815 |
| purchase_diversity_score | 0.3815 |
| price_sensitivity_index | 0.3815 |
| colour_preference_entropy | 0.3815 |
| style_consistency_score | 0.3815 |
| dataset_created_at | 1.2398 |
| created_by | 1.6212 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** FN, Active, club_member_status, fashion_news_frequency - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*