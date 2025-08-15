# Data Understanding Report
**Generated on:** 2025-08-12 10:58:49
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `..\data\cleaned\articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.84 MB
- **Last Modified:** 2025-08-12 10:58:45

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
| product_code | 42298 | 767829.3654 | N/A | 108775 | N/A | N/A | N/A | 956217 |
| product_type_no | 42298 | 237.0751 | N/A | 0 | N/A | N/A | N/A | 762 |
| graphical_appearance_no | 42298 | 1009869.993 | N/A | 0 | N/A | N/A | N/A | 1010029 |
| colour_group_code | 42298 | 29.7211 | N/A | -1 | N/A | N/A | N/A | 93 |
| department_no | 42298 | 3936.5935 | N/A | 1201 | N/A | N/A | N/A | 9989 |
| index_group_no | 42298 | 2.8064 | N/A | 1 | N/A | N/A | N/A | 26 |
| section_no | 42298 | 40.15 | N/A | 2 | N/A | N/A | N/A | 97 |
| garment_group_no | 42298 | 1010.9849 | N/A | 1001 | N/A | N/A | N/A | 1025 |

## 📝 Categorical Column Analysis
### prod_name
- **Unique Values:** 21,219
- **Average Length:** 15.97 characters
- **Top Values:**
  - `Denim Pauls LS Bandcollar`: 1 occurrences
  - `Legend Inner bra cropped tank`: 3 occurrences
  - `Tina(1)`: 2 occurrences
  - `New Pluto Dress`: 4 occurrences
  - `SHIRT WESTERN FRILL 79`: 1 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Dog wear`: 5 occurrences
  - `Mobile case`: 4 occurrences
  - `Washing bag`: 1 occurrences
  - `Skirt`: 1,310 occurrences
  - `Pyjama jumpsuit/playsuit`: 106 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Bags`: 25 occurrences
  - `Items`: 15 occurrences
  - `Garment Upper body`: 15,635 occurrences
  - `Garment Lower body`: 8,596 occurrences
  - `Fun`: 2 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Check`: 878 occurrences
  - `Sequin`: 242 occurrences
  - `Slub`: 46 occurrences
  - `Neps`: 20 occurrences
  - `Dot`: 305 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Dark Turquoise`: 135 occurrences
  - `Dark Orange`: 422 occurrences
  - `Transparent`: 12 occurrences
  - `Blue`: 1,383 occurrences
  - `Light Grey`: 671 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Dark`: 16,807 occurrences
  - `Light`: 6,424 occurrences
  - `Medium Dusty`: 5,777 occurrences
  - `Medium`: 1,748 occurrences
  - `Dusty Light`: 9,135 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `Unknown`: 355 occurrences
  - `Orange`: 1,174 occurrences
  - `Black`: 10,050 occurrences
  - `Metal`: 1,023 occurrences
  - `Turquoise`: 504 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Kids Girl UW/NW`: 102 occurrences
  - `Sneakers big girl inactive from s2`: 3 occurrences
  - `EQ Divided Blue`: 1 occurrences
  - `Bags`: 355 occurrences
  - `Clean Lingerie`: 204 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `F`: 4,717 occurrences
  - `D`: 7,111 occurrences
  - `I`: 2,471 occurrences
  - `B`: 3,919 occurrences
  - `H`: 2,832 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Menswear`: 4,717 occurrences
  - `Children Sizes 92-140`: 2,832 occurrences
  - `Baby Sizes 50-98`: 2,428 occurrences
  - `Ladieswear`: 12,862 occurrences
  - `Lingeries/Tights`: 3,919 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Baby/Children`: 8,887 occurrences
  - `Divided`: 7,111 occurrences
  - `Ladieswear`: 20,255 occurrences
  - `Sport`: 1,328 occurrences
  - `Menswear`: 4,717 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Womens Tailoring`: 1,805 occurrences
  - `Womens Everyday Basics`: 807 occurrences
  - `Divided Selected`: 404 occurrences
  - `Boys Underwear & Basics`: 614 occurrences
  - `Contemporary Smart`: 718 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Trousers Denim`: 1,505 occurrences
  - `Woven/Jersey/Knitted mix Baby`: 558 occurrences
  - `Trousers`: 3,132 occurrences
  - `Under-, Nightwear`: 3,214 occurrences
  - `Socks and Tights`: 947 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Halterneck balconette bra in microfibre and lace with underwired, thickly padded cups to maximise the bust and create a fuller cleavage. Adjustable strap at the back of the neck and a hook-and-eye fastening at the back.`: 1 occurrences
  - `Double-breasted, straight-style coat in a felted wool blend with peak lapels, flap front pockets, two inner pockets and a single back vent. Lined. The wool content of the coat is recycled.`: 1 occurrences
  - `Sports vest top in soft, fast-drying functional fabric with a racer back and a shorter top in airy fabric layered over the top.`: 4 occurrences
  - `Short dress in woven fabric with a smocked bodice and square neckline with concealed elastication and a small frill trim. Short puff sleeves with smocking and a frill trim at the hems, a seam at the waist and a bell-shaped skirt. Unlined.`: 2 occurrences
  - `Blouse in a viscose weave with a small stand-up collar and button placket. Gathered yoke at the back, long sleeves with a tab and button, and a rounded hem with short slits in the sides.`: 3 occurrences

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