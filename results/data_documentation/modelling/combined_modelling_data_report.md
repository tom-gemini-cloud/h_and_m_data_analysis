# Data Understanding Report
**Generated on:** 2025-08-15 12:59:42
**File:** combined_modelling_data.parquet

## 📄 File Information
- **File Path:** `c:\Users\tom\coding_projects\data_analytics_projects\h_and_m_data_analysis\notebooks\..\data\modelling_data\combined_modelling_data.parquet`
- **File Type:** PARQUET
- **File Size:** 2015.32 MB
- **Last Modified:** 2025-08-15 12:59:31

## 📊 Dataset Overview
- **Rows:** 3,904,391
- **Columns:** 40
- **Total Cells:** 156,175,640

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
| purchase_diversity_score | Float64 | 0 | 0.0% | 21,386 | 0.55% |
| price_sensitivity_index | Float64 | 0 | 0.0% | 269,264 | 6.9% |
| colour_preference_entropy | Float64 | 0 | 0.0% | 24,257 | 0.62% |
| style_consistency_score | Float64 | 0 | 0.0% | 26,861 | 0.69% |
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
| detail_desc | Categorical(Categories("")) | 0 | 0.0% | 19,739 | 0.51% |
| bert_cluster | Int32 | 2,460 | 0.06% | 33 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| price | 3904391 | 26.8386 | N/A | 2.39 | N/A | N/A | N/A | 149.99 |
| FN | 3904391 | 0.4506 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| Active | 3904391 | 0.4441 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| age | 3904391 | 35.0048 | N/A | 16.0 | N/A | N/A | N/A | 99.0 |
| recency | 3904391 | 30.1863 | N/A | 1 | N/A | N/A | N/A | 91 |
| monetary | 3904391 | 508.6834 | N/A | 2.39 | N/A | N/A | N/A | 19342.120000000024 |
| purchase_diversity_score | 3904391 | 1.4317 | N/A | -0.0 | N/A | N/A | N/A | 3.1395722619867232 |
| price_sensitivity_index | 3904391 | 0.633 | N/A | 0.0 | N/A | N/A | N/A | 2.7934880166020273 |
| colour_preference_entropy | 3904391 | 2.1974 | N/A | -0.0 | N/A | N/A | N/A | 4.747015200541309 |
| style_consistency_score | 3904391 | 0.1858 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| rfm_cluster | 3904391 | 0.3591 | N/A | 0 | N/A | N/A | N/A | 1 |
| preference_cluster | 3904391 | 0.9167 | N/A | 0 | N/A | N/A | N/A | 1 |
| hybrid_cluster | 3904391 | 0.089 | N/A | 0 | N/A | N/A | N/A | 1 |
| behavioural_cluster | 3904391 | 1.5117 | N/A | 0 | N/A | N/A | N/A | 5 |
| bert_cluster | 3901931 | 15.3364 | N/A | 0 | N/A | N/A | N/A | 31 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `43a0e83b2fc76fc020fff0063610c1a8b841cd2626776d268f60af26394c71a8`: 2 occurrences
  - `729cb04f181f230879aa3bd3c5ff65ada61298fa2e1ec4a3fc32558f779b431d`: 9 occurrences
  - `879fed9c416e11cba9b77935e4f4de52a48301a863e3376c31f41ada2534c46b`: 4 occurrences
  - `5ee0bef969ee86e6f5ed7a02a0d7423a81d6a3e4644f03eab3876085cc007334`: 11 occurrences
  - `348ca71f6fe303d1f995f82446b3ec5a3acb84d889a1f21794ae20f6ccadfc0d`: 1 occurrences

### created_by
- **Unique Values:** 1
- **Average Length:** 34.0 characters
- **Top Values:**
  - `customer_feature_engineering.ipynb`: 3,904,391 occurrences

### rfm_cluster_label
- **Unique Values:** 2
- **Average Length:** 39.64 characters
- **Top Values:**
  - `Developing Customers (Moderate Activity)`: 2,502,162 occurrences
  - `Champions (High Value, High Engagement)`: 1,402,229 occurrences

### preference_cluster_label
- **Unique Values:** 2
- **Average Length:** 27.83 characters
- **Top Values:**
  - `Moderate Preference Shoppers`: 3,579,175 occurrences
  - `Consistent Style Followers`: 325,216 occurrences

### hybrid_cluster_label
- **Unique Values:** 2
- **Average Length:** 20.47 characters
- **Top Values:**
  - `Diverse Style Seekers`: 3,556,839 occurrences
  - `Casual Shoppers`: 347,552 occurrences

### behavioural_cluster_label
- **Unique Values:** 1
- **Average Length:** 18.0 characters
- **Top Values:**
  - `Standard Customers`: 3,904,391 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 1444.97 MB

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
| rfm_cluster | 14.8941 |
| preference_cluster | 14.8941 |
| hybrid_cluster | 14.8941 |
| behavioural_cluster | 14.8941 |
| rfm_cluster_label | 147.6034 |
| preference_cluster_label | 103.6382 |
| hybrid_cluster_label | 76.2052 |
| behavioural_cluster_label | 67.0233 |
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
| bert_cluster | 15.3595 |

## 💡 Data Quality Recommendations
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** sales_channel_id, FN, Active, club_member_status, fashion_news_frequency, rfm_cluster, preference_cluster, hybrid_cluster, behavioural_cluster, rfm_cluster_label, preference_cluster_label, hybrid_cluster_label, perceived_colour_value_name, index_name, index_group_name - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*