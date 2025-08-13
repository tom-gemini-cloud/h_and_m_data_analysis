# Data Understanding Report
**Generated on:** 2025-08-13 09:32:44
**File:** articles_features_final.parquet

## 📄 File Information
- **File Path:** `data/features/final/articles_features_final.parquet`
- **File Type:** PARQUET
- **File Size:** 8.7 MB
- **Last Modified:** 2025-08-13 09:32:44

## 📊 Dataset Overview
- **Rows:** 42,298
- **Columns:** 29
- **Total Cells:** 1,226,642

## 🔍 Data Quality Summary
- **Completeness Score:** 99.99%
- **Missing Values:** 69 (0.01%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| article_id | Int64 | 0 | 0.0% | 42,298 | 100.0% |
| product_code | Int64 | 0 | 0.0% | 20,981 | 49.6% |
| prod_name | String | 0 | 0.0% | 21,219 | 50.17% |
| product_type_no | Int64 | 0 | 0.0% | 125 | 0.3% |
| product_type_name | Categorical(Categories("")) | 0 | 0.0% | 124 | 0.29% |
| product_group_name | Categorical(Categories("")) | 0 | 0.0% | 18 | 0.04% |
| graphical_appearance_no | Int64 | 0 | 0.0% | 30 | 0.07% |
| graphical_appearance_name | Categorical(Categories("")) | 0 | 0.0% | 30 | 0.07% |
| colour_group_code | Int64 | 0 | 0.0% | 50 | 0.12% |
| colour_group_name | Categorical(Categories("")) | 0 | 0.0% | 50 | 0.12% |
| perceived_colour_value_id | Int64 | 0 | 0.0% | 8 | 0.02% |
| perceived_colour_value_name | Categorical(Categories("")) | 0 | 0.0% | 8 | 0.02% |
| perceived_colour_master_id | Int64 | 0 | 0.0% | 20 | 0.05% |
| perceived_colour_master_name | Categorical(Categories("")) | 0 | 0.0% | 20 | 0.05% |
| department_no | Int64 | 0 | 0.0% | 286 | 0.68% |
| department_name | Categorical(Categories("")) | 0 | 0.0% | 238 | 0.56% |
| index_code | String | 0 | 0.0% | 10 | 0.02% |
| index_name | Categorical(Categories("")) | 0 | 0.0% | 10 | 0.02% |
| index_group_no | Int64 | 0 | 0.0% | 5 | 0.01% |
| index_group_name | Categorical(Categories("")) | 0 | 0.0% | 5 | 0.01% |
| section_no | Int64 | 0 | 0.0% | 56 | 0.13% |
| section_name | Categorical(Categories("")) | 0 | 0.0% | 56 | 0.13% |
| garment_group_no | Int64 | 0 | 0.0% | 21 | 0.05% |
| garment_group_name | Categorical(Categories("")) | 0 | 0.0% | 21 | 0.05% |
| detail_desc | Categorical(Categories("")) | 0 | 0.0% | 19,739 | 46.67% |
| product_type_no_negative_fixed | Boolean | 0 | 0.0% | 2 | 0.0% |
| graphical_appearance_no_negative_fixed | Boolean | 0 | 0.0% | 2 | 0.0% |
| product_code_invalid | Boolean | 0 | 0.0% | 1 | 0.0% |
| bert_cluster | Int64 | 69 | 0.16% | 33 | 0.08% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| product_code | 42298 | 767829.3654 | N/A | 108775 | N/A | N/A | N/A | 956217 |
| product_type_no | 42298 | 237.0751 | N/A | 0 | N/A | N/A | N/A | 762 |
| graphical_appearance_no | 42298 | 1009869.993 | N/A | 0 | N/A | N/A | N/A | 1010029 |
| colour_group_code | 42298 | 29.7211 | N/A | -1 | N/A | N/A | N/A | 93 |
| department_no | 42298 | 3936.5935 | N/A | 1201 | N/A | N/A | N/A | 9989 |
| index_group_no | 42298 | 2.8064 | N/A | 1 | N/A | N/A | N/A | 26 |
| section_no | 42298 | 40.15 | N/A | 2 | N/A | N/A | N/A | 97 |
| garment_group_no | 42298 | 1010.9849 | N/A | 1001 | N/A | N/A | N/A | 1025 |
| bert_cluster | 42229 | 16.3208 | N/A | 0 | N/A | N/A | N/A | 31 |

## 📝 Categorical Column Analysis
### prod_name
- **Unique Values:** 21,219
- **Average Length:** 15.97 characters
- **Top Values:**
  - `Mom Fit Trash`: 4 occurrences
  - `Portofino`: 2 occurrences
  - `ANNA-LENA buckethat`: 1 occurrences
  - `DORA COTTON PUFF SHIRT`: 1 occurrences
  - `AMAZON LONG JUMPSUIT`: 2 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `A`: 12,862 occurrences
  - `B`: 3,919 occurrences
  - `S`: 1,328 occurrences
  - `H`: 2,832 occurrences
  - `F`: 4,717 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 6.51 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| article_id | 0.3227 |
| product_code | 0.3227 |
| prod_name | 0.6443 |
| product_type_no | 0.3227 |
| product_type_name | 0.1614 |
| product_group_name | 0.1614 |
| graphical_appearance_no | 0.3227 |
| graphical_appearance_name | 0.1614 |
| colour_group_code | 0.3227 |
| colour_group_name | 0.1614 |
| perceived_colour_value_id | 0.3227 |
| perceived_colour_value_name | 0.1614 |
| perceived_colour_master_id | 0.3227 |
| perceived_colour_master_name | 0.1614 |
| department_no | 0.3227 |
| department_name | 0.1614 |
| index_code | 0.0403 |
| index_name | 0.1614 |
| index_group_no | 0.3227 |
| index_group_name | 0.1614 |
| section_no | 0.3227 |
| section_name | 0.1614 |
| garment_group_no | 0.3227 |
| garment_group_name | 0.1614 |
| detail_desc | 0.1614 |
| product_type_no_negative_fixed | 0.0051 |
| graphical_appearance_no_negative_fixed | 0.0051 |
| product_code_invalid | 0.0051 |
| bert_cluster | 0.3278 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** article_id - Verify if these should be used as identifiers
- **Low cardinality columns:** perceived_colour_value_id, perceived_colour_value_name, index_code, index_name, index_group_no, index_group_name, product_type_no_negative_fixed, graphical_appearance_no_negative_fixed - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*