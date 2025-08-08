# Data Understanding Report
**Generated on:** 2025-08-07 16:44:35
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 70.22 MB
- **Last Modified:** 2025-08-07 16:44:29

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
  - `1378fad7a82558d8b68dd7214634902c21b183e7106e776486c8cebe26837d17`: 1 occurrences
  - `51d981f0baef5617806702f0946e81283db9aa4bcf0070b5be848e6662ff6676`: 1 occurrences
  - `8dc19794f8e5d87efedcd46d11ee744c7d85eb9383ceb1fcbcd79ba199dc3083`: 1 occurrences
  - `daa4431474255f3d08643eadffeb58a8c62b1b1e44adbc644feb3763840a5afe`: 1 occurrences
  - `03de1829ca01b8c8f1034642c67cf988ce054d822b4eb8e7054ecea5cc1940aa`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `LEFT CLUB`: 65 occurrences
  - `PRE-CREATE`: 10,707 occurrences
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
  - `c4a5cc8b4e6f01bcc8aad53ccd24b7db4f9439ddedf9b9dd2c61a198eb17da5c`: 1 occurrences
  - `d86d82b304f7c54a635f7239de490d0dd7fe1c58ea8633897641ee559d105d3d`: 3 occurrences
  - `490b09efe64b38ff34c499ebead8f140115d06b27db7b7cea8268621acc9d4ca`: 1 occurrences
  - `ca3b00606afdacbee189a16fcc5b266500f18acfb4c5dec9fde4ae9e4d72f77d`: 3 occurrences
  - `50d584906731af8c191bc9f6a5a0657a5ab503fc76dda6163183e8ea3bf5e766`: 3 occurrences

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