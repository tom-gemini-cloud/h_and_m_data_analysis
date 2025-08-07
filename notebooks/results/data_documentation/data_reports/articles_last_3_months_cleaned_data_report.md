# Data Understanding Report
**Generated on:** 2025-08-07 10:35:48
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `../data/cleaned/articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.83 MB
- **Last Modified:** 2025-08-07 10:35:47

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
  - `Brissie summer jogger`: 1 occurrences
  - `Mary Scarf`: 10 occurrences
  - `Stockholm shirt`: 1 occurrences
  - `Utah`: 3 occurrences
  - `Valetta Blouse.`: 2 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Leg warmers`: 1 occurrences
  - `Unknown`: 111 occurrences
  - `Baby Bib`: 3 occurrences
  - `Shoulder bag`: 2 occurrences
  - `Mobile case`: 4 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Accessories`: 4,179 occurrences
  - `Items`: 15 occurrences
  - `Garment Upper body`: 15,635 occurrences
  - `Swimwear`: 1,820 occurrences
  - `Fun`: 2 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Other structure`: 739 occurrences
  - `Chambray`: 101 occurrences
  - `Placement print`: 878 occurrences
  - `Denim`: 2,569 occurrences
  - `Solid`: 21,928 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Other Purple`: 21 occurrences
  - `Light Orange`: 623 occurrences
  - `Light Yellow`: 429 occurrences
  - `Turquoise`: 132 occurrences
  - `Pink`: 940 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Medium Dusty`: 5,777 occurrences
  - `Undefined`: 29 occurrences
  - `Dark`: 16,807 occurrences
  - `Bright`: 2,373 occurrences
  - `Unknown`: 5 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `Metal`: 1,023 occurrences
  - `Yellowish Green`: 5 occurrences
  - `Brown`: 1,083 occurrences
  - `undefined`: 29 occurrences
  - `Grey`: 2,892 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Woven top`: 344 occurrences
  - `Tops & Bottoms Other`: 4 occurrences
  - `Outwear`: 455 occurrences
  - `Tops Knitwear DS`: 31 occurrences
  - `Sunglasses`: 154 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `S`: 1,328 occurrences
  - `I`: 2,471 occurrences
  - `C`: 3,474 occurrences
  - `F`: 4,717 occurrences
  - `D`: 7,111 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Ladies Accessories`: 3,474 occurrences
  - `Lingeries/Tights`: 3,919 occurrences
  - `Children Sizes 134-170`: 2,471 occurrences
  - `Children Sizes 92-140`: 2,832 occurrences
  - `Baby Sizes 50-98`: 2,428 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Menswear`: 4,717 occurrences
  - `Divided`: 7,111 occurrences
  - `Sport`: 1,328 occurrences
  - `Baby/Children`: 8,887 occurrences
  - `Ladieswear`: 20,255 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Womens Everyday Basics`: 807 occurrences
  - `Baby Girl`: 476 occurrences
  - `Kids Local Relevance`: 23 occurrences
  - `Divided Asia keys`: 133 occurrences
  - `Womens Nightwear, Socks & Tigh`: 925 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Under-, Nightwear`: 3,214 occurrences
  - `Special Offers`: 336 occurrences
  - `Knitwear`: 2,417 occurrences
  - `Swimwear`: 1,683 occurrences
  - `Jersey Fancy`: 7,715 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Jacket in soft pile with a lined hood, zip down the front and front pockets. Lined.`: 1 occurrences
  - `Body in lace and mesh with narrow, adjustable shoulder straps that cross at the back, cups lined with mesh in a contrasting colour and an elasticated seam under the bust. Lined cups with press-studs.`: 1 occurrences
  - `T-shirt in soft cotton jersey with a print motif on the front and slits in the sides.`: 1 occurrences
  - `Ankle-length trousers in woven fabric with a high waist, pleats at the top, a zip fly and buttons, side pockets, and straight, wide legs.`: 1 occurrences
  - `Sports bra in fast-drying functional fabric with a lined front, racer back and wide elastic hem. Medium support.`: 2 occurrences

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