# Data Understanding Report
**Generated on:** 2025-08-09 15:31:46
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.8 MB
- **Last Modified:** 2025-08-09 15:31:41

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
  - `Danni dress (RW)`: 1 occurrences
  - `Flirty Stella necklace`: 1 occurrences
  - `Cypress cardigan`: 2 occurrences
  - `SPEED Post dress`: 3 occurrences
  - `OLLIE cap(1)`: 1 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Pyjama bottom`: 117 occurrences
  - `Straw hat`: 6 occurrences
  - `Bra extender`: 1 occurrences
  - `Garment Set`: 365 occurrences
  - `Marker pen`: 4 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Swimwear`: 1,820 occurrences
  - `Socks & Tights`: 1,005 occurrences
  - `Garment Full body`: 5,796 occurrences
  - `Garment and Shoe care`: 8 occurrences
  - `Unknown`: 111 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Argyle`: 3 occurrences
  - `Stripe`: 1,660 occurrences
  - `Contrast`: 145 occurrences
  - `Treatment`: 160 occurrences
  - `Lace`: 557 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Red`: 754 occurrences
  - `Transparent`: 12 occurrences
  - `Light Grey`: 671 occurrences
  - `Light Green`: 303 occurrences
  - `Dark Red`: 751 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Dusty Light`: 9,135 occurrences
  - `Light`: 6,424 occurrences
  - `Medium Dusty`: 5,777 occurrences
  - `Unknown`: 5 occurrences
  - `Undefined`: 29 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `Khaki green`: 1,374 occurrences
  - `Red`: 1,635 occurrences
  - `Orange`: 1,174 occurrences
  - `Yellow`: 1,280 occurrences
  - `Grey`: 2,892 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Knit & Woven`: 206 occurrences
  - `Tops Boys`: 10 occurrences
  - `Baby Girl Local Relevance`: 2 occurrences
  - `Read & React`: 14 occurrences
  - `Denim Trousers`: 350 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `G`: 2,428 occurrences
  - `D`: 7,111 occurrences
  - `B`: 3,919 occurrences
  - `I`: 2,471 occurrences
  - `C`: 3,474 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Lingeries/Tights`: 3,919 occurrences
  - `Children Sizes 134-170`: 2,471 occurrences
  - `Sport`: 1,328 occurrences
  - `Children Accessories, Swimwear`: 1,156 occurrences
  - `Divided`: 7,111 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Divided`: 7,111 occurrences
  - `Sport`: 1,328 occurrences
  - `Menswear`: 4,717 occurrences
  - `Baby/Children`: 8,887 occurrences
  - `Ladieswear`: 20,255 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Men Accessories`: 418 occurrences
  - `Baby Girl`: 476 occurrences
  - `Contemporary Street`: 520 occurrences
  - `Contemporary Smart`: 718 occurrences
  - `Kids Sports`: 136 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Knitwear`: 2,417 occurrences
  - `Trousers`: 3,132 occurrences
  - `Accessories`: 4,336 occurrences
  - `Dresses/Skirts girls`: 418 occurrences
  - `Jersey Fancy`: 7,715 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Silk tie in a grosgrain weave. Width 7 cm.`: 2 occurrences
  - `Blouse in a cotton weave with buttons down the front, a V-neck with a wide flounced trim, long puff sleeves with adjustable buttoning at the cuffs and a tapered waist.`: 1 occurrences
  - `Dress in a soft, fine-knit cotton blend containing glittery threads with a ribbed neckline, sewn-on bow at the top and short sleeves.`: 2 occurrences
  - `Ankle boots in suede with a soft shaft. Fabric linings and insoles. Heel 8 cm.`: 1 occurrences
  - `Fully lined bikini bottoms with a low, V-shaped waist, narrow sides and a high cut at the back.`: 1 occurrences

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