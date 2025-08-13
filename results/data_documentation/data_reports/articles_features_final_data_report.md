# Data Understanding Report
**Generated on:** 2025-08-13 09:09:04
**File:** articles_features_final.parquet

## 📄 File Information
- **File Path:** `data/features/final/articles_features_final.parquet`
- **File Type:** PARQUET
- **File Size:** 0.46 MB
- **Last Modified:** 2025-08-13 09:08:56

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
| cluster_label | Int64 | 0 | 0.0% | 32 | 0.08% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| cluster_label | 42229 | 16.3208 | N/A | 0 | N/A | N/A | N/A | 31 |

## 📝 Categorical Column Analysis
### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Pumps`: 59 occurrences
  - `Wireless earphone case`: 2 occurrences
  - `Accessories set`: 6 occurrences
  - `Swimsuit`: 278 occurrences
  - `Blouse`: 1,774 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Garment Lower body`: 8,585 occurrences
  - `Garment and Shoe care`: 8 occurrences
  - `Cosmetic`: 13 occurrences
  - `Garment Full body`: 5,793 occurrences
  - `Fun`: 2 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Limited Edition`: 70 occurrences
  - `Trousers DS`: 36 occurrences
  - `Trouser S&T`: 73 occurrences
  - `Knitwear`: 1,252 occurrences
  - `Shorts DS`: 14 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Baby Girl`: 476 occurrences
  - `Womens Premium`: 486 occurrences
  - `Men Other 2`: 7 occurrences
  - `Mens Outerwear`: 222 occurrences
  - `Kids Outerwear`: 547 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Dresses/Skirts girls`: 418 occurrences
  - `Special Offers`: 336 occurrences
  - `Skirts`: 711 occurrences
  - `Shoes`: 1,904 occurrences
  - `Socks and Tights`: 947 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Dark Red`: 750 occurrences
  - `Purple`: 99 occurrences
  - `Dark Purple`: 87 occurrences
  - `Light Turquoise`: 292 occurrences
  - `Other Blue`: 22 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Front print`: 784 occurrences
  - `Other pattern`: 139 occurrences
  - `Mixed solid/pattern`: 413 occurrences
  - `Argyle`: 3 occurrences
  - `Neps`: 20 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 1.77 MB

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
| cluster_label | 0.3222 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** article_id - Verify if these should be used as identifiers

---
*Report generated using HnM Data Analytics - Data Understanding Module*