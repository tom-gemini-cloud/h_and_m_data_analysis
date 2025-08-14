# Data Understanding Report
**Generated on:** 2025-08-14 12:11:41
**File:** customers_features_final.parquet
**Note:** Analysis based on sample of 50,000 records

## 📄 File Information
- **File Path:** `..\data\features\final\customers_features_final.parquet`
- **File Type:** PARQUET
- **File Size:** 81.98 MB
- **Last Modified:** 2025-08-14 12:11:41

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
| age | Float64 | 0 | 0.0% | 73 | 0.15% |
| postal_code | Categorical | 0 | 0.0% | 43,603 | 87.21% |
| recency | Int64 | 0 | 0.0% | 91 | 0.18% |
| frequency | UInt32 | 0 | 0.0% | 120 | 0.24% |
| monetary | Float64 | 0 | 0.0% | 25,799 | 51.6% |
| purchase_diversity_score | Float64 | 0 | 0.0% | 4,240 | 8.48% |
| price_sensitivity_index | Float64 | 0 | 0.0% | 30,840 | 61.68% |
| colour_preference_entropy | Float64 | 0 | 0.0% | 4,594 | 9.19% |
| style_consistency_score | Float64 | 0 | 0.0% | 4,893 | 9.79% |
| dataset_created_at | String | 0 | 0.0% | 1 | 0.0% |
| created_by | String | 0 | 0.0% | 1 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| FN | 50000 | 0.4184 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| Active | 50000 | 0.4124 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| age | 50000 | 35.052 | N/A | 16.0 | N/A | N/A | N/A | 95.0 |
| recency | 50000 | 38.5158 | N/A | 1 | N/A | N/A | N/A | 91 |
| monetary | 50000 | 201.2076 | N/A | 2.39 | N/A | N/A | N/A | 7359.5599999999895 |
| purchase_diversity_score | 50000 | 0.9537 | N/A | -0.0 | N/A | N/A | N/A | 2.9394795182511317 |
| price_sensitivity_index | 50000 | 0.4668 | N/A | 0.0 | N/A | N/A | N/A | 2.502406831175997 |
| colour_preference_entropy | 50000 | 1.4452 | N/A | -0.0 | N/A | N/A | N/A | 4.3604286775872385 |
| style_consistency_score | 50000 | 0.332 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 50,000
- **Average Length:** 64.0 characters
- **Top Values:**
  - `b10fe321b14fa7190de6c9255936111443fa1d43ee8b4d663a22e70ec51c1a5e`: 1 occurrences
  - `0d8e2f3bf675e853eaded44267b50b94db081665a4d2cea784fc92c551a9b652`: 1 occurrences
  - `980bc296cd74bbd100741b11abf1d474eb858c51e3dc1e7f1fea8c1335ad7cf0`: 1 occurrences
  - `3bdec4f8787a9ee8805146e33229e5d12c08787718fc3607f5851ce0e7bd3b91`: 1 occurrences
  - `a1b2e2bba03249efbc68644adfa19ec322aaadc3ed3b7103f0bf01d304849c5c`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `PRE-CREATE`: 1,031 occurrences
  - `NONE`: 67 occurrences
  - `ACTIVE`: 48,895 occurrences
  - `LEFT CLUB`: 7 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `Regularly`: 20,975 occurrences
  - `Monthly`: 12 occurrences
  - `NONE`: 29,013 occurrences

### postal_code
- **Unique Values:** 43,603
- **Top Values:**
  - `313be0957c4b4d16cff29b3a06340014cc123113d156e4e1ec545102ac1ea184`: 1 occurrences
  - `2efd7249f292d89bdc248d29e87c4357f31b07b91e10edb45b946e06e6ca2d01`: 1 occurrences
  - `bc4be0c75909d56bc3c45cc020f72e816c09a8dd6fe73602c0910abfae71ee4e`: 1 occurrences
  - `d915f97611002a65ce45762f2b934916a22b967c7661c6f10b49eb300d0d2d04`: 1 occurrences
  - `c22dd5e6cc124b23faa826ac50f675c516e442f6cc0569a95bf190baa599dfa1`: 1 occurrences

### dataset_created_at
- **Unique Values:** 1
- **Average Length:** 26.0 characters
- **Top Values:**
  - `2025-08-14T12:11:39.236351`: 50,000 occurrences

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