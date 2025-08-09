# Data Understanding Report
**Generated on:** 2025-08-09 15:12:53
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 70.18 MB
- **Last Modified:** 2025-08-09 15:12:47

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
  - `8c329e190c1821b6d32a71c1605ff74468f18f751f8d9aa42f94daee99e3130a`: 1 occurrences
  - `2a2b9899fb41c263de8dbec742653336477a6f45ad5194ec4a2a0f53da46c7e1`: 1 occurrences
  - `2dbbcb984f09cf0974a35fb367118f7c59198047df1972758e074b433ad8fbf6`: 1 occurrences
  - `a6e1cda2b1239ed3877ac8e64b768519341a76b1a368dfe0e034a58d4f8ddabb`: 1 occurrences
  - `9ec9ce37cdabdfde9535644fe1335540471a3d6671d6d794d9af6d376a5ee121`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `ACTIVE`: 513,558 occurrences
  - `NONE`: 745 occurrences
  - `LEFT CLUB`: 65 occurrences
  - `PRE-CREATE`: 10,707 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `Monthly`: 165 occurrences
  - `NONE`: 303,821 occurrences
  - `Regularly`: 221,089 occurrences

### postal_code
- **Unique Values:** 246,741
- **Top Values:**
  - `23af2da2e503fe3a52eeaaa1e325445d20d126522a1f86b65d9bf2cdf5db2b1e`: 3 occurrences
  - `50997dbac85e2c4eb197340ae630dba40898b0d1dda2ab00a7353a65db1e6622`: 2 occurrences
  - `edf676a14886b1ee86cf515f4a3bef1281823bdb5d5e51324d3a68af76f00106`: 2 occurrences
  - `86f82603f06e001ec724da05597aa6cd97fc42793eb1773bf50789a03e3f4ad7`: 2 occurrences
  - `b760ec06e12da8aabda28afd5fab404c582741fd490c053e5cd912c3439eea36`: 1 occurrences

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