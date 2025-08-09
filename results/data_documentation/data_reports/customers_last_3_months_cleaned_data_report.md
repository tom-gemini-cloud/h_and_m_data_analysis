# Data Understanding Report
**Generated on:** 2025-08-09 15:00:02
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 70.2 MB
- **Last Modified:** 2025-08-09 14:59:56

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
  - `88e37d8e856e423b152adf8114e34361eff876cdc49589d5fab36ed66aa2ac76`: 1 occurrences
  - `1f5e3e6e69c24105f300f59dde76988f380951259874b4c8b3dbb5592b191c58`: 1 occurrences
  - `98cc7dee3909e5456acc6c837bbafaf2323f39016a5f818f9d561aba5121b275`: 1 occurrences
  - `c6528a3f8d2106da0728464798e69316e8d8bc6a09f4af26603718794ed47815`: 1 occurrences
  - `a2e5283fc9181fecece5d4e9fc4691096ce190f986b76214912b5b16fcb4b10d`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `LEFT CLUB`: 65 occurrences
  - `NONE`: 745 occurrences
  - `ACTIVE`: 513,558 occurrences
  - `PRE-CREATE`: 10,707 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `Monthly`: 165 occurrences
  - `Regularly`: 221,089 occurrences
  - `NONE`: 303,821 occurrences

### postal_code
- **Unique Values:** 246,741
- **Top Values:**
  - `debb58e679dee16c6f4c2badf54de56e8f6312ee55d815d5f315cfd65c4ea0cb`: 2 occurrences
  - `3bfe61ff33e1ed2d0ffd495fb407812500f0d1bc8ba874b0f166d9b8e2d7cf59`: 2 occurrences
  - `9a19d1f4b74c139b4a0226e6bceaecf795bc0b441ebc88cf01848b5a71a06ea3`: 1 occurrences
  - `c18c219bd9c3a50f1ae495ef51c68aaddfb671d991b5219e92f43baf8d299ba4`: 1 occurrences
  - `9ae8e390d1821482fe7e04d9b6b868b6217cf6ec2620677472ff7da784f62de7`: 2 occurrences

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