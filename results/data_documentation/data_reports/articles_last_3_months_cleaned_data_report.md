# Data Understanding Report
**Generated on:** 2025-08-09 14:55:09
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.87 MB
- **Last Modified:** 2025-08-09 14:55:05

## 📊 Dataset Overview
- **Rows:** 42,298
- **Columns:** 28
- **Total Cells:** 1,184,344

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| article_id | Int64 | 0 | 0.0% | 42,298 | 100.0% |
| product_code | Int64 | 0 | 0.0% | 20,981 | 49.6% |
| prod_name | String | 0 | 0.0% | 21,219 | 50.17% |
| product_type_no | Int64 | 0 | 0.0% | 125 | 0.3% |
| product_type_name | Categorical | 0 | 0.0% | 124 | 0.29% |
| product_group_name | Categorical | 0 | 0.0% | 18 | 0.04% |
| graphical_appearance_no | Int64 | 0 | 0.0% | 30 | 0.07% |
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
| product_type_no_negative_fixed | Boolean | 0 | 0.0% | 2 | 0.0% |
| graphical_appearance_no_negative_fixed | Boolean | 0 | 0.0% | 2 | 0.0% |
| product_code_invalid | Boolean | 0 | 0.0% | 1 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| article_id | 42298 | 767829371.9367 | N/A | 108775015 | N/A | N/A | N/A | 956217002 |
| product_code | 42298 | 767829.3654 | N/A | 108775 | N/A | N/A | N/A | 956217 |
| product_type_no | 42298 | 237.0751 | N/A | 0 | N/A | N/A | N/A | 762 |
| graphical_appearance_no | 42298 | 1009869.993 | N/A | 0 | N/A | N/A | N/A | 1010029 |
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
  - `TD SS Caleb`: 2 occurrences
  - `Beth buckle boot BG`: 1 occurrences
  - `Nebraska highshaft`: 1 occurrences
  - `Flirty Valeria earcuff pk`: 1 occurrences
  - `Ingrid top`: 2 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Outdoor trousers`: 30 occurrences
  - `Trousers`: 4,787 occurrences
  - `Kids Underwear top`: 36 occurrences
  - `Flat shoe`: 75 occurrences
  - `Underwear bottom`: 1,210 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Cosmetic`: 13 occurrences
  - `Fun`: 2 occurrences
  - `Socks & Tights`: 1,005 occurrences
  - `Swimwear`: 1,820 occurrences
  - `Accessories`: 4,179 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Lace`: 557 occurrences
  - `Chambray`: 101 occurrences
  - `Glittering/Metallic`: 314 occurrences
  - `Application/3D`: 365 occurrences
  - `Transparent`: 45 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Blue`: 1,383 occurrences
  - `Greyish Beige`: 129 occurrences
  - `Light Pink`: 1,998 occurrences
  - `Light Yellow`: 429 occurrences
  - `Turquoise`: 132 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Unknown`: 5 occurrences
  - `Medium Dusty`: 5,777 occurrences
  - `Medium`: 1,748 occurrences
  - `Bright`: 2,373 occurrences
  - `Undefined`: 29 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `Mole`: 705 occurrences
  - `Brown`: 1,083 occurrences
  - `Grey`: 2,892 occurrences
  - `Unknown`: 355 occurrences
  - `Green`: 1,339 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Jewellery Extended`: 250 occurrences
  - `Conscious Exclusive`: 58 occurrences
  - `Young Girl Big Acc`: 42 occurrences
  - `Kids Boy Big Acc`: 73 occurrences
  - `Small Accessories`: 349 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `H`: 2,832 occurrences
  - `A`: 12,862 occurrences
  - `B`: 3,919 occurrences
  - `S`: 1,328 occurrences
  - `I`: 2,471 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Children Accessories, Swimwear`: 1,156 occurrences
  - `Lingeries/Tights`: 3,919 occurrences
  - `Children Sizes 134-170`: 2,471 occurrences
  - `Ladies Accessories`: 3,474 occurrences
  - `Divided`: 7,111 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Baby/Children`: 8,887 occurrences
  - `Sport`: 1,328 occurrences
  - `Menswear`: 4,717 occurrences
  - `Divided`: 7,111 occurrences
  - `Ladieswear`: 20,255 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Divided Collection`: 3,489 occurrences
  - `Divided Projects`: 968 occurrences
  - `Kids Outerwear`: 547 occurrences
  - `Womens Casual`: 1,405 occurrences
  - `Womens Small accessories`: 1,693 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Trousers Denim`: 1,505 occurrences
  - `Dressed`: 385 occurrences
  - `Knitwear`: 2,417 occurrences
  - `Shoes`: 1,926 occurrences
  - `Skirts`: 712 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Jacket in woven fabric with a small print motif at the top. Detachable, jersey-lined hood, a stand-up collar and a zip down the front with a chin guard. Zipped side pockets and ribbing at the cuffs. Slightly longer and rounded at the back. Lined.`: 1 occurrences
  - `Jacket in soft sweatshirt fabric with a double-layered drawstring hood, zip down the front and side pockets at the front. Long raglan sleeves with ribbing at the cuffs, a frill-trimmed yoke at the back and an embroidered back section in woven fabric.`: 2 occurrences
  - `Joggers in sweatshirt fabric with contrasting colour stripes down the sides, an elasticated drawstring waist and slightly lower crotch. Side pockets, one back pocket and tapered legs with ribbed hems. Soft brushed inside.`: 5 occurrences
  - `Body in soft jersey made from a viscose and cotton blend with wide shoulder straps, a lined gusset with concealed press-studs and medium coverage at the back. Lined at the top.`: 1 occurrences
  - `Shirt in soft, washed cotton denim with a collar, press-studs down the front and yoke at the back. Chest pockets and long sleeves with press-studs at the cuffs.`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 6.19 MB

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
| product_type_no_negative_fixed | 0.0051 |
| graphical_appearance_no_negative_fixed | 0.0051 |
| product_code_invalid | 0.0051 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** article_id - Verify if these should be used as identifiers
- **Low cardinality columns:** perceived_colour_value_id, perceived_colour_value_name, index_code, index_name, index_group_no, index_group_name, product_type_no_negative_fixed, graphical_appearance_no_negative_fixed - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*