# Data Understanding Report
**Generated on:** 2025-08-09 11:24:36
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
  - `Abigail PQ sandal`: 3 occurrences
  - `Paloma Heel`: 1 occurrences
  - `Shorts Baggy`: 2 occurrences
  - `Chelsea WD blazer TP`: 4 occurrences
  - `Lexus lace dress`: 2 occurrences

### product_type_name
- **Unique Values:** 124
- **Average Length:** 7.46 characters
- **Top Values:**
  - `Swimwear bottom`: 751 occurrences
  - `Fine cosmetics`: 12 occurrences
  - `Cardigan`: 506 occurrences
  - `Tailored Waistcoat`: 23 occurrences
  - `Other shoe`: 123 occurrences

### product_group_name
- **Unique Values:** 18
- **Average Length:** 15.34 characters
- **Top Values:**
  - `Garment and Shoe care`: 8 occurrences
  - `Stationery`: 4 occurrences
  - `Garment Upper body`: 15,635 occurrences
  - `Unknown`: 111 occurrences
  - `Furniture`: 1 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Average Length:** 7.86 characters
- **Top Values:**
  - `Transparent`: 45 occurrences
  - `Neps`: 20 occurrences
  - `Chambray`: 101 occurrences
  - `Contrast`: 145 occurrences
  - `Mixed solid/pattern`: 415 occurrences

### colour_group_name
- **Unique Values:** 50
- **Average Length:** 7.43 characters
- **Top Values:**
  - `Dark Yellow`: 215 occurrences
  - `Light Turquoise`: 292 occurrences
  - `Light Grey`: 671 occurrences
  - `Dark Blue`: 3,696 occurrences
  - `Turquoise`: 132 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Average Length:** 6.95 characters
- **Top Values:**
  - `Medium`: 1,748 occurrences
  - `Medium Dusty`: 5,777 occurrences
  - `Unknown`: 5 occurrences
  - `Undefined`: 29 occurrences
  - `Bright`: 2,373 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Average Length:** 5.01 characters
- **Top Values:**
  - `Turquoise`: 504 occurrences
  - `Mole`: 705 occurrences
  - `Brown`: 1,083 occurrences
  - `White`: 5,542 occurrences
  - `Pink`: 3,474 occurrences

### department_name
- **Unique Values:** 238
- **Average Length:** 12.04 characters
- **Top Values:**
  - `Tops Girls`: 65 occurrences
  - `Other Accessories`: 89 occurrences
  - `Bags`: 355 occurrences
  - `Trouser S&T`: 73 occurrences
  - `Dress-up Boys`: 28 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `J`: 1,156 occurrences
  - `F`: 4,717 occurrences
  - `C`: 3,474 occurrences
  - `S`: 1,328 occurrences
  - `B`: 3,919 occurrences

### index_name
- **Unique Values:** 10
- **Average Length:** 12.66 characters
- **Top Values:**
  - `Children Accessories, Swimwear`: 1,156 occurrences
  - `Menswear`: 4,717 occurrences
  - `Baby Sizes 50-98`: 2,428 occurrences
  - `Lingeries/Tights`: 3,919 occurrences
  - `Divided`: 7,111 occurrences

### index_group_name
- **Unique Values:** 5
- **Average Length:** 9.75 characters
- **Top Values:**
  - `Sport`: 1,328 occurrences
  - `Menswear`: 4,717 occurrences
  - `Divided`: 7,111 occurrences
  - `Ladieswear`: 20,255 occurrences
  - `Baby/Children`: 8,887 occurrences

### section_name
- **Unique Values:** 56
- **Average Length:** 17.17 characters
- **Top Values:**
  - `Divided Selected`: 404 occurrences
  - `Womens Trend`: 1,216 occurrences
  - `Divided Asia keys`: 133 occurrences
  - `Kids Sports`: 136 occurrences
  - `Womens Tailoring`: 1,805 occurrences

### garment_group_name
- **Unique Values:** 21
- **Average Length:** 10.82 characters
- **Top Values:**
  - `Swimwear`: 1,683 occurrences
  - `Shorts`: 877 occurrences
  - `Socks and Tights`: 947 occurrences
  - `Jersey Basic`: 3,185 occurrences
  - `Dressed`: 385 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Average Length:** 149.28 characters
- **Top Values:**
  - `Outdoor jacket in woven fabric with a double-layered hood, stand up collar and zip down the front. Padded front and back sections and fleece-lined raglan sleeves in sturdy jersey with ribbed panels. Inset jersey panels in the sides and zipped front pockets. Longer and gently rounded at the back. Partly lined.`: 1 occurrences
  - `Jumper in a soft rib knit with low dropped shoulders, long sleeves and a hood with a wide, fine-knit drawstring.`: 3 occurrences
  - `Fully lined bikini top to give the bust a natural shape and light support. Decorative gathers at the front, narrow, detachable ties that tie at the back of the neck, a silicone trim at the top and support panels in the sides. Metal fastener at the back.`: 2 occurrences
  - `Satin-covered Alice band with a pointed, felted clown hat that has a faux fur pompom on top.`: 1 occurrences
  - `Long, sleeveless dress in pleated jersey. Round neckline and an opening with a decorative bar-shaped metal bead at the back of the neck. Narrow elasticated seam and a detachable tie belt at the waist, and a raw-edge hem.`: 4 occurrences

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