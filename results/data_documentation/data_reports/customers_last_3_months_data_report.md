# Data Understanding Report
**Generated on:** 2025-08-09 12:33:38
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
  - `29c769737590f954d500310e374e787c4b9b6f4e11fb5ac8ddeb2160c9e18079`: 1 occurrences
  - `7d2d2eac77732fac2f5d8802149836a411cbcbdb3f2ce9c107fa6cf5a897b280`: 1 occurrences
  - `60cb4cabb38775f0be729bf31178880445b7f18be0b0c04f89668d87fa0d7e56`: 1 occurrences
  - `4e09c880befd368e651b4391b940715e3c2280c7b3e7fac478d0d25f4eb58a23`: 1 occurrences
  - `af18128d2d491f89503541d6328385d316a5e8c5c69653349d090427abf20493`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Average Length:** 6.08 characters
- **Top Values:**
  - `None`: 745 occurrences
  - `ACTIVE`: 513,558 occurrences
  - `LEFT CLUB`: 65 occurrences
  - `PRE-CREATE`: 10,707 occurrences

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
  - `7bdeb6d8cf0db5dc29c517ff22534df41c9cb12f3cfe594d7440af37a013ca8c`: 1 occurrences
  - `a382e30211d3ea881432e174080bf896d0e9f9954478ffca14b8bc03df170e12`: 2 occurrences
  - `73a4170196ca47114a8331e39a34a73b108235cbcdf2df2a3ab3e59778dc8922`: 1 occurrences
  - `afab16f760290791c820c332d53ce2c0edb7b99556d0490e4ab253dd4d10005e`: 2 occurrences
  - `8d3252cc40060ff48dc4ffba29f6cf556a420167180671f4b16d9b4e8a24e79b`: 2 occurrences

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