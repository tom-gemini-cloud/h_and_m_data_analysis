# Data Understanding Report
**Generated on:** 2025-08-14 20:25:02
**File:** customers.csv

## 📄 File Information
- **File Path:** `data\raw\customers.csv`
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
| FN | 476930 | 1.0 | N/A | 1.0 | N/A | N/A | N/A | 1.0 |
| Active | 464404 | 1.0 | N/A | 1.0 | N/A | N/A | N/A | 1.0 |
| age | 1356119 | 36.387 | N/A | 16 | N/A | N/A | N/A | 99 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 1,371,980
- **Average Length:** 64.0 characters
- **Top Values:**
  - `38607e62ce9053b9a0e8c70ae680430ed05a104871d5beaabe3643bd7fb07a20`: 1 occurrences
  - `c7e0fba695f8a0e5913d882283782732e161f806f900ec840f402946604f4140`: 1 occurrences
  - `12f94b23fdc20ab9b35816d3735cd5fe120701b29e4e7ad8117009bef5dde62c`: 1 occurrences
  - `d959039804ca5407e13e34dae32a16d18bcb5f785a89e44c8508e89da0f48b7a`: 1 occurrences
  - `9edc741ac8684f90085d08a94af36ef96f4d8d4fbffc724aa1213e3b939c51a6`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Average Length:** 6.27 characters
- **Top Values:**
  - `PRE-CREATE`: 92,960 occurrences
  - `ACTIVE`: 1,272,491 occurrences
  - `None`: 6,062 occurrences
  - `LEFT CLUB`: 467 occurrences

### fashion_news_frequency
- **Unique Values:** 5
- **Average Length:** 5.76 characters
- **Top Values:**
  - `None`: 16,009 occurrences
  - `Monthly`: 842 occurrences
  - `Regularly`: 477,416 occurrences
  - `NONE`: 877,711 occurrences
  - `None`: 2 occurrences

### postal_code
- **Unique Values:** 352,899
- **Average Length:** 64.0 characters
- **Top Values:**
  - `79b15d18e613f10ee7fba190965d213fe47c1b9bb7cb97366cd1694e08812d21`: 1 occurrences
  - `7b093cc1d22b65bc91360e39311e03c5eeb5362d3c0f920c989fc3a53f01086b`: 1 occurrences
  - `d53b7741d20cb14245a91bcc7b321f875bec9881bb265ca029a8ee7e9eae392a`: 3 occurrences
  - `f203c8bcddaf2644a89d79003a5a49ec1ef12c6cd0c501f905e6f7c86771e9b8`: 2 occurrences
  - `d4490400e0e2398837dfb1597fe8cdb825a264e74ce3575a0d2b806042c8ddc9`: 2 occurrences

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