# Data Understanding Report
**Generated on:** 2025-08-07 16:44:35
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.86 MB
- **Last Modified:** 2025-08-07 16:44:32

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
  - `Margaux SL-Set (W)`: 3 occurrences
  - `HEADBAND BG mini me`: 2 occurrences
  - `2PACK TEMPEST TRS`: 2 occurrences
  - `Sugar Zip LS`: 1 occurrences
  - `GLOVES MAGIC 3-PACK BASIC`: 2 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Scarf`: 279 occurrences
  - `Cap/peaked`: 157 occurrences
  - `Outdoor overall`: 24 occurrences
  - `Braces`: 3 occurrences
  - `Necklace`: 277 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Items`: 15 occurrences
  - `Garment and Shoe care`: 8 occurrences
  - `Unknown`: 111 occurrences
  - `Underwear`: 2,503 occurrences
  - `Furniture`: 1 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Treatment`: 160 occurrences
  - `Neps`: 20 occurrences
  - `Chambray`: 101 occurrences
  - `Melange`: 2,161 occurrences
  - `Front print`: 785 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Light Beige`: 1,682 occurrences
  - `Dark Green`: 755 occurrences
  - `Other Red`: 34 occurrences
  - `Purple`: 99 occurrences
  - `Blue`: 1,383 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Medium Dusty`: 5,777 occurrences
  - `Bright`: 2,373 occurrences
  - `Dark`: 16,807 occurrences
  - `Light`: 6,424 occurrences
  - `Medium`: 1,748 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `Pink`: 3,474 occurrences
  - `Yellow`: 1,280 occurrences
  - `Lilac Purple`: 518 occurrences
  - `undefined`: 29 occurrences
  - `Unknown`: 355 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Take Care External`: 87 occurrences
  - `Young Girl UW/NW`: 122 occurrences
  - `Kids Girl Exclusive`: 14 occurrences
  - `Shirt S&T`: 81 occurrences
  - `Socks`: 125 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `B`: 3,919 occurrences
  - `I`: 2,471 occurrences
  - `F`: 4,717 occurrences
  - `D`: 7,111 occurrences
  - `C`: 3,474 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Sport`: 1,328 occurrences
  - `Lingeries/Tights`: 3,919 occurrences
  - `Children Accessories, Swimwear`: 1,156 occurrences
  - `Children Sizes 92-140`: 2,832 occurrences
  - `Baby Sizes 50-98`: 2,428 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Menswear`: 4,717 occurrences
  - `Ladieswear`: 20,255 occurrences
  - `Baby/Children`: 8,887 occurrences
  - `Divided`: 7,111 occurrences
  - `Sport`: 1,328 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Denim Men`: 306 occurrences
  - `Men Project`: 25 occurrences
  - `Womens Lingerie`: 1,836 occurrences
  - `Young Boy`: 655 occurrences
  - `Kids Local Relevance`: 23 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Trousers`: 3,132 occurrences
  - `Outdoor`: 1,550 occurrences
  - `Trousers Denim`: 1,505 occurrences
  - `Accessories`: 4,336 occurrences
  - `Dresses Ladies`: 2,513 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Parka in cotton twill with a lined, drawstring hood, zip and wind flap with concealed press-studs down the front, handwarmer pockets with a press-stud and patch front pockets with a flap. Adjustable press-stud fastenings at the cuffs, a drawstring at the hem and a single back vent. Lined.`: 1 occurrences
  - `Trainers in leather with suede details, open lacing and a lightly padded edge and tongue. Leather linings and insoles and slightly higher, textured soles.`: 1 occurrences
  - `Ballet shoes with a shimmering metallic finish. Wide elastic gore at the top and narrow elastication around the opening. Linings and insoles in a cotton weave. Suede soles.`: 1 occurrences
  - `Hi-tops in imitation leather with an adjustable hook and loop tab and elasticated lacing at the front. Loop at the back. Pile linings and insoles and rubber soles.`: 1 occurrences
  - `Ballet pumps in imitation leather with a grosgrain trim at the top, elastic strap over the foot and decorative bow at the front. Fabric linings and insoles.`: 2 occurrences

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