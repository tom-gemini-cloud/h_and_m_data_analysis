# Data Understanding Report
**Generated on:** 2025-08-09 11:20:43
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.8 MB
- **Last Modified:** 2025-08-09 11:20:39

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
  - `DEAL Bobyn 2-PACK TOP`: 3 occurrences
  - `PC Tina Turner`: 1 occurrences
  - `J MYSA JOGGERS. CNY`: 1 occurrences
  - `Regina SL Rib set (J)`: 2 occurrences
  - `Sabrina set`: 1 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Bra extender`: 1 occurrences
  - `Tailored Waistcoat`: 23 occurrences
  - `Alice band`: 6 occurrences
  - `Other shoe`: 123 occurrences
  - `Dress`: 4,863 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Unknown`: 111 occurrences
  - `Bags`: 25 occurrences
  - `Garment and Shoe care`: 8 occurrences
  - `Items`: 15 occurrences
  - `Furniture`: 1 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Jacquard`: 258 occurrences
  - `All over pattern`: 6,351 occurrences
  - `Check`: 878 occurrences
  - `Colour blocking`: 533 occurrences
  - `Solid`: 21,928 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Light Orange`: 623 occurrences
  - `Unknown`: 5 occurrences
  - `Greyish Beige`: 129 occurrences
  - `Other Green`: 71 occurrences
  - `Bronze/Copper`: 30 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Unknown`: 5 occurrences
  - `Medium`: 1,748 occurrences
  - `Dusty Light`: 9,135 occurrences
  - `Light`: 6,424 occurrences
  - `Medium Dusty`: 5,777 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `Grey`: 2,892 occurrences
  - `Pink`: 3,474 occurrences
  - `Lilac Purple`: 518 occurrences
  - `Green`: 1,339 occurrences
  - `Beige`: 2,972 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Baby Socks`: 144 occurrences
  - `Tops woven DS`: 42 occurrences
  - `Underwear Woven`: 63 occurrences
  - `Small Accessories Extended`: 76 occurrences
  - `Outdoor/Blazers`: 311 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `A`: 12,862 occurrences
  - `J`: 1,156 occurrences
  - `F`: 4,717 occurrences
  - `I`: 2,471 occurrences
  - `H`: 2,832 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Children Accessories, Swimwear`: 1,156 occurrences
  - `Ladies Accessories`: 3,474 occurrences
  - `Lingeries/Tights`: 3,919 occurrences
  - `Sport`: 1,328 occurrences
  - `Divided`: 7,111 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Baby/Children`: 8,887 occurrences
  - `Sport`: 1,328 occurrences
  - `Menswear`: 4,717 occurrences
  - `Ladieswear`: 20,255 occurrences
  - `Divided`: 7,111 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Divided Complements Other`: 24 occurrences
  - `Divided Collection`: 3,489 occurrences
  - `Divided Selected`: 404 occurrences
  - `Womens Trend`: 1,216 occurrences
  - `Divided Asia keys`: 133 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Shorts`: 877 occurrences
  - `Swimwear`: 1,683 occurrences
  - `Dressed`: 385 occurrences
  - `Trousers Denim`: 1,505 occurrences
  - `Socks and Tights`: 947 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Short dress in woven fabric with a V-neck and wrapover front with a visible button at one side and concealed ties at the other. Long sleeves and wide, buttoned cuffs. Lined at the top.`: 2 occurrences
  - `Microfibre body with a gentle sculpting effect on the waist and bum. Adjustable shoulder straps and padded cups to shape the bust and provide good support. Lined gusset with press-studs and a high cut at the back with folded, glued edges. Mesh lining at the front.`: 1 occurrences
  - `Oversized jumper in a soft knit containing some wool with dropped shoulders, long sleeves, a rounded hem and ribbing around the neckline, cuffs and hem. Longer at the back. The polyester content of the jumper is recycled.`: 2 occurrences
  - `Short jersey top with a round neckline, short sleeves and an open back with ties at the hem.`: 2 occurrences
  - `Platform ankle boots in imitation leather with a zip in one side. Jersey linings made from recycled polyester, and imitation leather insoles. Heel 9.5 cm.`: 1 occurrences

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