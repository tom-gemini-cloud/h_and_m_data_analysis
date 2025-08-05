# Data Understanding Report
**Generated on:** 2025-08-05 15:19:43
**File:** customers_last_3_months.csv

## 📄 File Information
- **File Path:** `..\data\processed\customers_last_3_months.csv`
- **File Type:** CSV
- **File Size:** 75.94 MB
- **Last Modified:** 2025-08-05 13:24:29

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
  - `dfce581451106f0abe486188c9d26fbf46b7e8aa32ca4c6e519525e1b52bb035`: 1 occurrences
  - `9282b366ff0b12e8a5553d1c6469f7c3889b79f053267141fe9e1c6b220dbec5`: 1 occurrences
  - `fb762bd8a3df8f6491025d3819108c162ef6252bef730731e8b989be5297343b`: 1 occurrences
  - `18df4b8a2c464bdedb0be9fa7b9b2b6c950161be341dca9d500eaac865f8817e`: 1 occurrences
  - `7afa4521ff4ced5ffe06be00135bf2c229c199067a2f0a54a705fcca10106572`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Average Length:** 6.08 characters
- **Top Values:**
  - `LEFT CLUB`: 65 occurrences
  - `None`: 745 occurrences
  - `PRE-CREATE`: 10,707 occurrences
  - `ACTIVE`: 513,558 occurrences

### fashion_news_frequency
- **Unique Values:** 4
- **Average Length:** 6.11 characters
- **Top Values:**
  - `NONE`: 301,797 occurrences
  - `None`: 2,024 occurrences
  - `Monthly`: 165 occurrences
  - `Regularly`: 221,089 occurrences

### postal_code
- **Unique Values:** 246,741
- **Average Length:** 64.0 characters
- **Top Values:**
  - `ccb965048f7c0f285a6df40659f1d1277c91ff12fe76924b3111f00966989c69`: 3 occurrences
  - `da579811ef8a4cc36412439cd9d7648c831436f9242a4dbea666b0694536084a`: 6 occurrences
  - `774f67a6a3ebd6f3fe229aed9dfad300c9a6fdae245afe19a19f7970af7b0e4a`: 3 occurrences
  - `44c66ba088dc680d3a726ee1d198e0aef70bbba4cd168b920aef89cbc80437a8`: 1 occurrences
  - `49a6e0f79e5a7d207ee8c8d04a10c7ef9864ec2b8d3126b746ee089d94a85331`: 2 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 82.39 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 32.048 |
| FN | 4.0687 |
| Active | 4.0687 |
| club_member_status | 3.0413 |
| fashion_news_frequency | 3.05 |
| age | 4.0687 |
| postal_code | 32.048 |

## 💡 Data Quality Recommendations
- **High missing values detected** - Consider imputation strategies or investigate data collection issues
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** FN, Active, club_member_status, fashion_news_frequency - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*