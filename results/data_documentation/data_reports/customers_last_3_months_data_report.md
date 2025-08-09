# Data Understanding Report
**Generated on:** 2025-08-09 11:24:33
**File:** customers_last_3_months.parquet

## 📄 File Information
- **File Path:** `..\data\processed\customers_last_3_months.parquet`
- **File Type:** PARQUET
- **File Size:** 30.0 MB
- **Last Modified:** 2025-08-09 11:18:30

## 📊 Dataset Overview
- **Rows:** 525,075
- **Columns:** 7
- **Total Cells:** 3,675,525

## 🔍 Data Quality Summary
- **Completeness Score:** 83.18%
- **Missing Values:** 618,175 (16.82%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| customer_id | String | 0 | 0.0% | 525,075 | 100.0% |
| FN | Float64 | 304,417 | 57.98% | 2 | 0.0% |
| Active | Float64 | 308,036 | 58.67% | 2 | 0.0% |
| club_member_status | String | 745 | 0.14% | 4 | 0.0% |
| fashion_news_frequency | String | 2,024 | 0.39% | 4 | 0.0% |
| age | Int64 | 2,953 | 0.56% | 84 | 0.02% |
| postal_code | String | 0 | 0.0% | 246,741 | 46.99% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| FN | 220658 | 1.0 | N/A | 1.0 | N/A | N/A | N/A | 1.0 |
| Active | 217039 | 1.0 | N/A | 1.0 | N/A | N/A | N/A | 1.0 |
| age | 522122 | 35.0471 | N/A | 16 | N/A | N/A | N/A | 99 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `e2bde14542cf4dc8cc161167b2406478eefb07256cd4c4541fb250b07ff57841`: 1 occurrences
  - `88a27a9b098012246444cdaeeb846ba84a38bfe840007442538c4d9726492bb3`: 1 occurrences
  - `a658c98f027d9c94b6a1f01dea9a9e86bcbbdc9a8700012eecbd252d743a1109`: 1 occurrences
  - `b1dbd2e8b78eddfc2e3812168ca34ed1926907ec75a748fe620da69ab74e12f8`: 1 occurrences
  - `88f85f882781202f65b814feab9b405def8d9e4a544e6cff8edcf6f2e7d46606`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Average Length:** 6.08 characters
- **Top Values:**
  - `PRE-CREATE`: 10,707 occurrences
  - `LEFT CLUB`: 65 occurrences
  - `None`: 745 occurrences
  - `ACTIVE`: 513,558 occurrences

### fashion_news_frequency
- **Unique Values:** 4
- **Average Length:** 6.11 characters
- **Top Values:**
  - `Regularly`: 221,089 occurrences
  - `Monthly`: 165 occurrences
  - `NONE`: 301,797 occurrences
  - `None`: 2,024 occurrences

### postal_code
- **Unique Values:** 246,741
- **Average Length:** 64.0 characters
- **Top Values:**
  - `3e598af0bc7109514b0848b4f12a3ebd7c2c35a2d348a9c9e86c4b0ee1cc09a1`: 2 occurrences
  - `a7acf16a8907d0d1d9621c1ef3b86191f44049c762999418e8e1a43e9c534548`: 1 occurrences
  - `b8410e20731e06211fe9f405faa9ee338a99ce0a54aeb3ae12c2428857766243`: 7 occurrences
  - `f7e81065c55073f20602bd290afcc989f8043eec13c6c2b9f5bd19685aa8e3f9`: 1 occurrences
  - `577c2c90023a845156208433c923a299169c418b70ceddf09799d3cfb2f4843d`: 4 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 82.41 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 32.048 |
| FN | 4.0686 |
| Active | 4.0686 |
| club_member_status | 3.0455 |
| fashion_news_frequency | 3.0618 |
| age | 4.0686 |
| postal_code | 32.048 |

## 💡 Data Quality Recommendations
- **High missing values detected** - Consider imputation strategies or investigate data collection issues
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** FN, Active, club_member_status, fashion_news_frequency - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*