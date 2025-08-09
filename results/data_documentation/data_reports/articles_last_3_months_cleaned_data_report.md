# Data Understanding Report
**Generated on:** 2025-08-09 15:00:03
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.82 MB
- **Last Modified:** 2025-08-09 14:59:59

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
  - `J LENA SHORTS EQ`: 1 occurrences
  - `Conan loafer`: 1 occurrences
  - `Seashell dress`: 2 occurrences
  - `Gladiator henley`: 5 occurrences
  - `Chip body`: 2 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Outdoor trousers`: 30 occurrences
  - `Zipper head`: 3 occurrences
  - `Garment Set`: 365 occurrences
  - `Slippers`: 56 occurrences
  - `Earrings`: 11 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Garment Upper body`: 15,635 occurrences
  - `Garment and Shoe care`: 8 occurrences
  - `Nightwear`: 631 occurrences
  - `Bags`: 25 occurrences
  - `Shoes`: 1,947 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Colour blocking`: 533 occurrences
  - `Check`: 878 occurrences
  - `Lace`: 557 occurrences
  - `Neps`: 20 occurrences
  - `Slub`: 46 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Pink`: 940 occurrences
  - `Yellow`: 624 occurrences
  - `Purple`: 99 occurrences
  - `Blue`: 1,383 occurrences
  - `Dark Yellow`: 215 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Undefined`: 29 occurrences
  - `Light`: 6,424 occurrences
  - `Dusty Light`: 9,135 occurrences
  - `Unknown`: 5 occurrences
  - `Dark`: 16,807 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `Khaki green`: 1,374 occurrences
  - `White`: 5,542 occurrences
  - `Metal`: 1,023 occurrences
  - `Unknown`: 355 occurrences
  - `undefined`: 29 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Kids Girl Jersey Fancy`: 453 occurrences
  - `Knitwear inactive from s1`: 4 occurrences
  - `Ladies Sport Acc`: 112 occurrences
  - `Shopbasket Socks`: 129 occurrences
  - `Men Sport Acc`: 49 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `C`: 3,474 occurrences
  - `S`: 1,328 occurrences
  - `I`: 2,471 occurrences
  - `D`: 7,111 occurrences
  - `B`: 3,919 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Lingeries/Tights`: 3,919 occurrences
  - `Children Sizes 134-170`: 2,471 occurrences
  - `Ladies Accessories`: 3,474 occurrences
  - `Ladieswear`: 12,862 occurrences
  - `Children Accessories, Swimwear`: 1,156 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Ladieswear`: 20,255 occurrences
  - `Baby/Children`: 8,887 occurrences
  - `Sport`: 1,328 occurrences
  - `Menswear`: 4,717 occurrences
  - `Divided`: 7,111 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Kids Girl`: 1,031 occurrences
  - `Divided Asia keys`: 133 occurrences
  - `Men Suits & Tailoring`: 572 occurrences
  - `Denim Men`: 306 occurrences
  - `Contemporary Smart`: 718 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Blouses`: 3,121 occurrences
  - `Shirts`: 748 occurrences
  - `Trousers Denim`: 1,505 occurrences
  - `Dresses/Skirts girls`: 418 occurrences
  - `Socks and Tights`: 947 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Short skirt woven in a modal blend with a grosgrain trim in a contrasting colour. Concealed zip in the side and a sewn-in belt at the front with D-rings. Unlined.`: 1 occurrences
  - `Trousers in stretch cotton twill with a regular waist, zip fly, side pockets, back pockets and slim, tapered legs with quilted sections at the knees.`: 1 occurrences
  - `Long dress in woven fabric in a narrow cut at the top with an opening at the front and short, narrow shoulder straps that fasten at the back of the neck. Decorative appliqués on the front, an opening and concealed zip at the back, a seam at the waist and gathered skirt. Lined.`: 1 occurrences
  - `Faux fur coat with wide lapels, concealed hook-and-eye fasteners at the front, welt side pockets and one inner pocket. Lined.`: 1 occurrences
  - `Waterproof trainers in mesh with imitation leather details. Padded edge and tongue, elasticated lacing and a hook and loop tab at the front, and a contrasting colour grosgrain loop at the back. Reflective details. Linings and moulded insoles in mesh.`: 1 occurrences

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