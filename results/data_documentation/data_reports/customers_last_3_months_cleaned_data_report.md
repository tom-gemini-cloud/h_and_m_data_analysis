# Data Understanding Report
**Generated on:** 2025-08-09 15:31:45
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 70.18 MB
- **Last Modified:** 2025-08-09 15:31:38

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
  - `44503a208cafe5a609a889e77533213736ff1742d415a9e7e253d9a70a851a89`: 1 occurrences
  - `f4cef1c0077ffe121a5f78a4462d67b6f88a57bf40d150cb5490a6630aede2b2`: 1 occurrences
  - `d6f4667fad7958e590e069876fe8fa4e7417609ed341f4a8e6aa04b1d4ebdeeb`: 1 occurrences
  - `e45a1d0b4f7421b74e986e86439ecd1a6d85ab016b0aeea9aebac3e99988f76f`: 1 occurrences
  - `7153553a29a40dd7d754e058df8f3a620a2cbc8f26f35814d803092e3375316e`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `NONE`: 745 occurrences
  - `PRE-CREATE`: 10,707 occurrences
  - `LEFT CLUB`: 65 occurrences
  - `ACTIVE`: 513,558 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `NONE`: 303,821 occurrences
  - `Regularly`: 221,089 occurrences
  - `Monthly`: 165 occurrences

### postal_code
- **Unique Values:** 246,741
- **Top Values:**
  - `eba24ac7f68e245a31048f49a197649b9138a62dd37179dd20500496433aaed0`: 2 occurrences
  - `bb4b88ac512f854cbb9a032115ca37aad0d5d713be53cf038c94466b1f91e18e`: 1 occurrences
  - `9d6a6637310ab9e82feecbac9a56f35876caf02e8f5c722c28f36100a6a2a9cd`: 1 occurrences
  - `fb3166e80a53520bab7e31965815a273f30a33d9639939cdb25992f58a9594a8`: 1 occurrences
  - `4dcd85ea02ed80e0fd9eb2a7b3cd4cd4f38ab35644b0a087832e70aaedf04330`: 1 occurrences

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