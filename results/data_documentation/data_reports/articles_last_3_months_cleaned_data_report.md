# Data Understanding Report
**Generated on:** 2025-08-11 08:15:27
**File:** articles_last_3_months_cleaned.parquet

## 📄 File Information
- **File Path:** `../data/cleaned/articles_last_3_months_cleaned.parquet`
- **File Type:** PARQUET
- **File Size:** 108.87 MB
- **Last Modified:** 2025-08-11 08:15:25

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
  - `Misses bucket`: 1 occurrences
  - `Caroline tulle`: 1 occurrences
  - `Pimento dress`: 1 occurrences
  - `Stella Wireless top`: 1 occurrences
  - `4p Elastic Headband (1)`: 1 occurrences

### product_type_name
- **Unique Values:** 124
- **Top Values:**
  - `Watch`: 16 occurrences
  - `Braces`: 3 occurrences
  - `Eyeglasses`: 2 occurrences
  - `Bra`: 1,089 occurrences
  - `Mobile case`: 4 occurrences

### product_group_name
- **Unique Values:** 18
- **Top Values:**
  - `Swimwear`: 1,820 occurrences
  - `Nightwear`: 631 occurrences
  - `Stationery`: 4 occurrences
  - `Garment Full body`: 5,796 occurrences
  - `Furniture`: 1 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Top Values:**
  - `Melange`: 2,161 occurrences
  - `Metallic`: 147 occurrences
  - `Placement print`: 878 occurrences
  - `Argyle`: 3 occurrences
  - `Dot`: 305 occurrences

### colour_group_name
- **Unique Values:** 50
- **Top Values:**
  - `Blue`: 1,383 occurrences
  - `Purple`: 99 occurrences
  - `Other Red`: 34 occurrences
  - `Other Pink`: 218 occurrences
  - `Yellowish Brown`: 744 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Top Values:**
  - `Dusty Light`: 9,135 occurrences
  - `Medium`: 1,748 occurrences
  - `Medium Dusty`: 5,777 occurrences
  - `Light`: 6,424 occurrences
  - `Dark`: 16,807 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Top Values:**
  - `White`: 5,542 occurrences
  - `Green`: 1,339 occurrences
  - `Red`: 1,635 occurrences
  - `Yellowish Green`: 5 occurrences
  - `Beige`: 2,972 occurrences

### department_name
- **Unique Values:** 238
- **Top Values:**
  - `Hair Accessories`: 447 occurrences
  - `Blouse & Dress`: 463 occurrences
  - `AK Bottoms`: 57 occurrences
  - `Light Basic Jersey`: 355 occurrences
  - `Test Ladies`: 3 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `F`: 4,717 occurrences
  - `J`: 1,156 occurrences
  - `G`: 2,428 occurrences
  - `D`: 7,111 occurrences
  - `S`: 1,328 occurrences

### index_name
- **Unique Values:** 10
- **Top Values:**
  - `Children Sizes 134-170`: 2,471 occurrences
  - `Lingeries/Tights`: 3,919 occurrences
  - `Children Accessories, Swimwear`: 1,156 occurrences
  - `Divided`: 7,111 occurrences
  - `Menswear`: 4,717 occurrences

### index_group_name
- **Unique Values:** 5
- **Top Values:**
  - `Baby/Children`: 8,887 occurrences
  - `Ladieswear`: 20,255 occurrences
  - `Sport`: 1,328 occurrences
  - `Divided`: 7,111 occurrences
  - `Menswear`: 4,717 occurrences

### section_name
- **Unique Values:** 56
- **Top Values:**
  - `Collaborations`: 121 occurrences
  - `Men Other 2`: 7 occurrences
  - `EQ Divided`: 1 occurrences
  - `Men Project`: 25 occurrences
  - `Men Suits & Tailoring`: 572 occurrences

### garment_group_name
- **Unique Values:** 21
- **Top Values:**
  - `Dresses Ladies`: 2,513 occurrences
  - `Trousers Denim`: 1,505 occurrences
  - `Shirts`: 748 occurrences
  - `Woven/Jersey/Knitted mix Baby`: 558 occurrences
  - `Dresses/Skirts girls`: 418 occurrences

### detail_desc
- **Unique Values:** 19,739
- **Top Values:**
  - `Pyjamas with a top and shorts in soft viscose jersey. Top with a slightly wider neckline and short, lace-trimmed raglan sleeves. The design includes a double layer at the top to help retain warmth while allowing easier nursing access. Short shorts with a low, wrapover waist with covered elastication, and lace-trimmed hems.`: 2 occurrences
  - `5-pocket trousers in stretch cotton twill with a regular waist, zip fly and skinny legs.`: 6 occurrences
  - `Fitted, long-sleeved top in ribbed cotton jersey with a V-neck and sewn-in wrapover at the front.`: 3 occurrences
  - `Double-breasted trenchcoat in soft twill made from cotton and Tencel™ lyocell with wide peak lapels, gently dropped shoulders and long puff sleeves with a detachable, adjustable buttoned strap at the cuffs. Front pockets, a wide, detachable belt with metal eyelets at the waist, and a single back vent. Half-lined.`: 1 occurrences
  - `Body in mesh and lace with a push-up bra. Underwired, padded cups for a larger bust and fuller cleavage, adjustable shoulder straps and a hook-and-eye fastening at the back. Lined gusset with concealed press-studs and cutaway coverage at the back.`: 2 occurrences

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