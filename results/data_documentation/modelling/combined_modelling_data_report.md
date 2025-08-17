# Data Understanding Report
**Generated on:** 2025-08-15 18:35:38
**File:** combined_modelling_data.parquet

## 📄 File Information
- **File Path:** `/Users/tom/Data Analysis Projects/h_and_m_data_analysis/notebooks/../data/modelling_data/combined_modelling_data.parquet`
- **File Type:** PARQUET
- **File Size:** 2011.22 MB
- **Last Modified:** 2025-08-15 18:35:32

## 📊 Dataset Overview
- **Rows:** 3,904,391
- **Columns:** 32
- **Total Cells:** 124,940,512

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 2,460 (0.0%)
- **Duplicate Rows:** 328,885 (8.42%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | Date | 0 | 0.0% | 91 | 0.0% |
| customer_id | String | 0 | 0.0% | 525,075 | 13.45% |
| article_id | Int64 | 0 | 0.0% | 42,298 | 1.08% |
| price | Float64 | 0 | 0.0% | 3,236 | 0.08% |
| sales_channel_id | Int64 | 0 | 0.0% | 2 | 0.0% |
| FN | Float64 | 0 | 0.0% | 2 | 0.0% |
| Active | Float64 | 0 | 0.0% | 2 | 0.0% |
| club_member_status | Categorical(Categories("")) | 0 | 0.0% | 4 | 0.0% |
| fashion_news_frequency | Categorical(Categories("")) | 0 | 0.0% | 3 | 0.0% |
| age | Float64 | 0 | 0.0% | 83 | 0.0% |
| postal_code | Categorical(Categories("")) | 0 | 0.0% | 246,741 | 6.32% |
| recency | Int64 | 0 | 0.0% | 91 | 0.0% |
| frequency | UInt32 | 0 | 0.0% | 197 | 0.01% |
| monetary | Float64 | 0 | 0.0% | 131,356 | 3.36% |
| purchase_diversity_score | Float64 | 0 | 0.0% | 21,353 | 0.55% |
| price_sensitivity_index | Float64 | 0 | 0.0% | 269,264 | 6.9% |
| colour_preference_entropy | Float64 | 0 | 0.0% | 24,261 | 0.62% |
| style_consistency_score | Float64 | 0 | 0.0% | 26,821 | 0.69% |
| created_by | String | 0 | 0.0% | 1 | 0.0% |
| product_type_name | Categorical(Categories("")) | 0 | 0.0% | 124 | 0.0% |
| product_group_name | Categorical(Categories("")) | 0 | 0.0% | 18 | 0.0% |
| graphical_appearance_name | Categorical(Categories("")) | 0 | 0.0% | 30 | 0.0% |
| colour_group_name | Categorical(Categories("")) | 0 | 0.0% | 50 | 0.0% |
| perceived_colour_value_name | Categorical(Categories("")) | 0 | 0.0% | 8 | 0.0% |
| perceived_colour_master_name | Categorical(Categories("")) | 0 | 0.0% | 20 | 0.0% |
| department_name | Categorical(Categories("")) | 0 | 0.0% | 238 | 0.01% |
| index_name | Categorical(Categories("")) | 0 | 0.0% | 10 | 0.0% |
| index_group_name | Categorical(Categories("")) | 0 | 0.0% | 5 | 0.0% |
| section_name | Categorical(Categories("")) | 0 | 0.0% | 56 | 0.0% |
| garment_group_name | Categorical(Categories("")) | 0 | 0.0% | 21 | 0.0% |
| detail_desc | Categorical(Categories("")) | 0 | 0.0% | 19,739 | 0.51% |
| bert_cluster | Int64 | 2,460 | 0.06% | 33 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| price | 3904391 | 26.8386 | N/A | 2.39 | N/A | N/A | N/A | 149.99 |
| FN | 3904391 | 0.4506 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| Active | 3904391 | 0.4441 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| age | 3904391 | 35.0048 | N/A | 16.0 | N/A | N/A | N/A | 99.0 |
| recency | 3904391 | 30.1863 | N/A | 1 | N/A | N/A | N/A | 91 |
| monetary | 3904391 | 508.6834 | N/A | 2.39 | N/A | N/A | N/A | 19342.120000000024 |
| purchase_diversity_score | 3904391 | 1.4317 | N/A | -0.0 | N/A | N/A | N/A | 3.139572261986723 |
| price_sensitivity_index | 3904391 | 0.633 | N/A | 0.0 | N/A | N/A | N/A | 2.7934880166020273 |
| colour_preference_entropy | 3904391 | 2.1974 | N/A | -0.0 | N/A | N/A | N/A | 4.747015200541311 |
| style_consistency_score | 3904391 | 0.1858 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| bert_cluster | 3901931 | 16.2387 | N/A | 0 | N/A | N/A | N/A | 31 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `a7a6d967223cf33aae2d345e8840b3716380a9ce3499609ef1b53f15f7803702`: 1 occurrences
  - `6285ee21fa6fa5653e3204671b543a77eb5fbbe2ecbc1567c80b7a529c7d6cd4`: 5 occurrences
  - `4e5992993c3a2f87f3d165357f77416e476d57be5651679f95397859a4ddf035`: 50 occurrences
  - `96c27089edb4f90d31ef7a757d11b499ca5fa373786ca7e225c43b51cc3512cb`: 6 occurrences
  - `10fe02a6042f5819e0bc6f0ac821ea075a333f931d9c05a57b40793126e2db7b`: 22 occurrences

### created_by
- **Unique Values:** 1
- **Average Length:** 34.0 characters
- **Top Values:**
  - `customer_feature_engineering.ipynb`: 3,904,391 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 1005.82 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 14.8941 |
| customer_id | 238.3051 |
| article_id | 29.7881 |
| price | 29.7881 |
| sales_channel_id | 29.7881 |
| FN | 29.7881 |
| Active | 29.7881 |
| club_member_status | 14.8941 |
| fashion_news_frequency | 14.8941 |
| age | 29.7881 |
| postal_code | 14.8941 |
| recency | 29.7881 |
| frequency | 14.8941 |
| monetary | 29.7881 |
| purchase_diversity_score | 29.7881 |
| price_sensitivity_index | 29.7881 |
| colour_preference_entropy | 29.7881 |
| style_consistency_score | 29.7881 |
| created_by | 126.5996 |
| product_type_name | 14.8941 |
| product_group_name | 14.8941 |
| graphical_appearance_name | 14.8941 |
| colour_group_name | 14.8941 |
| perceived_colour_value_name | 14.8941 |
| perceived_colour_master_name | 14.8941 |
| department_name | 14.8941 |
| index_name | 14.8941 |
| index_group_name | 14.8941 |
| section_name | 14.8941 |
| garment_group_name | 14.8941 |
| detail_desc | 14.8941 |
| bert_cluster | 30.2536 |

## 💡 Data Quality Recommendations
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** sales_channel_id, FN, Active, club_member_status, fashion_news_frequency, perceived_colour_value_name, index_name, index_group_name - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*