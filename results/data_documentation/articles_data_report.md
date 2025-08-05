# Data Understanding Report
**Generated on:** 2025-08-05 15:29:57
**File:** articles.csv

## 📄 File Information
- **File Path:** `..\data\raw\articles.csv`
- **File Type:** CSV
- **File Size:** 34.45 MB
- **Last Modified:** 2022-01-17 21:12:22

## 📊 Dataset Overview
- **Rows:** 105,542
- **Columns:** 25
- **Total Cells:** 2,638,550

## 🔍 Data Quality Summary
- **Completeness Score:** 99.98%
- **Missing Values:** 416 (0.02%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| article_id | Int64 | 0 | 0.0% | 105,542 | 100.0% |
| product_code | Int64 | 0 | 0.0% | 47,224 | 44.74% |
| prod_name | String | 0 | 0.0% | 45,875 | 43.47% |
| product_type_no | Int64 | 0 | 0.0% | 132 | 0.13% |
| product_type_name | String | 0 | 0.0% | 131 | 0.12% |
| product_group_name | String | 0 | 0.0% | 19 | 0.02% |
| graphical_appearance_no | Int64 | 0 | 0.0% | 30 | 0.03% |
| graphical_appearance_name | String | 0 | 0.0% | 30 | 0.03% |
| colour_group_code | Int64 | 0 | 0.0% | 50 | 0.05% |
| colour_group_name | String | 0 | 0.0% | 50 | 0.05% |
| perceived_colour_value_id | Int64 | 0 | 0.0% | 8 | 0.01% |
| perceived_colour_value_name | String | 0 | 0.0% | 8 | 0.01% |
| perceived_colour_master_id | Int64 | 0 | 0.0% | 20 | 0.02% |
| perceived_colour_master_name | String | 0 | 0.0% | 20 | 0.02% |
| department_no | Int64 | 0 | 0.0% | 299 | 0.28% |
| department_name | String | 0 | 0.0% | 250 | 0.24% |
| index_code | String | 0 | 0.0% | 10 | 0.01% |
| index_name | String | 0 | 0.0% | 10 | 0.01% |
| index_group_no | Int64 | 0 | 0.0% | 5 | 0.0% |
| index_group_name | String | 0 | 0.0% | 5 | 0.0% |
| section_no | Int64 | 0 | 0.0% | 57 | 0.05% |
| section_name | String | 0 | 0.0% | 56 | 0.05% |
| garment_group_no | Int64 | 0 | 0.0% | 21 | 0.02% |
| garment_group_name | String | 0 | 0.0% | 21 | 0.02% |
| detail_desc | String | 416 | 0.39% | 43,405 | 41.13% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| article_id | 105542 | 698424569.0969 | N/A | 108775015 | N/A | N/A | N/A | 959461001 |
| product_code | 105542 | 698424.5634 | N/A | 108775 | N/A | N/A | N/A | 959461 |
| product_type_no | 105542 | 234.8619 | N/A | -1 | N/A | N/A | N/A | 762 |
| graphical_appearance_no | 105542 | 1009515.0757 | N/A | -1 | N/A | N/A | N/A | 1010029 |
| colour_group_code | 105542 | 32.2338 | N/A | -1 | N/A | N/A | N/A | 93 |
| perceived_colour_value_id | 105542 | 3.2062 | N/A | -1 | N/A | N/A | N/A | 7 |
| perceived_colour_master_id | 105542 | 7.808 | N/A | -1 | N/A | N/A | N/A | 20 |
| department_no | 105542 | 4532.7778 | N/A | 1201 | N/A | N/A | N/A | 9989 |
| index_group_no | 105542 | 3.1715 | N/A | 1 | N/A | N/A | N/A | 26 |
| section_no | 105542 | 42.6642 | N/A | 2 | N/A | N/A | N/A | 97 |
| garment_group_no | 105542 | 1010.4383 | N/A | 1001 | N/A | N/A | N/A | 1025 |

## 📝 Categorical Column Analysis
### prod_name
- **Unique Values:** 45,875
- **Average Length:** 15.54 characters
- **Top Values:**
  - `ANDREA romper set`: 1 occurrences
  - `ANDY L/S PRICE TEE`: 1 occurrences
  - `LS flip flop`: 1 occurrences
  - `Cayla fancy jogger`: 2 occurrences
  - `Mel Tulle Dress`: 1 occurrences

### product_type_name
- **Unique Values:** 131
- **Average Length:** 7.53 characters
- **Top Values:**
  - `Hair/alice band`: 854 occurrences
  - `Underwear body`: 174 occurrences
  - `Eyeglasses`: 2 occurrences
  - `Night gown`: 171 occurrences
  - `Other accessories`: 1,034 occurrences

### product_group_name
- **Unique Values:** 19
- **Average Length:** 15.44 characters
- **Top Values:**
  - `Fun`: 2 occurrences
  - `Underwear`: 5,490 occurrences
  - `Furniture`: 13 occurrences
  - `Garment Upper body`: 42,741 occurrences
  - `Garment Full body`: 13,292 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Average Length:** 8.29 characters
- **Top Values:**
  - `Lace`: 1,513 occurrences
  - `Hologram`: 8 occurrences
  - `Metallic`: 346 occurrences
  - `All over pattern`: 17,165 occurrences
  - `Solid`: 49,747 occurrences

### colour_group_name
- **Unique Values:** 50
- **Average Length:** 7.48 characters
- **Top Values:**
  - `Light Pink`: 5,811 occurrences
  - `Dark Orange`: 886 occurrences
  - `Pink`: 2,063 occurrences
  - `Green`: 815 occurrences
  - `Other Pink`: 750 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Average Length:** 6.81 characters
- **Top Values:**
  - `Medium Dusty`: 12,630 occurrences
  - `Unknown`: 28 occurrences
  - `Dark`: 42,706 occurrences
  - `Dusty Light`: 22,152 occurrences
  - `Light`: 15,739 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Average Length:** 4.92 characters
- **Top Values:**
  - `Lilac Purple`: 1,100 occurrences
  - `Mole`: 1,223 occurrences
  - `Unknown`: 685 occurrences
  - `undefined`: 105 occurrences
  - `Turquoise`: 1,829 occurrences

### department_name
- **Unique Values:** 250
- **Average Length:** 13.14 characters
- **Top Values:**
  - `Blazer S&T`: 142 occurrences
  - `Woven inactive from s1`: 62 occurrences
  - `Shoes`: 443 occurrences
  - `Girls Local Relevance`: 70 occurrences
  - `Young Boy Shirt`: 290 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `A`: 26,001 occurrences
  - `S`: 3,392 occurrences
  - `I`: 9,214 occurrences
  - `H`: 12,007 occurrences
  - `D`: 15,149 occurrences

### index_name
- **Unique Values:** 10
- **Average Length:** 13.76 characters
- **Top Values:**
  - `Sport`: 3,392 occurrences
  - `Ladies Accessories`: 6,961 occurrences
  - `Divided`: 15,149 occurrences
  - `Menswear`: 12,553 occurrences
  - `Baby Sizes 50-98`: 8,875 occurrences

### index_group_name
- **Unique Values:** 5
- **Average Length:** 10.16 characters
- **Top Values:**
  - `Menswear`: 12,553 occurrences
  - `Baby/Children`: 34,711 occurrences
  - `Divided`: 15,149 occurrences
  - `Sport`: 3,392 occurrences
  - `Ladieswear`: 39,737 occurrences

### section_name
- **Unique Values:** 56
- **Average Length:** 16.74 characters
- **Top Values:**
  - `Divided Basics`: 1,723 occurrences
  - `Mens Outerwear`: 629 occurrences
  - `Men H&M Sport`: 872 occurrences
  - `Divided Asia keys`: 280 occurrences
  - `EQ Divided`: 26 occurrences

### garment_group_name
- **Unique Values:** 21
- **Average Length:** 10.95 characters
- **Top Values:**
  - `Accessories`: 11,519 occurrences
  - `Shoes`: 5,145 occurrences
  - `Blouses`: 5,838 occurrences
  - `Unknown`: 3,873 occurrences
  - `Shirts`: 2,116 occurrences

### detail_desc
- **Unique Values:** 43,405
- **Average Length:** 142.16 characters
- **Top Values:**
  - `Pyjamas with a top and shorts in soft, patterned jersey. Top with a lace-trimmed V-neck, and short sleeves with overlocked edges. Shorts with narrow elastication at the waist and overlocked hems.`: 3 occurrences
  - `5-pocket slim-fit jeans in washed, stretch, flexible denim for high comfort with an adjustable, elasticated waist, zip fly and button and straight hems.`: 2 occurrences
  - `Padded parka with a pile-lined hood with a faux fur trim. Zip and wind flap with press-studs down the front and a drawstring at the waist and hem. Handwarmer pockets and flap front pockets with a press-stud, tab with adjustable fastening and inner ribbing at the cuffs and a single back vent. Lined.`: 1 occurrences
  - `Patterned softshell jacket in windproof, water-repellent functional fabric with folded seams, a detachable hood and zip down the front. Side pockets, reflective details and narrow elastication at the cuffs and hem. Brushed thermal inside. The jacket has a water-repellent coating without fluorocarbons.`: 3 occurrences
  - `High-waisted jeans in washed, superstretch denim with a print motif, zip fly and button, fake front pockets, real back pockets and super-skinny legs.`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 36.38 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| article_id | 0.8052 |
| product_code | 0.8052 |
| prod_name | 1.5639 |
| product_type_no | 0.8052 |
| product_type_name | 0.758 |
| product_group_name | 1.5541 |
| graphical_appearance_no | 0.8052 |
| graphical_appearance_name | 0.834 |
| colour_group_code | 0.8052 |
| colour_group_name | 0.7529 |
| perceived_colour_value_id | 0.8052 |
| perceived_colour_value_name | 0.6857 |
| perceived_colour_master_id | 0.8052 |
| perceived_colour_master_name | 0.4957 |
| department_no | 0.8052 |
| department_name | 1.3226 |
| index_code | 0.1007 |
| index_name | 1.3852 |
| index_group_no | 0.8052 |
| index_group_name | 1.0224 |
| section_no | 0.8052 |
| section_name | 1.6852 |
| garment_group_no | 0.8052 |
| garment_group_name | 1.1023 |
| detail_desc | 14.2634 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** article_id - Verify if these should be used as identifiers
- **Low cardinality columns:** perceived_colour_value_id, perceived_colour_value_name, index_code, index_name, index_group_no, index_group_name - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*