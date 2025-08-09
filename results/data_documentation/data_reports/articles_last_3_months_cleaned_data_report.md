# Data Understanding Report
**Generated on:** 2025-08-09 13:02:46
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.8 MB
- **Last Modified:** 2025-08-09 13:02:42

## 📊 Dataset Overview
- **Rows:** 42,298
- **Columns:** 30
- **Total Cells:** 1,268,940

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| article_id | Int64 | 0 | 0.0% | 42,298 | 100.0% |
| product_code | Int64 | 0 | 0.0% | 20,517 | 48.51% |
| prod_name | String | 0 | 0.0% | 21,219 | 50.17% |
| product_type_no | Int64 | 0 | 0.0% | 84 | 0.2% |
| product_type_name | Categorical | 0 | 0.0% | 124 | 0.29% |
| product_group_name | Categorical | 0 | 0.0% | 18 | 0.04% |
| graphical_appearance_no | Int64 | 0 | 0.0% | 2 | 0.0% |
| graphical_appearance_name | Categorical | 0 | 0.0% | 30 | 0.07% |
| colour_group_code | Int64 | 0 | 0.0% | 50 | 0.12% |
| colour_group_name | Categorical | 0 | 0.0% | 50 | 0.12% |
| perceived_colour_value_id | Int64 | 0 | 0.0% | 8 | 0.02% |
| perceived_colour_value_name | Categorical | 0 | 0.0% | 8 | 0.02% |
| perceived_colour_master_id | Int64 | 0 | 0.0% | 20 | 0.05% |
| perceived_colour_master_name | Categorical | 0 | 0.0% | 20 | 0.05% |
| department_no | Int64 | 0 | 0.0% | 286 | 0.68% |
| department_name | Categorical | 0 | 0.0% | 238 | 0.56% |
| index_code | String | 0 | 0.0% | 10 | 0.02% |
| index_name | Categorical | 0 | 0.0% | 10 | 0.02% |
| index_group_no | Int64 | 0 | 0.0% | 5 | 0.01% |
| index_group_name | Categorical | 0 | 0.0% | 5 | 0.01% |
| section_no | Int64 | 0 | 0.0% | 56 | 0.13% |
| section_name | Categorical | 0 | 0.0% | 56 | 0.13% |
| garment_group_no | Int64 | 0 | 0.0% | 21 | 0.05% |
| garment_group_name | Categorical | 0 | 0.0% | 21 | 0.05% |
| detail_desc | Categorical | 0 | 0.0% | 19,739 | 46.67% |
| product_type_no_outlier_capped | Boolean | 0 | 0.0% | 2 | 0.0% |
| product_code_outlier_capped | Boolean | 0 | 0.0% | 2 | 0.0% |
| graphical_appearance_no_outlier_capped | Boolean | 0 | 0.0% | 1 | 0.0% |
| index_group_no_outlier_capped | Boolean | 0 | 0.0% | 1 | 0.0% |
| product_code_invalid | Boolean | 0 | 0.0% | 1 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| article_id | 42298 | 767829371.9367 | N/A | 108775015 | N/A | N/A | N/A | 956217002 |
| product_code | 42298 | 771537.1165 | N/A | 485308 | N/A | N/A | N/A | 956217 |
| product_type_no | 42298 | 235.7421 | N/A | 1 | N/A | N/A | N/A | 300 |
| graphical_appearance_no | 42298 | 99.986 | N/A | 1 | N/A | N/A | N/A | 100 |
| colour_group_code | 42298 | 29.7211 | N/A | -1 | N/A | N/A | N/A | 93 |
| perceived_colour_value_id | 42298 | 3.1079 | N/A | -1 | N/A | N/A | N/A | 7 |
| perceived_colour_master_id | 42298 | 7.7332 | N/A | -1 | N/A | N/A | N/A | 20 |
| department_no | 42298 | 3936.5935 | N/A | 1201 | N/A | N/A | N/A | 9989 |
| index_group_no | 42298 | 2.8064 | N/A | 1 | N/A | N/A | N/A | 26 |
| section_no | 42298 | 40.15 | N/A | 2 | N/A | N/A | N/A | 97 |
| garment_group_no | 42298 | 1010.9849 | N/A | 1001 | N/A | N/A | N/A | 1025 |

## 📝 Categorical Column Analysis
### prod_name
- **Unique Values:** 21,219
- **Average Length:** 15.97 characters
- **Top Values:**
  - `Dawna dress`: 2 occurrences
  - `Mona waistbelt`: 2 occurrences
  - `CHEERY SKIRT S.0`: 2 occurrences
  - `Portofino dress`: 1 occurrences
  - `5pk regular`: 1 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Hat/beanie`: 308 occurrences
  - `Costumes`: 33 occurrences
  - `Marker pen`: 4 occurrences
  - `Outdoor Waistcoat`: 43 occurrences
  - `Vest top`: 1,412 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Furniture`: 1 occurrences
  - `Items`: 15 occurrences
  - `Stationery`: 4 occurrences
  - `Socks & Tights`: 1,005 occurrences
  - `Cosmetic`: 13 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Lace`: 557 occurrences
  - `Argyle`: 3 occurrences
  - `Metallic`: 147 occurrences
  - `Chambray`: 101 occurrences
  - `Dot`: 305 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Turquoise`: 132 occurrences
  - `Other Red`: 34 occurrences
  - `Other Green`: 71 occurrences
  - `Red`: 754 occurrences
  - `Other Pink`: 218 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Undefined`: 29 occurrences
  - `Dusty Light`: 9,135 occurrences
  - `Light`: 6,424 occurrences
  - `Bright`: 2,373 occurrences
  - `Dark`: 16,807 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `Beige`: 2,972 occurrences
  - `Grey`: 2,892 occurrences
  - `Green`: 1,339 occurrences
  - `Blue`: 6,343 occurrences
  - `Metal`: 1,023 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Boots`: 185 occurrences
  - `Equatorial Assortment`: 48 occurrences
  - `Outdoor/Blazers`: 311 occurrences
  - `Bottoms Girls`: 54 occurrences
  - `Basics`: 19 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `J`: 1,156 occurrences
  - `I`: 2,471 occurrences
  - `C`: 3,474 occurrences
  - `H`: 2,832 occurrences
  - `B`: 3,919 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Baby Sizes 50-98`: 2,428 occurrences
  - `Ladieswear`: 12,862 occurrences
  - `Divided`: 7,111 occurrences
  - `Sport`: 1,328 occurrences
  - `Children Sizes 134-170`: 2,471 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Baby/Children`: 8,887 occurrences
  - `Ladieswear`: 20,255 occurrences
  - `Divided`: 7,111 occurrences
  - `Sport`: 1,328 occurrences
  - `Menswear`: 4,717 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Womens Jackets`: 392 occurrences
  - `Womens Trend`: 1,216 occurrences
  - `Womens Tailoring`: 1,805 occurrences
  - `Divided Collection`: 3,489 occurrences
  - `Men Other`: 24 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Shirts`: 748 occurrences
  - `Dresses/Skirts girls`: 418 occurrences
  - `Jersey Basic`: 3,185 occurrences
  - `Under-, Nightwear`: 3,214 occurrences
  - `Dresses Ladies`: 2,513 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Top in soft slub cotton jersey with a heart-shaped chiffon appliqué on the front and long puff sleeves.`: 1 occurrences
  - `Trousers woven in a wool blend with an extended waistband and concealed hook-and-eye fastening. Pockets in the side seams, a welt back pocket and straight, wide legs with creases and visible seams at the back.`: 1 occurrences
  - `Knee-length dress in lightweight, airy Tencel™ lyocell denim with a V-neck and short puff sleeves. Gathered elastication at the top and down the sleeves, a seam under the bust, concealed elastication at the back of the waist and a flared skirt. Unlined.`: 1 occurrences
  - `Jumper in a soft, fine-knit viscose blend with buttons on one shoulder, 3/4-length sleeves and roll edges around the neckline, cuffs and hem.`: 2 occurrences
  - `Pile-lined jacket in imitation suede with raw edges. Collar, diagonal zip down the front, zipped side pockets and a zip at the cuffs.`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 6.2 MB

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
| product_type_no_outlier_capped | 0.0051 |
| product_code_outlier_capped | 0.0051 |
| graphical_appearance_no_outlier_capped | 0.0051 |
| index_group_no_outlier_capped | 0.0051 |
| product_code_invalid | 0.0051 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** article_id - Verify if these should be used as identifiers
- **Low cardinality columns:** graphical_appearance_no, perceived_colour_value_id, perceived_colour_value_name, index_code, index_name, index_group_no, index_group_name, product_type_no_outlier_capped, product_code_outlier_capped - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*