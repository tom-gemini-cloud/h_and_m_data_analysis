# Data Understanding Report
**Generated on:** 2025-08-09 14:55:09
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 70.22 MB
- **Last Modified:** 2025-08-09 14:55:03

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
  - `ae31aaf76149ad49a3d61660466e1ebcf6835d17bb78791f25b1b4143abcebd4`: 1 occurrences
  - `a669391e617ad8aa74982f46365cc0d4e2de1d16485981ac8f1e415a6fffff63`: 1 occurrences
  - `1d94ad971aeb21711b706ab2f1e5dd14bfa2c925a3a02ec06c38667c24ac1721`: 1 occurrences
  - `75b69e586025e6f1af18d5a0eb56018fe71065be0d7ae33dd3e69388f517409c`: 1 occurrences
  - `f20853b8d9e980bd99116fa5a4eb00f9817d373d5f187c6f88c3436d3e841f0e`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `PRE-CREATE`: 10,707 occurrences
  - `NONE`: 745 occurrences
  - `LEFT CLUB`: 65 occurrences
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
  - `3a7ef4f557a649f21dde79b36bfb91c0915081bd5b97f0eb1bf8827a7fe03462`: 2 occurrences
  - `484457b1c5ea31c201b2980e985477400ce8dddca3b50a84f8f3b9fc838a5367`: 2 occurrences
  - `68cc1efbc5a90852df194e4960e6022354473475e0718cf421ef778df15419d0`: 1 occurrences
  - `2589ae56a58ffd57acda36768a1744804ce1bb20c3b2b86d3f940e2ac5ae87e0`: 1 occurrences
  - `64485fc548a9b49c99055d1752817e56ebd855c883d140ebb29bcb10e4f8c61c`: 2 occurrences

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