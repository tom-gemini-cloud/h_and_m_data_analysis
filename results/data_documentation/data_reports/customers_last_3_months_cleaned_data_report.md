# Data Understanding Report
**Generated on:** 2025-08-09 11:20:42
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 70.19 MB
- **Last Modified:** 2025-08-09 11:20:36

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
  - `57dbfd4ae3c29b409f213fd2a085b804680bfc617863abe51aac833297bcdb27`: 1 occurrences
  - `5ca8cac3ae3a1c23121709648b28c96e61d29524c1867c01b8f012bd3c30e96c`: 1 occurrences
  - `76e77006524dbd04837503c9193463a7104834f9247996366c66777f36668661`: 1 occurrences
  - `2f4fca7bf07d6d86be80f80dc0382f467320a8ad209babcf15a685c375cc4e7b`: 1 occurrences
  - `ee3062e90a262b4f839f19137b0f47bdcdf3d4a6d3ad61ba07c6b68662baeefb`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `LEFT CLUB`: 65 occurrences
  - `NONE`: 745 occurrences
  - `PRE-CREATE`: 10,707 occurrences
  - `ACTIVE`: 513,558 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `Regularly`: 221,089 occurrences
  - `NONE`: 303,821 occurrences
  - `Monthly`: 165 occurrences

### postal_code
- **Unique Values:** 246,741
- **Top Values:**
  - `c76c444062d190b0646c17859f6467fa95fe689a5d16f025b2a27f4822220bfb`: 6 occurrences
  - `0c6f4217e913f6cf47b891bda4d77e120e011a3a79612714e703d27b035045f2`: 8 occurrences
  - `9c92c8522c20e950564f66f01e0504042d4b2dbd5bac540957ad8cfa7fda7c49`: 1 occurrences
  - `8ada62554f4383d7b4904628797894ed3078112c1059158dfc59cc398d7b7e20`: 4 occurrences
  - `ca21ff516b41d8bf50ea5ab8307182f02a0e6c84b265709f24786038d2e18abf`: 4 occurrences

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