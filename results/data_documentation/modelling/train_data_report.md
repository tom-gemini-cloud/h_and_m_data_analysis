# Data Understanding Report
**Generated on:** 2025-08-15 14:03:10
**File:** train_data.parquet

## 📄 File Information
- **File Path:** `data\modelling_data\train_data.parquet`
- **File Type:** PARQUET
- **File Size:** 1451.06 MB
- **Last Modified:** 2025-08-15 14:00:26

## 📊 Dataset Overview
- **Rows:** 3,122,370
- **Columns:** 40
- **Total Cells:** 124,894,800

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 1,969 (0.0%)
- **Duplicate Rows:** 263,176 (8.43%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | Date | 0 | 0.0% | 91 | 0.0% |
| customer_id | String | 0 | 0.0% | 420,060 | 13.45% |
| article_id | Int64 | 0 | 0.0% | 40,717 | 1.3% |
| price | Float64 | 0 | 0.0% | 3,207 | 0.1% |
| sales_channel_id | Int64 | 0 | 0.0% | 2 | 0.0% |
| FN | Float64 | 0 | 0.0% | 2 | 0.0% |
| Active | Float64 | 0 | 0.0% | 2 | 0.0% |
| club_member_status | Categorical(Categories("")) | 0 | 0.0% | 4 | 0.0% |
| fashion_news_frequency | Categorical(Categories("")) | 0 | 0.0% | 3 | 0.0% |
| age | Float64 | 0 | 0.0% | 83 | 0.0% |
| postal_code | Categorical(Categories("")) | 0 | 0.0% | 219,727 | 7.04% |
| recency | Int64 | 0 | 0.0% | 91 | 0.0% |
| frequency | UInt32 | 0 | 0.0% | 188 | 0.01% |
| monetary | Float64 | 0 | 0.0% | 115,198 | 3.69% |
| purchase_diversity_score | Float64 | 0 | 0.0% | 18,365 | 0.59% |
| price_sensitivity_index | Float64 | 0 | 0.0% | 219,293 | 7.02% |
| colour_preference_entropy | Float64 | 0 | 0.0% | 20,752 | 0.66% |
| style_consistency_score | Float64 | 0 | 0.0% | 22,826 | 0.73% |
| created_by | String | 0 | 0.0% | 1 | 0.0% |
| rfm_cluster | Int32 | 0 | 0.0% | 2 | 0.0% |
| preference_cluster | Int32 | 0 | 0.0% | 2 | 0.0% |
| hybrid_cluster | Int32 | 0 | 0.0% | 2 | 0.0% |
| behavioural_cluster | Int32 | 0 | 0.0% | 6 | 0.0% |
| rfm_cluster_label | String | 0 | 0.0% | 2 | 0.0% |
| preference_cluster_label | String | 0 | 0.0% | 2 | 0.0% |
| hybrid_cluster_label | String | 0 | 0.0% | 2 | 0.0% |
| behavioural_cluster_label | String | 0 | 0.0% | 1 | 0.0% |
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
| detail_desc | Categorical(Categories("")) | 0 | 0.0% | 19,105 | 0.61% |
| bert_cluster | Int32 | 1,969 | 0.06% | 33 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| price | 3122370 | 26.8452 | N/A | 2.39 | N/A | N/A | N/A | 149.99 |
| FN | 3122370 | 0.4506 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| Active | 3122370 | 0.4441 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| age | 3122370 | 35.0051 | N/A | 16.0 | N/A | N/A | N/A | 99.0 |
| recency | 3122370 | 30.1932 | N/A | 1 | N/A | N/A | N/A | 91 |
| monetary | 3122370 | 509.4994 | N/A | 2.39 | N/A | N/A | N/A | 19342.120000000024 |
| purchase_diversity_score | 3122370 | 1.4321 | N/A | -0.0 | N/A | N/A | N/A | 3.1395722619867232 |
| price_sensitivity_index | 3122370 | 0.6334 | N/A | 0.0 | N/A | N/A | N/A | 2.7934880166020273 |
| colour_preference_entropy | 3122370 | 2.198 | N/A | -0.0 | N/A | N/A | N/A | 4.747015200541309 |
| style_consistency_score | 3122370 | 0.1858 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| rfm_cluster | 3122370 | 0.3587 | N/A | 0 | N/A | N/A | N/A | 1 |
| preference_cluster | 3122370 | 0.9167 | N/A | 0 | N/A | N/A | N/A | 1 |
| hybrid_cluster | 3122370 | 0.089 | N/A | 0 | N/A | N/A | N/A | 1 |
| behavioural_cluster | 3122370 | 1.5117 | N/A | 0 | N/A | N/A | N/A | 5 |
| bert_cluster | 3120401 | 15.3356 | N/A | 0 | N/A | N/A | N/A | 31 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 420,060
- **Average Length:** 64.0 characters
- **Top Values:**
  - `a9d23d1680ba31412496dd2f792e3f79ae7c9e9e960449059c51b612938d0835`: 6 occurrences
  - `406ebf3862395897d89658179ea9bbedfbf005101224fdbe03285977429e1843`: 11 occurrences
  - `d81d80a3145998b3e0cbd21cbacb2f4bb404b1f42c2769ff6649fea918b02428`: 2 occurrences
  - `db81aeadf0e5ffb25b730c58eaaef5949232d674158bb5af89ea01b9382e6f32`: 1 occurrences
  - `16279eac6c24fafd3130a363605a2bd8ec24bca8058792d65cadb4405d1c5264`: 11 occurrences

### created_by
- **Unique Values:** 1
- **Average Length:** 34.0 characters
- **Top Values:**
  - `customer_feature_engineering.ipynb`: 3,122,370 occurrences

### rfm_cluster_label
- **Unique Values:** 2
- **Average Length:** 39.64 characters
- **Top Values:**
  - `Champions (High Value, High Engagement)`: 1,119,991 occurrences
  - `Developing Customers (Moderate Activity)`: 2,002,379 occurrences

### preference_cluster_label
- **Unique Values:** 2
- **Average Length:** 27.83 characters
- **Top Values:**
  - `Consistent Style Followers`: 260,110 occurrences
  - `Moderate Preference Shoppers`: 2,862,260 occurrences

### hybrid_cluster_label
- **Unique Values:** 2
- **Average Length:** 20.47 characters
- **Top Values:**
  - `Diverse Style Seekers`: 2,844,424 occurrences
  - `Casual Shoppers`: 277,946 occurrences

### behavioural_cluster_label
- **Unique Values:** 1
- **Average Length:** 18.0 characters
- **Top Values:**
  - `Standard Customers`: 3,122,370 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 1155.55 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 11.9109 |
| customer_id | 190.5743 |
| article_id | 23.8218 |
| price | 23.8218 |
| sales_channel_id | 23.8218 |
| FN | 23.8218 |
| Active | 23.8218 |
| club_member_status | 11.9109 |
| fashion_news_frequency | 11.9109 |
| age | 23.8218 |
| postal_code | 11.9109 |
| recency | 23.8218 |
| frequency | 11.9109 |
| monetary | 23.8218 |
| purchase_diversity_score | 23.8218 |
| price_sensitivity_index | 23.8218 |
| colour_preference_entropy | 23.8218 |
| style_consistency_score | 23.8218 |
| created_by | 101.2426 |
| rfm_cluster | 11.9109 |
| preference_cluster | 11.9109 |
| hybrid_cluster | 11.9109 |
| behavioural_cluster | 11.9109 |
| rfm_cluster_label | 118.0409 |
| preference_cluster_label | 82.8802 |
| hybrid_cluster_label | 60.9418 |
| behavioural_cluster_label | 53.599 |
| product_type_name | 11.9109 |
| product_group_name | 11.9109 |
| graphical_appearance_name | 11.9109 |
| colour_group_name | 11.9109 |
| perceived_colour_value_name | 11.9109 |
| perceived_colour_master_name | 11.9109 |
| department_name | 11.9109 |
| index_name | 11.9109 |
| index_group_name | 11.9109 |
| section_name | 11.9109 |
| garment_group_name | 11.9109 |
| detail_desc | 11.9109 |
| bert_cluster | 12.2831 |

## 💡 Data Quality Recommendations
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** sales_channel_id, FN, Active, club_member_status, fashion_news_frequency, rfm_cluster, preference_cluster, hybrid_cluster, behavioural_cluster, rfm_cluster_label, preference_cluster_label, hybrid_cluster_label, perceived_colour_value_name, index_name, index_group_name - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*