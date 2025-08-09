# Data Understanding Report
**Generated on:** 2025-08-09 11:49:00
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 70.21 MB
- **Last Modified:** 2025-08-09 11:48:54

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
  - `394ce3bc2d7f0c90269ca2d5e8a8ea6ce532860d84437a5b2a72e2a3dbb8d54d`: 1 occurrences
  - `9437c1b91b0819b2a70afa6be28e08bd80ec126dc650ba3d0f867f4dd8849516`: 1 occurrences
  - `f99ecc96a28f5ea45843e90c1ee4efbaba404ca600ff3e8271cb68ff47341b74`: 1 occurrences
  - `a110e3b7a3d4e35c15b1c3798318e6b30fb2e897cb835ba56e899d64e6768af0`: 1 occurrences
  - `82ec56a6cabcf61eb7d60e1f14871602a06d3a9d00a5bae2fb4d88049ea777f1`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `ACTIVE`: 513,558 occurrences
  - `LEFT CLUB`: 65 occurrences
  - `PRE-CREATE`: 10,707 occurrences
  - `NONE`: 745 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `Monthly`: 165 occurrences
  - `NONE`: 303,821 occurrences
  - `Regularly`: 221,089 occurrences

### postal_code
- **Unique Values:** 246,741
- **Top Values:**
  - `efb7aec4c431f7797ccde92654238b602f37132600dd29d771af402014970280`: 1 occurrences
  - `3b871f07b8493b8c0f95d3aafde96fe394a687418aedecc5e443d30145851c26`: 2 occurrences
  - `601d18436cc8bb3895176b1d5989aa187e13a9edaa62f519a61d35dc708ac96c`: 5 occurrences
  - `37b8b567ade7308982dff8b5e1716b70bc9f69b3919b9ddf73cd1c0bd11d98a9`: 3 occurrences
  - `120202dc5a75e2e7894dde06bd8820bb3b7813aefc1d1639712898bbf772b4c4`: 1 occurrences

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