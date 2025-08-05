# Data Understanding Report
**Generated on:** 2025-08-05 15:19:42
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
  - `Billy fluffy`: 1 occurrences
  - `BB Adam Wind Jkt`: 1 occurrences
  - `VANJA`: 2 occurrences
  - `Wired Push`: 1 occurrences
  - `LINDA RIBBED BEANIE`: 3 occurrences

### product_type_name
- **Unique Values:** 131
- **Average Length:** 7.53 characters
- **Top Values:**
  - `Wallet`: 77 occurrences
  - `Headband`: 1 occurrences
  - `Watch`: 73 occurrences
  - `Clothing mist`: 1 occurrences
  - `Socks`: 1,889 occurrences

### product_group_name
- **Unique Values:** 19
- **Average Length:** 15.44 characters
- **Top Values:**
  - `Shoes`: 5,283 occurrences
  - `Bags`: 25 occurrences
  - `Garment Full body`: 13,292 occurrences
  - `Furniture`: 13 occurrences
  - `Unknown`: 121 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Average Length:** 8.29 characters
- **Top Values:**
  - `Transparent`: 86 occurrences
  - `Application/3D`: 1,341 occurrences
  - `Placement print`: 3,098 occurrences
  - `Melange`: 5,938 occurrences
  - `Jacquard`: 830 occurrences

### colour_group_name
- **Unique Values:** 50
- **Average Length:** 7.48 characters
- **Top Values:**
  - `Dark Green`: 2,106 occurrences
  - `Dark Red`: 2,340 occurrences
  - `Gold`: 1,377 occurrences
  - `Unknown`: 28 occurrences
  - `Other Red`: 114 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Average Length:** 6.81 characters
- **Top Values:**
  - `Medium`: 5,711 occurrences
  - `Unknown`: 28 occurrences
  - `Undefined`: 105 occurrences
  - `Medium Dusty`: 12,630 occurrences
  - `Bright`: 6,471 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Average Length:** 4.92 characters
- **Top Values:**
  - `Pink`: 9,403 occurrences
  - `Beige`: 5,657 occurrences
  - `Yellowish Green`: 5 occurrences
  - `Orange`: 2,734 occurrences
  - `Green`: 3,526 occurrences

### department_name
- **Unique Values:** 250
- **Average Length:** 13.14 characters
- **Top Values:**
  - `Girls Projects`: 7 occurrences
  - `Belts`: 374 occurrences
  - `Knit & Woven`: 512 occurrences
  - `Young Girl Swimwear`: 175 occurrences
  - `Baby Boy Jersey Fancy`: 872 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `C`: 6,961 occurrences
  - `F`: 12,553 occurrences
  - `I`: 9,214 occurrences
  - `A`: 26,001 occurrences
  - `B`: 6,775 occurrences

### index_name
- **Unique Values:** 10
- **Average Length:** 13.76 characters
- **Top Values:**
  - `Ladieswear`: 26,001 occurrences
  - `Menswear`: 12,553 occurrences
  - `Children Sizes 92-140`: 12,007 occurrences
  - `Ladies Accessories`: 6,961 occurrences
  - `Children Sizes 134-170`: 9,214 occurrences

### index_group_name
- **Unique Values:** 5
- **Average Length:** 10.16 characters
- **Top Values:**
  - `Sport`: 3,392 occurrences
  - `Ladieswear`: 39,737 occurrences
  - `Divided`: 15,149 occurrences
  - `Baby/Children`: 34,711 occurrences
  - `Menswear`: 12,553 occurrences

### section_name
- **Unique Values:** 56
- **Average Length:** 16.74 characters
- **Top Values:**
  - `Kids & Baby Shoes`: 2,142 occurrences
  - `Special Collections`: 682 occurrences
  - `Men Edition`: 330 occurrences
  - `Ladies Other`: 4 occurrences
  - `Womens Tailoring`: 3,376 occurrences

### garment_group_name
- **Unique Values:** 21
- **Average Length:** 10.95 characters
- **Top Values:**
  - `Special Offers`: 1,061 occurrences
  - `Dresses/Skirts girls`: 1,541 occurrences
  - `Shirts`: 2,116 occurrences
  - `Jersey Basic`: 8,126 occurrences
  - `Woven/Jersey/Knitted mix Baby`: 1,965 occurrences

### detail_desc
- **Unique Values:** 43,405
- **Average Length:** 142.16 characters
- **Top Values:**
  - `Fitted,off-the-shoulder mesh top with decorative gathers at the front and long sleeves. Jersey lining front and back.`: 1 occurrences
  - `3/4-length sports tights in fast-drying functional fabric with an elasticated waist and reflective details.`: 2 occurrences
  - `Leather bag with two handles and a zip at the top and a detachable, adjustable shoulder strap. Tab and press-stud at the sides to adjust the size of the bag and a detachable address label on one handle. Padded compartment to fit laptops up to 15”, a zipped inner compartment and studs on the bottom. Lined. Size approx. 14x34x40 cm.`: 1 occurrences
  - `Hat in braided paper straw with a grosgrain band. Width of brim 3.5 cm.`: 2 occurrences
  - `Short, straight-cut dress in woven fabric with a round neckline that has a small opening and concealed button at the back of the neck. Long sleeves and cuffs with two buttons. Unlined.`: 5 occurrences

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