# Data Understanding Report
**Generated on:** 2025-08-09 11:49:01
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.81 MB
- **Last Modified:** 2025-08-09 11:48:57

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
  - `Venice melbourne`: 3 occurrences
  - `ALVA Hood`: 1 occurrences
  - `Mr Smith Coat`: 3 occurrences
  - `TD Minidots`: 1 occurrences
  - `LA-JS-W-AC BUCKET HAT`: 1 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Cross-body bag`: 5 occurrences
  - `Leg warmers`: 1 occurrences
  - `Gloves`: 93 occurrences
  - `Hat/beanie`: 308 occurrences
  - `Outdoor overall`: 24 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Unknown`: 111 occurrences
  - `Garment and Shoe care`: 8 occurrences
  - `Cosmetic`: 13 occurrences
  - `Nightwear`: 631 occurrences
  - `Accessories`: 4,179 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Treatment`: 160 occurrences
  - `Transparent`: 45 occurrences
  - `Chambray`: 101 occurrences
  - `All over pattern`: 6,351 occurrences
  - `Placement print`: 878 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Other Yellow`: 117 occurrences
  - `Purple`: 99 occurrences
  - `Light Green`: 303 occurrences
  - `Yellowish Brown`: 744 occurrences
  - `Other Green`: 71 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Dusty Light`: 9,135 occurrences
  - `Light`: 6,424 occurrences
  - `Medium Dusty`: 5,777 occurrences
  - `Undefined`: 29 occurrences
  - `Unknown`: 5 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `undefined`: 29 occurrences
  - `Metal`: 1,023 occurrences
  - `Turquoise`: 504 occurrences
  - `Green`: 1,339 occurrences
  - `Black`: 10,050 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Light Basic Jersey`: 355 occurrences
  - `Baby Boy Outdoor`: 62 occurrences
  - `Other items`: 135 occurrences
  - `Equatorial`: 2 occurrences
  - `Kids Girl Denim`: 125 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `J`: 1,156 occurrences
  - `D`: 7,111 occurrences
  - `H`: 2,832 occurrences
  - `B`: 3,919 occurrences
  - `C`: 3,474 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Ladies Accessories`: 3,474 occurrences
  - `Children Sizes 92-140`: 2,832 occurrences
  - `Divided`: 7,111 occurrences
  - `Menswear`: 4,717 occurrences
  - `Sport`: 1,328 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Divided`: 7,111 occurrences
  - `Sport`: 1,328 occurrences
  - `Ladieswear`: 20,255 occurrences
  - `Menswear`: 4,717 occurrences
  - `Baby/Children`: 8,887 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Womens Tailoring`: 1,805 occurrences
  - `Ladies Other`: 3 occurrences
  - `Womens Small accessories`: 1,693 occurrences
  - `EQ Divided`: 1 occurrences
  - `Divided Asia keys`: 133 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Trousers`: 3,132 occurrences
  - `Knitwear`: 2,417 occurrences
  - `Blouses`: 3,121 occurrences
  - `Jersey Fancy`: 7,715 occurrences
  - `Shoes`: 1,926 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Fitted top in soft jersey made from a cotton blend with short, voluminous puff sleeves in a cotton weave. Square neckline front and back and elasticated edges over the shoulders and around the sleeves.`: 4 occurrences
  - `Calf-length trousers in fast-drying functional fabric with a regular, elasticated drawstring waist, side pockets and straight, wide legs.`: 1 occurrences
  - `Trousers in a cotton weave. High paper bag waist with pleats at the front, covered elastication at the back and a tie belt. Zip fly with concealed hook-and-eye fasteners, front pockets and wide, gently tapered, loose-fitting legs with flap pockets.`: 2 occurrences
  - `Jacket in woven fabric with a ribbed stand-up collar, side pockets and ribbing at the cuffs and hem. Lined.`: 3 occurrences
  - `Trousers in washed, stretch twill. High waist with a detachable belt, zip fly with hook-and-eye fasteners, side pockets, back pockets and slim legs.`: 1 occurrences

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