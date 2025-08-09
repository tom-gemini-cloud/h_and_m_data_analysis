# Data Understanding Report
**Generated on:** 2025-08-09 13:02:45
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 70.2 MB
- **Last Modified:** 2025-08-09 13:02:40

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
  - `e214c8cfac03d3f769b0275dbdb126908f673ad628f44aded8e4863274b91a1c`: 1 occurrences
  - `9d081a243d9861b77fc59739dcdb835add21cbddf27acacc409ad04b8b4f756e`: 1 occurrences
  - `92c96e4acc3f55828df07e6502cb930fe928714eda69c700779a286632926160`: 1 occurrences
  - `d2892602d20c7bd55f8c8d6c3881819594e199aa51ea29d6980bef5ba0fac93c`: 1 occurrences
  - `902f9c0b6e5bb7e615a86653da13a4d937e3903abaeee060a094c6b11d5ee8b3`: 1 occurrences

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
  - `NONE`: 303,821 occurrences
  - `Regularly`: 221,089 occurrences
  - `Monthly`: 165 occurrences

### postal_code
- **Unique Values:** 246,741
- **Top Values:**
  - `645425053886f23e39d6c2ce53184cc83553f8dc1cd7e4e70c15d12021bf9b34`: 2 occurrences
  - `8a044d1feb14ea2901db41b364a020a64e1285a0b247f839defcf2776f5a99a2`: 1 occurrences
  - `a9e8c08c6c383686ed4f6a1a5ae85d72ae7373ef07cf898ab8ea2b164d6e6f2e`: 2 occurrences
  - `e6116c7ab88473d401396c8bea50ed0cad76aa002e3411ed66c07263b6c1ace2`: 1 occurrences
  - `690b589db761e08b4bb174430c1340899615d8cac984bde4beb806e9d6d5bdf0`: 1 occurrences

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