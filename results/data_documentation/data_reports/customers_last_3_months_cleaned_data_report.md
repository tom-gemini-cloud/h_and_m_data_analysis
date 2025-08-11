# Data Understanding Report
**Generated on:** 2025-08-11 08:15:26
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `../data/cleaned/customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 70.23 MB
- **Last Modified:** 2025-08-11 08:15:24

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
  - `074cf76d8428363648b0ea54d3ff73012ea2cfd26e2b3fd86063988d1f28348f`: 1 occurrences
  - `cc37e63e0bdb02d568abc87a2e12bb00428586f7f65f3e20ea8f9f50aca8396d`: 1 occurrences
  - `5998cee76f6c06d2b661f02d2997e45178bb42490406e490511368e7519ea3a0`: 1 occurrences
  - `5b7b7e965318f95e3b14cbb7bf69a82445346a108ab4e5245ad0d4fe066c4548`: 1 occurrences
  - `f4ef20280543a284b2612c354cbfabc8f1c4b2e0d3c9c248400fdc997f8715ed`: 1 occurrences

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
  - `Regularly`: 221,089 occurrences
  - `NONE`: 303,821 occurrences

### postal_code
- **Unique Values:** 246,741
- **Top Values:**
  - `298996c342f37dbeaf89019c188c8926647c10a649c2b7bcbeff146ca948d441`: 4 occurrences
  - `7c2eba8336f713d769800734cd657a753858093067949a10b94f11c36e77b3e5`: 4 occurrences
  - `5ca1bbaaac1d64ecd494b13b0f06c8b24ab8b76c7d4ceeb618a0f6954b2869f8`: 2 occurrences
  - `dd606ba4be1ee2dd4d1dceb5dadfb81117322e32e0d15612af3adcb7b58042dd`: 4 occurrences
  - `4f1a605e9afbb4a75d663ec3447cb5cc5ac38b6bc9c11f675a615753baac1976`: 1 occurrences

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