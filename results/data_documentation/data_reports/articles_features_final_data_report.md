# Data Understanding Report
**Generated on:** 2025-08-12 21:36:35
**File:** articles_features_final.parquet

## 📄 File Information
- **File Path:** `data\features\final\articles_features_final.parquet`
- **File Type:** PARQUET
- **File Size:** 0.46 MB
- **Last Modified:** 2025-08-12 21:36:35

## 📊 Dataset Overview
- **Rows:** 42,229
- **Columns:** 9
- **Total Cells:** 380,061

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| article_id | Int64 | 0 | 0.0% | 42,229 | 100.0% |
| product_type_name | Categorical | 0 | 0.0% | 124 | 0.29% |
| product_group_name | Categorical | 0 | 0.0% | 18 | 0.04% |
| department_name | Categorical | 0 | 0.0% | 238 | 0.56% |
| section_name | Categorical | 0 | 0.0% | 56 | 0.13% |
| garment_group_name | Categorical | 0 | 0.0% | 21 | 0.05% |
| colour_group_name | Categorical | 0 | 0.0% | 50 | 0.12% |
| graphical_appearance_name | Categorical | 0 | 0.0% | 30 | 0.07% |
| cluster_label | Int32 | 0 | 0.0% | 30 | 0.07% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| cluster_label | 42229 | 12.7912 | N/A | 0 | N/A | N/A | N/A | 29 |

## 📝 Categorical Column Analysis
### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Ballerinas`: 132 occurrences
  - `Blazer`: 463 occurrences
  - `Hair/alice band`: 384 occurrences
  - `Pyjama jumpsuit/playsuit`: 106 occurrences
  - `Underwear set`: 22 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Underwear`: 2,491 occurrences
  - `Shoes`: 1,925 occurrences
  - `Swimwear`: 1,813 occurrences
  - `Furniture`: 1 occurrences
  - `Fun`: 2 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Basic 1`: 701 occurrences
  - `Baby Shoes`: 147 occurrences
  - `Clean Lingerie`: 198 occurrences
  - `Hair Accessories`: 447 occurrences
  - `Kids Boy UW/NW`: 89 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Men Suits & Tailoring`: 572 occurrences
  - `H&M+`: 1,078 occurrences
  - `Men Other`: 24 occurrences
  - `Womens Small accessories`: 1,692 occurrences
  - `Divided Basics`: 872 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Shoes`: 1,904 occurrences
  - `Accessories`: 4,332 occurrences
  - `Socks and Tights`: 947 occurrences
  - `Outdoor`: 1,550 occurrences
  - `Jersey Fancy`: 7,708 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Orange`: 338 occurrences
  - `Grey`: 1,359 occurrences
  - `Light Beige`: 1,678 occurrences
  - `Other Turquoise`: 3 occurrences
  - `White`: 4,110 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Slub`: 46 occurrences
  - `Metallic`: 146 occurrences
  - `Placement print`: 876 occurrences
  - `Lace`: 554 occurrences
  - `Front print`: 784 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 1.61 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| article_id | 0.3222 |
| product_type_name | 0.1611 |
| product_group_name | 0.1611 |
| department_name | 0.1611 |
| section_name | 0.1611 |
| garment_group_name | 0.1611 |
| colour_group_name | 0.1611 |
| graphical_appearance_name | 0.1611 |
| cluster_label | 0.1611 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** article_id - Verify if these should be used as identifiers

---
*Report generated using HnM Data Analytics - Data Understanding Module*