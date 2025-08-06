# Data Understanding Report
**Generated on:** 2025-08-06 13:47:25
**File:** articles_last_3_months.parquet

## 📄 File Information
- **File Path:** `..\data\processed\articles_last_3_months.parquet`
- **File Type:** PARQUET
- **File Size:** 1.5 MB
- **Last Modified:** 2025-08-05 13:24:29

## 📊 Dataset Overview
- **Rows:** 42,298
- **Columns:** 25
- **Total Cells:** 1,057,450

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
| product_type_name | String | 0 | 0.0% | 124 | 0.29% |
| product_group_name | String | 0 | 0.0% | 18 | 0.04% |
| graphical_appearance_no | Int64 | 0 | 0.0% | 30 | 0.07% |
| graphical_appearance_name | String | 0 | 0.0% | 30 | 0.07% |
| colour_group_code | Int64 | 0 | 0.0% | 50 | 0.12% |
| colour_group_name | String | 0 | 0.0% | 50 | 0.12% |
| perceived_colour_value_id | Int64 | 0 | 0.0% | 8 | 0.02% |
| perceived_colour_value_name | String | 0 | 0.0% | 8 | 0.02% |
| perceived_colour_master_id | Int64 | 0 | 0.0% | 20 | 0.05% |
| perceived_colour_master_name | String | 0 | 0.0% | 20 | 0.05% |
| department_no | Int64 | 0 | 0.0% | 286 | 0.68% |
| department_name | String | 0 | 0.0% | 238 | 0.56% |
| index_code | String | 0 | 0.0% | 10 | 0.02% |
| index_name | String | 0 | 0.0% | 10 | 0.02% |
| index_group_no | Int64 | 0 | 0.0% | 5 | 0.01% |
| index_group_name | String | 0 | 0.0% | 5 | 0.01% |
| section_no | Int64 | 0 | 0.0% | 56 | 0.13% |
| section_name | String | 0 | 0.0% | 56 | 0.13% |
| garment_group_no | Int64 | 0 | 0.0% | 21 | 0.05% |
| garment_group_name | String | 0 | 0.0% | 21 | 0.05% |
| detail_desc | String | 69 | 0.16% | 19,739 | 46.67% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| article_id | 42298 | 767829371.9367 | N/A | 108775015 | N/A | N/A | N/A | 956217002 |
| product_code | 42298 | 767829.3654 | N/A | 108775 | N/A | N/A | N/A | 956217 |
| product_type_no | 42298 | 237.0724 | N/A | -1 | N/A | N/A | N/A | 762 |
| graphical_appearance_no | 42298 | 1009869.9929 | N/A | -1 | N/A | N/A | N/A | 1010029 |
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
  - `Apollo barell leg trouser`: 3 occurrences
  - `Detroit sweater`: 6 occurrences
  - `Tank sweater Fast buy`: 1 occurrences
  - `2P Fearow Click Clack`: 1 occurrences
  - `COLAB C.KIJAK ESA TEE`: 3 occurrences

### product_type_name
- **Unique Values:** 124
- **Average Length:** 7.46 characters
- **Top Values:**
  - `Night gown`: 60 occurrences
  - `Long John`: 11 occurrences
  - `Dress`: 4,863 occurrences
  - `Hair ties`: 24 occurrences
  - `Earrings`: 11 occurrences

### product_group_name
- **Unique Values:** 18
- **Average Length:** 15.34 characters
- **Top Values:**
  - `Nightwear`: 631 occurrences
  - `Bags`: 25 occurrences
  - `Garment Full body`: 5,796 occurrences
  - `Furniture`: 1 occurrences
  - `Garment and Shoe care`: 8 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Average Length:** 7.86 characters
- **Top Values:**
  - `Argyle`: 3 occurrences
  - `Chambray`: 101 occurrences
  - `Hologram`: 7 occurrences
  - `Sequin`: 242 occurrences
  - `Mesh`: 64 occurrences

### colour_group_name
- **Unique Values:** 50
- **Average Length:** 7.43 characters
- **Top Values:**
  - `Light Pink`: 1,998 occurrences
  - `Dark Yellow`: 215 occurrences
  - `Other Orange`: 82 occurrences
  - `White`: 4,115 occurrences
  - `Red`: 754 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Average Length:** 6.95 characters
- **Top Values:**
  - `Light`: 6,424 occurrences
  - `Dusty Light`: 9,135 occurrences
  - `Medium Dusty`: 5,777 occurrences
  - `Undefined`: 29 occurrences
  - `Medium`: 1,748 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Average Length:** 5.01 characters
- **Top Values:**
  - `Mole`: 705 occurrences
  - `Beige`: 2,972 occurrences
  - `Bluish Green`: 1 occurrences
  - `Orange`: 1,174 occurrences
  - `Turquoise`: 504 occurrences

### department_name
- **Unique Values:** 238
- **Average Length:** 12.04 characters
- **Top Values:**
  - `Shirt S&T`: 81 occurrences
  - `Young Girl Jersey Basic`: 217 occurrences
  - `Young Girl S&T`: 36 occurrences
  - `Young Boy Denim`: 140 occurrences
  - `Kids Boy Swimwear`: 34 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `A`: 12,862 occurrences
  - `J`: 1,156 occurrences
  - `S`: 1,328 occurrences
  - `F`: 4,717 occurrences
  - `C`: 3,474 occurrences

### index_name
- **Unique Values:** 10
- **Average Length:** 12.66 characters
- **Top Values:**
  - `Ladies Accessories`: 3,474 occurrences
  - `Sport`: 1,328 occurrences
  - `Menswear`: 4,717 occurrences
  - `Divided`: 7,111 occurrences
  - `Lingeries/Tights`: 3,919 occurrences

### index_group_name
- **Unique Values:** 5
- **Average Length:** 9.75 characters
- **Top Values:**
  - `Divided`: 7,111 occurrences
  - `Sport`: 1,328 occurrences
  - `Menswear`: 4,717 occurrences
  - `Ladieswear`: 20,255 occurrences
  - `Baby/Children`: 8,887 occurrences

### section_name
- **Unique Values:** 56
- **Average Length:** 17.17 characters
- **Top Values:**
  - `Baby Girl`: 476 occurrences
  - `Divided Projects`: 968 occurrences
  - `Divided Basics`: 872 occurrences
  - `Kids Accessories, Swimwear & D`: 526 occurrences
  - `Kids Outerwear`: 547 occurrences

### garment_group_name
- **Unique Values:** 21
- **Average Length:** 10.82 characters
- **Top Values:**
  - `Skirts`: 712 occurrences
  - `Shorts`: 877 occurrences
  - `Dressed`: 385 occurrences
  - `Knitwear`: 2,417 occurrences
  - `Trousers Denim`: 1,505 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Average Length:** 149.28 characters
- **Top Values:**
  - `Long-sleeved nursing top in a soft viscose weave with a boat neck and practical inner top for easier nursing access.`: 2 occurrences
  - `Long-sleeved blouse in a crêpe weave with a collar, buttons down the front, a yoke with a pleat at the back, buttoned cuffs and a rounded hem.`: 5 occurrences
  - `Rugby shirt in soft jersey with a contrasting colour collar, concealed buttons at the top, long sleeves with ribbed cuffs, and slits in the sides.`: 1 occurrences
  - `Ankle-length trousers in an airy viscose weave. High waist with covered elastication, a small frill trim and decorative ties, side pockets and slightly wider, tapered legs.`: 2 occurrences
  - `Playsuit in a patterned weave with a V-neck, wrapover front with a concealed press-stud at the top and 3/4-length, cuffed sleeves. Elasticated seam and a detachable tie belt at the waist, side pockets and short legs. Partly lined.`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 14.8 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| article_id | 0.3227 |
| product_code | 0.3227 |
| prod_name | 0.6443 |
| product_type_no | 0.3227 |
| product_type_name | 0.301 |
| product_group_name | 0.6186 |
| graphical_appearance_no | 0.3227 |
| graphical_appearance_name | 0.317 |
| colour_group_code | 0.3227 |
| colour_group_name | 0.2997 |
| perceived_colour_value_id | 0.3227 |
| perceived_colour_value_name | 0.2806 |
| perceived_colour_master_id | 0.3227 |
| perceived_colour_master_name | 0.2022 |
| department_no | 0.3227 |
| department_name | 0.4856 |
| index_code | 0.0403 |
| index_name | 0.5106 |
| index_group_no | 0.3227 |
| index_group_name | 0.3931 |
| section_no | 0.3227 |
| section_name | 0.6925 |
| garment_group_no | 0.3227 |
| garment_group_name | 0.4366 |
| detail_desc | 6.0256 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** article_id - Verify if these should be used as identifiers
- **Low cardinality columns:** perceived_colour_value_id, perceived_colour_value_name, index_code, index_name, index_group_no, index_group_name - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*