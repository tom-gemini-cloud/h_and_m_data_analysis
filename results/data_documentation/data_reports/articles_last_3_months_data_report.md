# Data Understanding Report
**Generated on:** 2025-08-09 12:33:41
**File:** articles_last_3_months.parquet

## 📄 File Information
- **File Path:** `..\data\processed\articles_last_3_months.parquet`
- **File Type:** PARQUET
- **File Size:** 1.5 MB
- **Last Modified:** 2025-08-09 11:18:29

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
  - `20 den 1p Stockings`: 1 occurrences
  - `Trudy Cardigan`: 5 occurrences
  - `EDIE shorts`: 1 occurrences
  - `OL CELESTE PQ Espadrille`: 5 occurrences
  - `Monaco dress`: 1 occurrences

### product_type_name
- **Unique Values:** 124
- **Average Length:** 7.46 characters
- **Top Values:**
  - `Underdress`: 12 occurrences
  - `Costumes`: 33 occurrences
  - `Pyjama set`: 348 occurrences
  - `Dog wear`: 5 occurrences
  - `Headband`: 1 occurrences

### product_group_name
- **Unique Values:** 18
- **Average Length:** 15.34 characters
- **Top Values:**
  - `Bags`: 25 occurrences
  - `Furniture`: 1 occurrences
  - `Shoes`: 1,947 occurrences
  - `Garment Lower body`: 8,596 occurrences
  - `Underwear/nightwear`: 7 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Average Length:** 7.86 characters
- **Top Values:**
  - `All over pattern`: 6,351 occurrences
  - `Stripe`: 1,660 occurrences
  - `Chambray`: 101 occurrences
  - `Colour blocking`: 533 occurrences
  - `Check`: 878 occurrences

### colour_group_name
- **Unique Values:** 50
- **Average Length:** 7.43 characters
- **Top Values:**
  - `Turquoise`: 132 occurrences
  - `Pink`: 940 occurrences
  - `Light Pink`: 1,998 occurrences
  - `Silver`: 318 occurrences
  - `Light Grey`: 671 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Average Length:** 6.95 characters
- **Top Values:**
  - `Dusty Light`: 9,135 occurrences
  - `Undefined`: 29 occurrences
  - `Light`: 6,424 occurrences
  - `Bright`: 2,373 occurrences
  - `Medium`: 1,748 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Average Length:** 5.01 characters
- **Top Values:**
  - `Unknown`: 355 occurrences
  - `Khaki green`: 1,374 occurrences
  - `Orange`: 1,174 occurrences
  - `Black`: 10,050 occurrences
  - `Pink`: 3,474 occurrences

### department_name
- **Unique Values:** 238
- **Average Length:** 12.04 characters
- **Top Values:**
  - `Knitwear Basic`: 25 occurrences
  - `Hair Accessories`: 447 occurrences
  - `Kids Boy Exclusive`: 19 occurrences
  - `Underwear Jersey`: 134 occurrences
  - `Young boy Swimwear`: 42 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `I`: 2,471 occurrences
  - `J`: 1,156 occurrences
  - `B`: 3,919 occurrences
  - `S`: 1,328 occurrences
  - `C`: 3,474 occurrences

### index_name
- **Unique Values:** 10
- **Average Length:** 12.66 characters
- **Top Values:**
  - `Children Sizes 92-140`: 2,832 occurrences
  - `Children Accessories, Swimwear`: 1,156 occurrences
  - `Sport`: 1,328 occurrences
  - `Menswear`: 4,717 occurrences
  - `Baby Sizes 50-98`: 2,428 occurrences

### index_group_name
- **Unique Values:** 5
- **Average Length:** 9.75 characters
- **Top Values:**
  - `Menswear`: 4,717 occurrences
  - `Ladieswear`: 20,255 occurrences
  - `Baby/Children`: 8,887 occurrences
  - `Sport`: 1,328 occurrences
  - `Divided`: 7,111 occurrences

### section_name
- **Unique Values:** 56
- **Average Length:** 17.17 characters
- **Top Values:**
  - `Divided Basics`: 872 occurrences
  - `Kids Girl`: 1,031 occurrences
  - `Womens Lingerie`: 1,836 occurrences
  - `Young Girl`: 1,014 occurrences
  - `Ladies Denim`: 727 occurrences

### garment_group_name
- **Unique Values:** 21
- **Average Length:** 10.82 characters
- **Top Values:**
  - `Trousers Denim`: 1,505 occurrences
  - `Socks and Tights`: 947 occurrences
  - `Shorts`: 877 occurrences
  - `Special Offers`: 336 occurrences
  - `Shirts`: 748 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Average Length:** 149.28 characters
- **Top Values:**
  - `Fitted top in ribbed jersey made from an organic cotton blend with a deep neckline, decorative buttons and short sleeves.`: 1 occurrences
  - `Fitted jacket in woven fabric with notch lapels and a concealed hook-and-eye fastening at the front. Jetted front pockets, decorative slits at the cuffs and a single back vent. Lined.`: 1 occurrences
  - `Jumper in a soft knit with low dropped shoulders, long, textured-knit balloon sleeves and ribbing around the neckline, cuffs and hem.`: 2 occurrences
  - `Long-sleeved cardigan in a soft fine knit with a V-neck and buttons down the front. Ribbing around the neckline, cuffs and hem.`: 1 occurrences
  - `Pyjamas in soft, patterned jersey. Long-sleeved top with ribbing at the cuffs and hem. Bottoms with an elasticated waist and ribbed hems.`: 1 occurrences

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