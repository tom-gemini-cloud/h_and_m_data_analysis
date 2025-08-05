# Data Understanding Report
**Generated on:** 2025-08-05 14:23:50
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
- **Unique Values:** 45,875
- **Average Length:** 15.54 characters
- **Top Values:**
  - `Easy shorts (D/W)`: 2 occurrences
  - `Ted Runner AOP SB`: 1 occurrences
  - `Bracelet Skull`: 1 occurrences
  - `Assa`: 1 occurrences
  - `Elise Belted top`: 1 occurrences

### product_type_name
- **Unique Values:** 131
- **Average Length:** 7.53 characters
- **Top Values:**
  - `Tote bag`: 2 occurrences
  - `Pyjama bottom`: 220 occurrences
  - `Hair string`: 238 occurrences
  - `Belt`: 458 occurrences
  - `Outdoor Waistcoat`: 154 occurrences

### product_group_name
- **Unique Values:** 19
- **Average Length:** 15.44 characters
- **Top Values:**
  - `Accessories`: 11,158 occurrences
  - `Garment and Shoe care`: 9 occurrences
  - `Fun`: 2 occurrences
  - `Interior textile`: 3 occurrences
  - `Garment Full body`: 13,292 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Average Length:** 8.29 characters
- **Top Values:**
  - `Jacquard`: 830 occurrences
  - `Check`: 2,178 occurrences
  - `Application/3D`: 1,341 occurrences
  - `Colour blocking`: 1,830 occurrences
  - `Mesh`: 86 occurrences

### colour_group_name
- **Unique Values:** 50
- **Average Length:** 7.48 characters
- **Top Values:**
  - `Other Purple`: 46 occurrences
  - `Dark Yellow`: 574 occurrences
  - `Greenish Khaki`: 2,767 occurrences
  - `Black`: 22,670 occurrences
  - `Green`: 815 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Average Length:** 6.81 characters
- **Top Values:**
  - `Medium`: 5,711 occurrences
  - `Unknown`: 28 occurrences
  - `Dark`: 42,706 occurrences
  - `Light`: 15,739 occurrences
  - `Bright`: 6,471 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Average Length:** 4.92 characters
- **Top Values:**
  - `Pink`: 9,403 occurrences
  - `Green`: 3,526 occurrences
  - `Grey`: 8,924 occurrences
  - `undefined`: 105 occurrences
  - `Yellowish Green`: 5 occurrences

### department_name
- **Unique Values:** 250
- **Average Length:** 13.14 characters
- **Top Values:**
  - `Kids Dress-up/Football`: 262 occurrences
  - `EQ Divided Basics`: 14 occurrences
  - `Kids Boy Outdoor`: 394 occurrences
  - `Tops Fancy Jersey`: 1,429 occurrences
  - `Young Girl Swimwear`: 175 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `I`: 9,214 occurrences
  - `B`: 6,775 occurrences
  - `D`: 15,149 occurrences
  - `J`: 4,615 occurrences
  - `S`: 3,392 occurrences

### index_name
- **Unique Values:** 10
- **Average Length:** 13.76 characters
- **Top Values:**
  - `Menswear`: 12,553 occurrences
  - `Ladies Accessories`: 6,961 occurrences
  - `Ladieswear`: 26,001 occurrences
  - `Sport`: 3,392 occurrences
  - `Divided`: 15,149 occurrences

### index_group_name
- **Unique Values:** 5
- **Average Length:** 10.16 characters
- **Top Values:**
  - `Ladieswear`: 39,737 occurrences
  - `Menswear`: 12,553 occurrences
  - `Sport`: 3,392 occurrences
  - `Baby/Children`: 34,711 occurrences
  - `Divided`: 15,149 occurrences

### section_name
- **Unique Values:** 56
- **Average Length:** 16.74 characters
- **Top Values:**
  - `Men Suits & Tailoring`: 1,428 occurrences
  - `Collaborations`: 559 occurrences
  - `Womens Small accessories`: 3,270 occurrences
  - `Special Collections`: 682 occurrences
  - `Divided Selected`: 991 occurrences

### garment_group_name
- **Unique Values:** 21
- **Average Length:** 10.95 characters
- **Top Values:**
  - `Knitwear`: 7,490 occurrences
  - `Jersey Basic`: 8,126 occurrences
  - `Blouses`: 5,838 occurrences
  - `Skirts`: 1,254 occurrences
  - `Trousers`: 6,727 occurrences

### detail_desc
- **Unique Values:** 43,405
- **Average Length:** 142.16 characters
- **Top Values:**
  - `Bomber jacket woven in a nylon blend with a stand-up collar that has a decorative zip and tab with press-studs. Zip down the front, a chest pocket, zipped side pockets and one inner pocket with a concealed press-stud. Ribbing at the cuffs and hem. Lined.`: 2 occurrences
  - `Short, bell-shaped skirt in woven fabric with a concealed zip and button at the back, and seam with a flare to the hem. Unlined.`: 3 occurrences
  - `Warm-lined boots in imitation leather with lacing at the front, a zip in one side and a loop at the back. Pile linings and insoles.`: 9 occurrences
  - `Suede boots with lacing at the front. Fabric linings, leather insoles and thermoplastic rubber (TPR) soles.`: 4 occurrences
  - `Calf-length jersey dress with a wrapover front, deep V-neck and a seam at the waist with pleats that go all the way round. Yoke at the back, a press-stud fastening at the waist, dropped shoulders and long, tapered sleeves. Unlined.`: 2 occurrences

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