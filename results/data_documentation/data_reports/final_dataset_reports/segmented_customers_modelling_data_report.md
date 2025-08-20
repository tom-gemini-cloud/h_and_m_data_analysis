# Data Understanding Report
**Generated on:** 2025-08-20 11:03:02
**File:** segmented_customers.parquet

## 📄 File Information
- **File Path:** `data/modelling_data/segmented_customers.parquet`
- **File Type:** PARQUET
- **File Size:** 78.24 MB
- **Last Modified:** 2025-08-20 11:00:40

## 📊 Dataset Overview
- **Rows:** 525,075
- **Columns:** 15
- **Total Cells:** 7,876,125

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
| club_member_status | Categorical(Categories("")) | 0 | 0.0% | 4 | 0.0% |
| fashion_news_frequency | Categorical(Categories("")) | 0 | 0.0% | 3 | 0.0% |
| age | Float64 | 0 | 0.0% | 83 | 0.02% |
| postal_code | Categorical(Categories("")) | 0 | 0.0% | 246,741 | 46.99% |
| recency | Int64 | 0 | 0.0% | 91 | 0.02% |
| frequency | UInt32 | 0 | 0.0% | 197 | 0.04% |
| monetary | Float64 | 0 | 0.0% | 131,356 | 25.02% |
| purchase_diversity_score | Float64 | 0 | 0.0% | 21,401 | 4.08% |
| price_sensitivity_index | Float64 | 0 | 0.0% | 269,264 | 51.28% |
| colour_preference_entropy | Float64 | 0 | 0.0% | 24,206 | 4.61% |
| style_consistency_score | Float64 | 0 | 0.0% | 26,898 | 5.12% |
| customer_cluster | Int32 | 0 | 0.0% | 5 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| FN | 525075 | 0.4202 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| Active | 525075 | 0.4133 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| age | 525075 | 35.0187 | N/A | 16.0 | N/A | N/A | N/A | 99.0 |
| recency | 525075 | 38.5421 | N/A | 1 | N/A | N/A | N/A | 91 |
| monetary | 525075 | 199.5682 | N/A | 2.39 | N/A | N/A | N/A | 19342.120000000024 |
| purchase_diversity_score | 525075 | 0.9555 | N/A | 0.0 | N/A | N/A | N/A | 3.139572261986723 |
| price_sensitivity_index | 525075 | 0.4651 | N/A | 0.0 | N/A | N/A | N/A | 2.7934880166020273 |
| colour_preference_entropy | 525075 | 1.4449 | N/A | 0.0 | N/A | N/A | N/A | 4.74701520054131 |
| style_consistency_score | 525075 | 0.3311 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| customer_cluster | 525075 | 2.1908 | N/A | 0 | N/A | N/A | N/A | 4 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `133a7f1c86f727e83f61eefee93c518d94962dfcf526b3382ab14bd2f4f3dccc`: 1 occurrences
  - `645883bd594d02487e90861a1779f9cc7b025f89ecf79db5b5bc9b2542bd17f3`: 1 occurrences
  - `f236c5072b3305daa55f38d1fb8c25bca7dcece4ba927a2a158ebe56672999c1`: 1 occurrences
  - `d082105fa4336abb19fc6374a2908766f06069f80279a7872419f2482ed479d8`: 1 occurrences
  - `a1319189650357cd0cb68ee01e25f530e3d62f2025a4d0436eedae56015c55fc`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 78.12 MB

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
| recency | 4.006 |
| frequency | 2.003 |
| monetary | 4.006 |
| purchase_diversity_score | 4.006 |
| price_sensitivity_index | 4.006 |
| colour_preference_entropy | 4.006 |
| style_consistency_score | 4.006 |
| customer_cluster | 2.003 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** FN, Active, club_member_status, fashion_news_frequency, customer_cluster - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*