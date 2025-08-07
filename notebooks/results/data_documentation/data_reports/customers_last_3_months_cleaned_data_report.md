# Data Understanding Report
**Generated on:** 2025-08-07 10:35:48
**File:** customers_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `../data/cleaned/customers_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 86.53 MB
- **Last Modified:** 2025-08-07 10:35:45

## 📊 Dataset Overview
- **Rows:** 525,075
- **Columns:** 13
- **Total Cells:** 6,825,975

## 🔍 Data Quality Summary
- **Completeness Score:** 92.31%
- **Missing Values:** 525,075 (7.69%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| customer_id | String | 0 | 0.0% | 525,075 | 100.0% |
| FN | Float64 | 0 | 0.0% | 2 | 0.0% |
| Active | Categorical | 525,075 | 100.0% | 1 | 0.0% |
| club_member_status | Categorical | 0 | 0.0% | 4 | 0.0% |
| fashion_news_frequency | Categorical | 0 | 0.0% | 3 | 0.0% |
| age | Float64 | 0 | 0.0% | 83 | 0.02% |
| postal_code | Categorical | 0 | 0.0% | 246,741 | 46.99% |
| FN_imputed | Boolean | 0 | 0.0% | 1 | 0.0% |
| Active_imputed | Boolean | 0 | 0.0% | 1 | 0.0% |
| club_member_status_imputed | Boolean | 0 | 0.0% | 1 | 0.0% |
| fashion_news_frequency_imputed | Boolean | 0 | 0.0% | 1 | 0.0% |
| age_imputed | Boolean | 0 | 0.0% | 1 | 0.0% |
| age_corrected | Boolean | 0 | 0.0% | 1 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| FN | 525075 | 0.4202 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| age | 525075 | 35.0187 | N/A | 16.0 | N/A | N/A | N/A | 99.0 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `c272d4f355df5469b24fb3e0188c11668bfb736b16be5178f64fb1cf8eaaf655`: 1 occurrences
  - `d436d41a893a1cf6453e971bd23fc2b18e6eec8f46b8b6836f5ce03dd11e79a6`: 1 occurrences
  - `414f6ea9bc13bce2555400b350b08ab8051c7f15cb21df13ce051ce23ce1a343`: 1 occurrences
  - `dd6e7fd0629efef7c150411eda5c5ce6429593428f5102f25e6d043d601d598b`: 1 occurrences
  - `453920fa84204450fda7f6f37ca5be87dfc765c7e86a501717806afd2342eb20`: 1 occurrences

### Active
- **Unique Values:** 1
- **Top Values:**
  - `None`: 525,075 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `NONE`: 745 occurrences
  - `PRE-CREATE`: 10,707 occurrences
  - `ACTIVE`: 513,558 occurrences
  - `LEFT CLUB`: 65 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `Monthly`: 165 occurrences
  - `Regularly`: 221,089 occurrences
  - `NONE`: 303,821 occurrences

### postal_code
- **Unique Values:** 246,741
- **Top Values:**
  - `73d35a38a9e51ca07d3a1dcf2c37d0ca5de69fc2d943b1726bc9bd08aa1d3928`: 4 occurrences
  - `93c308f0ac5de823b9491bc8b7bba268a643c218ac4963bf189e4341122643e1`: 1 occurrences
  - `fbc2d6d108704e02ad71d8326bc33886c6d9d3eafa37fe78f6e3949b4bdc6647`: 3 occurrences
  - `b05383f6581196ffec53889c9238a7a4fbdb909e3e0fd24527fb0043fd68dcfb`: 4 occurrences
  - `fab10ca8a836bc4ec8136e5de83a81502e91f253154761ac9123dd2b9446de92`: 5 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 48.51 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 32.048 |
| FN | 4.006 |
| Active | 2.0656 |
| club_member_status | 2.003 |
| fashion_news_frequency | 2.003 |
| age | 4.006 |
| postal_code | 2.003 |
| FN_imputed | 0.0626 |
| Active_imputed | 0.0626 |
| club_member_status_imputed | 0.0626 |
| fashion_news_frequency_imputed | 0.0626 |
| age_imputed | 0.0626 |
| age_corrected | 0.0626 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** FN, club_member_status, fashion_news_frequency - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*