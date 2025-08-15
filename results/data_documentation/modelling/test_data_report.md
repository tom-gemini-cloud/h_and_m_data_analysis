# Data Understanding Report
**Generated on:** 2025-08-15 14:03:25
**File:** test_data.parquet

## 📄 File Information
- **File Path:** `data\modelling_data\test_data.parquet`
- **File Type:** PARQUET
- **File Size:** 428.05 MB
- **Last Modified:** 2025-08-15 14:00:35

## 📊 Dataset Overview
- **Rows:** 782,021
- **Columns:** 40
- **Total Cells:** 31,280,840

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 491 (0.0%)
- **Duplicate Rows:** 65,709 (8.4%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | Date | 0 | 0.0% | 91 | 0.01% |
| customer_id | String | 0 | 0.0% | 105,015 | 13.43% |
| article_id | Int64 | 0 | 0.0% | 31,227 | 3.99% |
| price | Float64 | 0 | 0.0% | 2,826 | 0.36% |
| sales_channel_id | Int64 | 0 | 0.0% | 2 | 0.0% |
| FN | Float64 | 0 | 0.0% | 2 | 0.0% |
| Active | Float64 | 0 | 0.0% | 2 | 0.0% |
| club_member_status | Categorical(Categories("")) | 0 | 0.0% | 4 | 0.0% |
| fashion_news_frequency | Categorical(Categories("")) | 0 | 0.0% | 3 | 0.0% |
| age | Float64 | 0 | 0.0% | 75 | 0.01% |
| postal_code | Categorical(Categories("")) | 0 | 0.0% | 82,914 | 10.6% |
| recency | Int64 | 0 | 0.0% | 91 | 0.01% |
| frequency | UInt32 | 0 | 0.0% | 147 | 0.02% |
| monetary | Float64 | 0 | 0.0% | 45,838 | 5.86% |
| purchase_diversity_score | Float64 | 0 | 0.0% | 7,126 | 0.91% |
| price_sensitivity_index | Float64 | 0 | 0.0% | 61,239 | 7.83% |
| colour_preference_entropy | Float64 | 0 | 0.0% | 7,833 | 1.0% |
| style_consistency_score | Float64 | 0 | 0.0% | 8,454 | 1.08% |
| created_by | String | 0 | 0.0% | 1 | 0.0% |
| rfm_cluster | Int32 | 0 | 0.0% | 2 | 0.0% |
| preference_cluster | Int32 | 0 | 0.0% | 2 | 0.0% |
| hybrid_cluster | Int32 | 0 | 0.0% | 2 | 0.0% |
| behavioural_cluster | Int32 | 0 | 0.0% | 6 | 0.0% |
| rfm_cluster_label | String | 0 | 0.0% | 2 | 0.0% |
| preference_cluster_label | String | 0 | 0.0% | 2 | 0.0% |
| hybrid_cluster_label | String | 0 | 0.0% | 2 | 0.0% |
| behavioural_cluster_label | String | 0 | 0.0% | 1 | 0.0% |
| product_type_name | Categorical(Categories("")) | 0 | 0.0% | 120 | 0.02% |
| product_group_name | Categorical(Categories("")) | 0 | 0.0% | 18 | 0.0% |
| graphical_appearance_name | Categorical(Categories("")) | 0 | 0.0% | 30 | 0.0% |
| colour_group_name | Categorical(Categories("")) | 0 | 0.0% | 50 | 0.01% |
| perceived_colour_value_name | Categorical(Categories("")) | 0 | 0.0% | 8 | 0.0% |
| perceived_colour_master_name | Categorical(Categories("")) | 0 | 0.0% | 20 | 0.0% |
| department_name | Categorical(Categories("")) | 0 | 0.0% | 231 | 0.03% |
| index_name | Categorical(Categories("")) | 0 | 0.0% | 10 | 0.0% |
| index_group_name | Categorical(Categories("")) | 0 | 0.0% | 5 | 0.0% |
| section_name | Categorical(Categories("")) | 0 | 0.0% | 55 | 0.01% |
| garment_group_name | Categorical(Categories("")) | 0 | 0.0% | 21 | 0.0% |
| detail_desc | Categorical(Categories("")) | 0 | 0.0% | 15,180 | 1.94% |
| bert_cluster | Int32 | 491 | 0.06% | 33 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| price | 782021 | 26.8122 | N/A | 2.39 | N/A | N/A | N/A | 149.99 |
| FN | 782021 | 0.451 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| Active | 782021 | 0.4441 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| age | 782021 | 35.0036 | N/A | 16.0 | N/A | N/A | N/A | 95.0 |
| recency | 782021 | 30.1587 | N/A | 1 | N/A | N/A | N/A | 91 |
| monetary | 782021 | 505.4255 | N/A | 2.39 | N/A | N/A | N/A | 11454.55999999998 |
| purchase_diversity_score | 782021 | 1.4302 | N/A | -0.0 | N/A | N/A | N/A | 3.084962500721156 |
| price_sensitivity_index | 782021 | 0.6317 | N/A | 0.0 | N/A | N/A | N/A | 2.2251065144475626 |
| colour_preference_entropy | 782021 | 2.1947 | N/A | -0.0 | N/A | N/A | N/A | 4.29980772416735 |
| style_consistency_score | 782021 | 0.1859 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| rfm_cluster | 782021 | 0.3609 | N/A | 0 | N/A | N/A | N/A | 1 |
| preference_cluster | 782021 | 0.9167 | N/A | 0 | N/A | N/A | N/A | 1 |
| hybrid_cluster | 782021 | 0.089 | N/A | 0 | N/A | N/A | N/A | 1 |
| behavioural_cluster | 782021 | 1.5117 | N/A | 0 | N/A | N/A | N/A | 5 |
| bert_cluster | 781530 | 15.3399 | N/A | 0 | N/A | N/A | N/A | 31 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 105,015
- **Average Length:** 64.0 characters
- **Top Values:**
  - `301155215979eaef93f09d6a2a55f520f330dc35477fd461c2e47443ecc93110`: 14 occurrences
  - `50763936900a7797738d7ed8e3079b2b59fc8c8f39501d8e3e73bcdd1dbf06d8`: 16 occurrences
  - `400210521e975bcfb70e91c7f250fb762bc60734e73bbe307259f56eb85d56fe`: 1 occurrences
  - `d0355b32e75d8cbc9ea9f526738d9a27ad36aeddd694e9a35a73d1c8e495b946`: 5 occurrences
  - `e6a644f0c47570c8a3efae35261158739e472a98e9ab9b2747a9821c20a489e9`: 21 occurrences

### created_by
- **Unique Values:** 1
- **Average Length:** 34.0 characters
- **Top Values:**
  - `customer_feature_engineering.ipynb`: 782,021 occurrences

### rfm_cluster_label
- **Unique Values:** 2
- **Average Length:** 39.64 characters
- **Top Values:**
  - `Champions (High Value, High Engagement)`: 282,238 occurrences
  - `Developing Customers (Moderate Activity)`: 499,783 occurrences

### preference_cluster_label
- **Unique Values:** 2
- **Average Length:** 27.83 characters
- **Top Values:**
  - `Moderate Preference Shoppers`: 716,915 occurrences
  - `Consistent Style Followers`: 65,106 occurrences

### hybrid_cluster_label
- **Unique Values:** 2
- **Average Length:** 20.47 characters
- **Top Values:**
  - `Diverse Style Seekers`: 712,415 occurrences
  - `Casual Shoppers`: 69,606 occurrences

### behavioural_cluster_label
- **Unique Values:** 1
- **Average Length:** 18.0 characters
- **Top Values:**
  - `Standard Customers`: 782,021 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 289.42 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 2.9832 |
| customer_id | 47.7308 |
| article_id | 5.9663 |
| price | 5.9663 |
| sales_channel_id | 5.9663 |
| FN | 5.9663 |
| Active | 5.9663 |
| club_member_status | 2.9832 |
| fashion_news_frequency | 2.9832 |
| age | 5.9663 |
| postal_code | 2.9832 |
| recency | 5.9663 |
| frequency | 2.9832 |
| monetary | 5.9663 |
| purchase_diversity_score | 5.9663 |
| price_sensitivity_index | 5.9663 |
| colour_preference_entropy | 5.9663 |
| style_consistency_score | 5.9663 |
| created_by | 25.357 |
| rfm_cluster | 2.9832 |
| preference_cluster | 2.9832 |
| hybrid_cluster | 2.9832 |
| behavioural_cluster | 2.9832 |
| rfm_cluster_label | 29.5626 |
| preference_cluster_label | 20.758 |
| hybrid_cluster_label | 15.2634 |
| behavioural_cluster_label | 13.4243 |
| product_type_name | 2.9832 |
| product_group_name | 2.9832 |
| graphical_appearance_name | 2.9832 |
| colour_group_name | 2.9832 |
| perceived_colour_value_name | 2.9832 |
| perceived_colour_master_name | 2.9832 |
| department_name | 2.9832 |
| index_name | 2.9832 |
| index_group_name | 2.9832 |
| section_name | 2.9832 |
| garment_group_name | 2.9832 |
| detail_desc | 2.9832 |
| bert_cluster | 3.0764 |

## 💡 Data Quality Recommendations
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** sales_channel_id, FN, Active, club_member_status, fashion_news_frequency, rfm_cluster, preference_cluster, hybrid_cluster, behavioural_cluster, rfm_cluster_label, preference_cluster_label, hybrid_cluster_label, perceived_colour_value_name, index_name, index_group_name - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*