# Data Understanding Report
**Generated on:** 2025-08-13 10:47:46
**File:** articles_features_final.parquet

## 📄 File Information
- **File Path:** `data\features\final\articles_features_final.parquet`
- **File Type:** PARQUET
- **File Size:** 8.07 MB
- **Last Modified:** 2025-08-13 10:47:46

## 📊 Dataset Overview
- **Rows:** 42,298
- **Columns:** 14
- **Total Cells:** 592,172

## 🔍 Data Quality Summary
- **Completeness Score:** 99.99%
- **Missing Values:** 69 (0.01%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| article_id | Int64 | 0 | 0.0% | 42,298 | 100.0% |
| product_type_name | Categorical(Categories("")) | 0 | 0.0% | 124 | 0.29% |
| product_group_name | Categorical(Categories("")) | 0 | 0.0% | 18 | 0.04% |
| graphical_appearance_name | Categorical(Categories("")) | 0 | 0.0% | 30 | 0.07% |
| colour_group_name | Categorical(Categories("")) | 0 | 0.0% | 50 | 0.12% |
| perceived_colour_value_name | Categorical(Categories("")) | 0 | 0.0% | 8 | 0.02% |
| perceived_colour_master_name | Categorical(Categories("")) | 0 | 0.0% | 20 | 0.05% |
| department_name | Categorical(Categories("")) | 0 | 0.0% | 238 | 0.56% |
| index_name | Categorical(Categories("")) | 0 | 0.0% | 10 | 0.02% |
| index_group_name | Categorical(Categories("")) | 0 | 0.0% | 5 | 0.01% |
| section_name | Categorical(Categories("")) | 0 | 0.0% | 56 | 0.13% |
| garment_group_name | Categorical(Categories("")) | 0 | 0.0% | 21 | 0.05% |
| detail_desc | Categorical(Categories("")) | 0 | 0.0% | 19,739 | 46.67% |
| bert_cluster | Int32 | 69 | 0.16% | 33 | 0.08% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| bert_cluster | 42229 | 15.3813 | N/A | 0 | N/A | N/A | N/A | 31 |

## 💾 Memory Usage
- **Estimated Total Memory:** 2.43 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| article_id | 0.3227 |
| product_type_name | 0.1614 |
| product_group_name | 0.1614 |
| graphical_appearance_name | 0.1614 |
| colour_group_name | 0.1614 |
| perceived_colour_value_name | 0.1614 |
| perceived_colour_master_name | 0.1614 |
| department_name | 0.1614 |
| index_name | 0.1614 |
| index_group_name | 0.1614 |
| section_name | 0.1614 |
| garment_group_name | 0.1614 |
| detail_desc | 0.1614 |
| bert_cluster | 0.1664 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** article_id - Verify if these should be used as identifiers
- **Low cardinality columns:** perceived_colour_value_name, index_name, index_group_name - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*