# Data Understanding Report
**Generated on:** 2025-08-05 14:23:47
**File:** customers.csv

## 📄 File Information
- **File Path:** `..\data\raw\customers.csv`
- **File Type:** CSV
- **File Size:** 197.54 MB
- **Last Modified:** 2022-01-17 21:12:24

## 📊 Dataset Overview
- **Rows:** 1,371,980
- **Columns:** 7
- **Total Cells:** 9,603,860

## 🔍 Data Quality Summary
- **Completeness Score:** 80.84%
- **Missing Values:** 1,840,558 (19.16%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| customer_id | String | 0 | 0.0% | 1,371,980 | 100.0% |
| FN | Float64 | 895,050 | 65.24% | 2 | 0.0% |
| Active | Float64 | 907,576 | 66.15% | 2 | 0.0% |
| club_member_status | String | 6,062 | 0.44% | 4 | 0.0% |
| fashion_news_frequency | String | 16,009 | 1.17% | 5 | 0.0% |
| age | Int64 | 15,861 | 1.16% | 85 | 0.01% |
| postal_code | String | 0 | 0.0% | 352,899 | 25.72% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| FN | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Active | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| age | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 1,371,980
- **Average Length:** 64.0 characters
- **Top Values:**
  - `17158a7f053bfa99f74c3fa725d42e647d4de1c1ab5ad785d984a2c57aa3c6d6`: 1 occurrences
  - `3a2a16c2b30e80957165a5be16706b0aded3ea29ede4a9ab5dd1471762092282`: 1 occurrences
  - `d65c7d17e56220e5d67bc25397d83721dab446bf99fbb9a4f254ead3380eb3ff`: 1 occurrences
  - `1abf581604fe42a1fb055f94f9ecc3c58aa7894f5a2613d30c2ac5099297fdc7`: 1 occurrences
  - `7195019dfad16dbfca59961d56ddb91bf57a3d93b5065bce07be41a84fb447b7`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Average Length:** 6.27 characters
- **Top Values:**
  - `None`: 6,062 occurrences
  - `LEFT CLUB`: 467 occurrences
  - `PRE-CREATE`: 92,960 occurrences
  - `ACTIVE`: 1,272,491 occurrences

### fashion_news_frequency
- **Unique Values:** 5
- **Average Length:** 5.76 characters
- **Top Values:**
  - `Monthly`: 842 occurrences
  - `None`: 2 occurrences
  - `Regularly`: 477,416 occurrences
  - `NONE`: 877,711 occurrences
  - `None`: 16,009 occurrences

### postal_code
- **Unique Values:** 352,899
- **Average Length:** 64.0 characters
- **Top Values:**
  - `ffecc2c8fac0004626f49bd97748bb422d7be6105ce259159bf387f3d1f55be4`: 2 occurrences
  - `b0b6acf414aae916cd6c5b28fe3ddbbb87230d148542b7838131a4e1589dce23`: 4 occurrences
  - `d144304b4b8808e7de60b63a2a202500aaccf06eefd6c3087a61dc83c2969547`: 3 occurrences
  - `31eea8aaece759a7b9e24f35d041fafaf26cb18fd6c64492ccf20b86205ec882`: 1 occurrences
  - `1440c28d8dbb4dce0de3fc33d78976809e722446d6400809136c2a09cd8446ae`: 7 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 214.99 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 83.739 |
| FN | 10.631 |
| Active | 10.631 |
| club_member_status | 8.1718 |
| fashion_news_frequency | 7.4515 |
| age | 10.631 |
| postal_code | 83.739 |

## 💡 Data Quality Recommendations
- **High missing values detected** - Consider imputation strategies or investigate data collection issues
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** FN, Active, club_member_status, fashion_news_frequency - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*