# Data Understanding Report
**Generated on:** 2025-08-12 10:58:48
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 70.21 MB
- **Last Modified:** 2025-08-12 10:58:42

## 📊 Dataset Overview
- **Rows:** 525,075
- **Columns:** 14
- **Total Cells:** 7,351,050

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| customer_id | String | 0 | 0.0% | 525,075 | 100.0% |
| FN | Float64 | 0 | 0.0% | 2 | 0.0% |
| Active | Float64 | 0 | 0.0% | 2 | 0.0% |
| club_member_status | Categorical | 0 | 0.0% | 4 | 0.0% |
| fashion_news_frequency | Categorical | 0 | 0.0% | 3 | 0.0% |
| age | Float64 | 0 | 0.0% | 83 | 0.02% |
| postal_code | Categorical | 0 | 0.0% | 246,741 | 46.99% |
| FN_imputed | Boolean | 0 | 0.0% | 2 | 0.0% |
| Active_imputed | Boolean | 0 | 0.0% | 2 | 0.0% |
| club_member_status_imputed | Boolean | 0 | 0.0% | 2 | 0.0% |
| fashion_news_frequency_imputed | Boolean | 0 | 0.0% | 2 | 0.0% |
| age_imputed | Boolean | 0 | 0.0% | 2 | 0.0% |
| postal_code_imputed | Boolean | 0 | 0.0% | 1 | 0.0% |
| age_corrected | Boolean | 0 | 0.0% | 1 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| FN | 525075 | 0.4202 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| Active | 525075 | 0.4133 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| age | 525075 | 35.0187 | N/A | 16.0 | N/A | N/A | N/A | 99.0 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `3cf0fbb32bb6879c18b1e7edd70e383cdfd2daa571c49108a43c7f651f1960fd`: 1 occurrences
  - `844f890a35f5f16edff61e0c229a4120b4be3faa050bf1d65448d06595df65c7`: 1 occurrences
  - `225dab084fd8c37d784f1285853db2ee6d1b284e91421c95b7f6b24557fda200`: 1 occurrences
  - `00e59bc10e162c83758a8ece0d6536d96fe2c7afdae9d5f97e58e16bd2a32619`: 1 occurrences
  - `6bd7ec6c805702bb2742e24d14d7d3db3044569306fa59531d38dcf1c51ee07b`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `PRE-CREATE`: 10,707 occurrences
  - `LEFT CLUB`: 65 occurrences
  - `NONE`: 745 occurrences
  - `ACTIVE`: 513,558 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `Monthly`: 165 occurrences
  - `NONE`: 303,821 occurrences
  - `Regularly`: 221,089 occurrences

### postal_code
- **Unique Values:** 246,741
- **Top Values:**
  - `029e1052f1b66d4e3e74ea6218d95186fc964cfd643b839ac603c24693c540ab`: 1 occurrences
  - `7d73adf5f1950d79fce1fdb7d97fb3b4eeaeadb6cacbd09d0afe4870fe38ba2f`: 3 occurrences
  - `2893122a9e32bcce47979b2627dd3cbf2f92ca3785c5e609d8cc55eccd1742b0`: 2 occurrences
  - `890951edf804be6dd01a18481020ef5577d64696abebfdb6a338047a7ac1e05d`: 1 occurrences
  - `959ff299883da9a25ae877063077be5ef22e356a35b1db30f87a5c1a05f12452`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 50.51 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 32.048 |
| FN | 4.006 |
| Active | 4.006 |
| club_member_status | 2.003 |
| fashion_news_frequency | 2.003 |
| age | 4.006 |
| postal_code | 2.003 |
| FN_imputed | 0.0626 |
| Active_imputed | 0.0626 |
| club_member_status_imputed | 0.0626 |
| fashion_news_frequency_imputed | 0.0626 |
| age_imputed | 0.0626 |
| postal_code_imputed | 0.0626 |
| age_corrected | 0.0626 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** FN, Active, club_member_status, fashion_news_frequency, FN_imputed, Active_imputed, club_member_status_imputed, fashion_news_frequency_imputed, age_imputed - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*