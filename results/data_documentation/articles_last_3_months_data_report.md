# Data Understanding Report
**Generated on:** 2025-08-05 14:23:26
**File:** articles_last_3_months.parquet

## 📄 File Information
- **File Path:** `data\processed\articles_last_3_months.parquet`
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
| article_id | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| product_code | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| product_type_no | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| graphical_appearance_no | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| colour_group_code | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| perceived_colour_value_id | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| perceived_colour_master_id | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| department_no | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| index_group_no | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| section_no | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| garment_group_no | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

## 📝 Categorical Column Analysis
### prod_name
- **Unique Values:** 21,219
- **Average Length:** 15.97 characters
- **Top Values:**
  - `Shelley`: 3 occurrences
  - `Lazer Razer Sport Top`: 4 occurrences
  - `Jacqueline Strap dress`: 1 occurrences
  - `Luca waterproof low SG`: 2 occurrences
  - `Class Carro earrings RT`: 2 occurrences

### product_type_name
- **Unique Values:** 124
- **Average Length:** 7.46 characters
- **Top Values:**
  - `Watch`: 16 occurrences
  - `Toy`: 2 occurrences
  - `Backpack`: 6 occurrences
  - `Cross-body bag`: 5 occurrences
  - `Earring`: 505 occurrences

### product_group_name
- **Unique Values:** 18
- **Average Length:** 15.34 characters
- **Top Values:**
  - `Garment Upper body`: 15,635 occurrences
  - `Garment Lower body`: 8,596 occurrences
  - `Swimwear`: 1,820 occurrences
  - `Socks & Tights`: 1,005 occurrences
  - `Furniture`: 1 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Average Length:** 7.86 characters
- **Top Values:**
  - `Jacquard`: 258 occurrences
  - `Contrast`: 145 occurrences
  - `Colour blocking`: 533 occurrences
  - `Dot`: 305 occurrences
  - `Stripe`: 1,660 occurrences

### colour_group_name
- **Unique Values:** 50
- **Average Length:** 7.43 characters
- **Top Values:**
  - `Greyish Beige`: 129 occurrences
  - `Other Yellow`: 117 occurrences
  - `Other Orange`: 82 occurrences
  - `Orange`: 339 occurrences
  - `Other`: 29 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Average Length:** 6.95 characters
- **Top Values:**
  - `Undefined`: 29 occurrences
  - `Bright`: 2,373 occurrences
  - `Medium Dusty`: 5,777 occurrences
  - `Unknown`: 5 occurrences
  - `Light`: 6,424 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Average Length:** 5.01 characters
- **Top Values:**
  - `Khaki green`: 1,374 occurrences
  - `Brown`: 1,083 occurrences
  - `Orange`: 1,174 occurrences
  - `Beige`: 2,972 occurrences
  - `Blue`: 6,343 occurrences

### department_name
- **Unique Values:** 238
- **Average Length:** 12.04 characters
- **Top Values:**
  - `Young Boy Jersey Basic`: 174 occurrences
  - `Test Ladies`: 3 occurrences
  - `Young Boy Trouser`: 84 occurrences
  - `Kids Boy Outdoor`: 97 occurrences
  - `Projects Woven Tops`: 107 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `G`: 2,428 occurrences
  - `S`: 1,328 occurrences
  - `A`: 12,862 occurrences
  - `F`: 4,717 occurrences
  - `I`: 2,471 occurrences

### index_name
- **Unique Values:** 10
- **Average Length:** 12.66 characters
- **Top Values:**
  - `Children Accessories, Swimwear`: 1,156 occurrences
  - `Baby Sizes 50-98`: 2,428 occurrences
  - `Children Sizes 134-170`: 2,471 occurrences
  - `Sport`: 1,328 occurrences
  - `Ladieswear`: 12,862 occurrences

### index_group_name
- **Unique Values:** 5
- **Average Length:** 9.75 characters
- **Top Values:**
  - `Ladieswear`: 20,255 occurrences
  - `Menswear`: 4,717 occurrences
  - `Sport`: 1,328 occurrences
  - `Baby/Children`: 8,887 occurrences
  - `Divided`: 7,111 occurrences

### section_name
- **Unique Values:** 56
- **Average Length:** 17.17 characters
- **Top Values:**
  - `Kids Outerwear`: 547 occurrences
  - `Men Other`: 24 occurrences
  - `Divided Collection`: 3,489 occurrences
  - `Men Accessories`: 418 occurrences
  - `H&M+`: 1,079 occurrences

### garment_group_name
- **Unique Values:** 21
- **Average Length:** 10.82 characters
- **Top Values:**
  - `Blouses`: 3,121 occurrences
  - `Unknown`: 1,020 occurrences
  - `Trousers`: 3,132 occurrences
  - `Dresses/Skirts girls`: 418 occurrences
  - `Shorts`: 877 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Average Length:** 149.28 characters
- **Top Values:**
  - `Boots in imitation leather with an ankle-height shaft and platform soles. Lacing at the front with speed hooks at the top and a welt seam around the soles. Fabric linings and insoles and chunky thermoplastic rubber (TPR) soles. Platform 3.5 cm.`: 1 occurrences
  - `Hair scarf in an airy, patterned weave that can be tied around the head or neck. Size 16x22 cm.`: 1 occurrences
  - `Jumper in a soft jacquard knit with a round neck, long sleeves and ribbing around the neckline, cuffs and hem.`: 1 occurrences
  - `Chunky, metal anchor chain necklace with a pendant. Adjustable length approx. 45-55 cm.`: 2 occurrences
  - `Shirt in a cotton weave with a collar, buttons down the front, a yoke at the back and long sleeves with narrow, buttoned cuffs. Pre-tied bow tie with an adjustable elastic strap and plastic fastener at the back.`: 1 occurrences

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