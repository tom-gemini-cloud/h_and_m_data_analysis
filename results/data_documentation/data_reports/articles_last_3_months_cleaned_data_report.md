# Data Understanding Report
**Generated on:** 2025-08-09 15:12:54
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.79 MB
- **Last Modified:** 2025-08-09 15:12:50

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
  - `Rosalie dress`: 3 occurrences
  - `Salmon basic denim`: 5 occurrences
  - `Maran linen`: 5 occurrences
  - `Marla 2pk`: 1 occurrences
  - `MIAMI cargo shorts`: 1 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Coat`: 169 occurrences
  - `Tie`: 33 occurrences
  - `Trousers`: 4,787 occurrences
  - `Sneakers`: 543 occurrences
  - `Bodysuit`: 371 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Underwear/nightwear`: 7 occurrences
  - `Accessories`: 4,179 occurrences
  - `Garment Upper body`: 15,635 occurrences
  - `Nightwear`: 631 occurrences
  - `Stationery`: 4 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Chambray`: 101 occurrences
  - `Embroidery`: 477 occurrences
  - `Melange`: 2,161 occurrences
  - `Application/3D`: 365 occurrences
  - `Glittering/Metallic`: 314 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Silver`: 318 occurrences
  - `White`: 4,115 occurrences
  - `Other Blue`: 22 occurrences
  - `Light Orange`: 623 occurrences
  - `Grey`: 1,359 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Light`: 6,424 occurrences
  - `Unknown`: 5 occurrences
  - `Dusty Light`: 9,135 occurrences
  - `Bright`: 2,373 occurrences
  - `Undefined`: 29 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `Green`: 1,339 occurrences
  - `Metal`: 1,023 occurrences
  - `Red`: 1,635 occurrences
  - `Bluish Green`: 1 occurrences
  - `Mole`: 705 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Trousers & Skirt`: 155 occurrences
  - `AK Dresses & Outdoor`: 49 occurrences
  - `Conscious Exclusive`: 58 occurrences
  - `Baby basics`: 307 occurrences
  - `Skirts DS`: 22 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `B`: 3,919 occurrences
  - `G`: 2,428 occurrences
  - `C`: 3,474 occurrences
  - `D`: 7,111 occurrences
  - `J`: 1,156 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Children Accessories, Swimwear`: 1,156 occurrences
  - `Ladieswear`: 12,862 occurrences
  - `Divided`: 7,111 occurrences
  - `Menswear`: 4,717 occurrences
  - `Lingeries/Tights`: 3,919 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Sport`: 1,328 occurrences
  - `Baby/Children`: 8,887 occurrences
  - `Ladieswear`: 20,255 occurrences
  - `Menswear`: 4,717 occurrences
  - `Divided`: 7,111 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Womens Premium`: 487 occurrences
  - `Ladies Other`: 3 occurrences
  - `Collaborations`: 121 occurrences
  - `Kids Accessories, Swimwear & D`: 526 occurrences
  - `Womens Tailoring`: 1,805 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Dresses/Skirts girls`: 418 occurrences
  - `Skirts`: 712 occurrences
  - `Trousers`: 3,132 occurrences
  - `Shirts`: 748 occurrences
  - `Blouses`: 3,121 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Leggings in stretch imitation leather. High waist with concealed elastication.`: 1 occurrences
  - `Platform sandals with open toes, crossover foot straps and an adjustable ankle strap with concealed elastication and a round metal buckle. Imitation leather insoles. Platform front approx. 2 cm. Heel 9.5 cm.`: 1 occurrences
  - `Short dress in soft jersey made from a viscose blend with a round neckline, long sleeves and side pockets. Unlined.`: 3 occurrences
  - `Socks in a fine-knit cotton blend with a small motif at the top and elasticated tops.`: 1 occurrences
  - `Sports bras in fast-drying functional fabric with a lined front, racer back with sections in ventilating mesh, and a wide elasticated hem. Medium support.`: 5 occurrences

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