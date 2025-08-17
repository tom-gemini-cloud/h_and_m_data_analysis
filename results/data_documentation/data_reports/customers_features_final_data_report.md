# Data Understanding Report
**Generated on:** 2025-08-16 09:44:26
**File:** customers_features_final.parquet
**Note:** Analysis based on sample of 50,000 records

## 📄 File Information
- **File Path:** `../data/features/final/customers_features_final.parquet`
- **File Type:** PARQUET
- **File Size:** 81.92 MB
- **Last Modified:** 2025-08-16 09:44:25

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
| purchase_diversity_score | Float64 | 0 | 0.0% | 4,283 | 8.57% |
| price_sensitivity_index | Float64 | 0 | 0.0% | 31,061 | 62.12% |
| colour_preference_entropy | Float64 | 0 | 0.0% | 4,722 | 9.44% |
| style_consistency_score | Float64 | 0 | 0.0% | 5,072 | 10.14% |
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
| purchase_diversity_score | 50000 | 0.9613 | N/A | 0.0 | N/A | N/A | N/A | 3.094588496642342 |
| price_sensitivity_index | 50000 | 0.4689 | N/A | 0.0 | N/A | N/A | N/A | 2.502406831175997 |
| colour_preference_entropy | 50000 | 1.4587 | N/A | 0.0 | N/A | N/A | N/A | 4.2497438554199976 |
| style_consistency_score | 50000 | 0.3288 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 50,000
- **Average Length:** 64.0 characters
- **Top Values:**
  - `4017d21726158975c550acdad2957bbb5450e3421e77cde7bfe419c3cd32b793`: 1 occurrences
  - `332dd3f90e5d6280d46223d2956ac1b7896f9817b5678f327b4d76f61aca0a7c`: 1 occurrences
  - `a4890af0f2e898f07a5ad328571a4f2a85caca8b124888adb92891d9b4689169`: 1 occurrences
  - `1f8b8bd935cdda11ecc0c1697e92f38ec343f3355ed73502832c44bcad661f40`: 1 occurrences
  - `79fcce86e225b33da80150476edd9da9b14d56b3b1f0bae17c7cdabf57bd1f6d`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `LEFT CLUB`: 6 occurrences
  - `PRE-CREATE`: 1,032 occurrences
  - `ACTIVE`: 48,891 occurrences
  - `NONE`: 71 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `Monthly`: 14 occurrences
  - `Regularly`: 21,065 occurrences
  - `NONE`: 28,921 occurrences

### postal_code
- **Unique Values:** 43,606
- **Top Values:**
  - `e15b70acce0a1519369bcbb58ac68000373c76731e19f9837fecfdd862f36b23`: 1 occurrences
  - `aa81dbdac04f8d9683d3eb6ecf80f11101f8b0e288604e14cfcfe953a0b77dcc`: 1 occurrences
  - `6011cb45b14d6a4b0d432c20843143fd9f851fa9bdeb12c49559edf8bc90c6d8`: 1 occurrences
  - `6e01db77ab1cb6f857e650d3b940a88c252b67fd47c3a672311b886b35f6da37`: 1 occurrences
  - `1b313f0b24f44f558685b2d10c1274001a524f9f49a7a1eb34923a5ec749edf7`: 2 occurrences

### dataset_created_at
- **Unique Values:** 1
- **Average Length:** 26.0 characters
- **Top Values:**
  - `2025-08-16T09:44:24.967209`: 50,000 occurrences

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