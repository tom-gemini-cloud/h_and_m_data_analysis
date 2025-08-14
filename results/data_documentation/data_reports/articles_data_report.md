# Data Understanding Report
**Generated on:** 2025-08-14 20:24:52
**File:** articles.csv

## 📄 File Information
- **File Path:** `data\raw\articles.csv`
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
| product_code | 105542 | 698424.5634 | N/A | 108775 | N/A | N/A | N/A | 959461 |
| product_type_no | 105542 | 234.8619 | N/A | -1 | N/A | N/A | N/A | 762 |
| graphical_appearance_no | 105542 | 1009515.0757 | N/A | -1 | N/A | N/A | N/A | 1010029 |
| colour_group_code | 105542 | 32.2338 | N/A | -1 | N/A | N/A | N/A | 93 |
| department_no | 105542 | 4532.7778 | N/A | 1201 | N/A | N/A | N/A | 9989 |
| index_group_no | 105542 | 3.1715 | N/A | 1 | N/A | N/A | N/A | 26 |
| section_no | 105542 | 42.6642 | N/A | 2 | N/A | N/A | N/A | 97 |
| garment_group_no | 105542 | 1010.4383 | N/A | 1001 | N/A | N/A | N/A | 1025 |

## 📝 Categorical Column Analysis
### prod_name
- **Unique Values:** 45,875
- **Average Length:** 15.54 characters
- **Top Values:**
  - `Premium Missy leggings`: 2 occurrences
  - `COLAB NL Espadrille BG`: 1 occurrences
  - `Adele LS`: 2 occurrences
  - `Mercury Stripe Sweater`: 1 occurrences
  - `Ragdoll fur collar`: 1 occurrences

### product_type_name
- **Unique Values:** 131
- **Average Length:** 7.53 characters
- **Top Values:**
  - `Boots`: 1,028 occurrences
  - `Flat shoe`: 165 occurrences
  - `Jumpsuit/Playsuit`: 1,147 occurrences
  - `Swimwear set`: 192 occurrences
  - `Robe`: 136 occurrences

### product_group_name
- **Unique Values:** 19
- **Average Length:** 15.44 characters
- **Top Values:**
  - `Socks & Tights`: 2,442 occurrences
  - `Interior textile`: 3 occurrences
  - `Garment Upper body`: 42,741 occurrences
  - `Shoes`: 5,283 occurrences
  - `Unknown`: 121 occurrences

### graphical_appearance_name
- **Unique Values:** 30
- **Average Length:** 8.29 characters
- **Top Values:**
  - `Hologram`: 8 occurrences
  - `Treatment`: 586 occurrences
  - `Transparent`: 86 occurrences
  - `Other structure`: 1,502 occurrences
  - `Argyle`: 15 occurrences

### colour_group_name
- **Unique Values:** 50
- **Average Length:** 7.48 characters
- **Top Values:**
  - `Other Turquoise`: 14 occurrences
  - `Light Yellow`: 984 occurrences
  - `Dark Orange`: 886 occurrences
  - `Other Purple`: 46 occurrences
  - `Light Turquoise`: 1,027 occurrences

### perceived_colour_value_name
- **Unique Values:** 8
- **Average Length:** 6.81 characters
- **Top Values:**
  - `Dark`: 42,706 occurrences
  - `Medium Dusty`: 12,630 occurrences
  - `Unknown`: 28 occurrences
  - `Light`: 15,739 occurrences
  - `Dusty Light`: 22,152 occurrences

### perceived_colour_master_name
- **Unique Values:** 20
- **Average Length:** 4.92 characters
- **Top Values:**
  - `Red`: 5,878 occurrences
  - `Blue`: 18,469 occurrences
  - `Turquoise`: 1,829 occurrences
  - `Unknown`: 685 occurrences
  - `Beige`: 5,657 occurrences

### department_name
- **Unique Values:** 250
- **Average Length:** 13.14 characters
- **Top Values:**
  - `Ladies Sport Woven`: 172 occurrences
  - `Shirt Extended inactive from s1`: 1 occurrences
  - `Shopbasket Lingerie`: 56 occurrences
  - `Kids Boy Outdoor`: 394 occurrences
  - `Men Sport Woven`: 300 occurrences

### index_code
- **Unique Values:** 10
- **Average Length:** 1.0 characters
- **Top Values:**
  - `C`: 6,961 occurrences
  - `J`: 4,615 occurrences
  - `D`: 15,149 occurrences
  - `A`: 26,001 occurrences
  - `F`: 12,553 occurrences

### index_name
- **Unique Values:** 10
- **Average Length:** 13.76 characters
- **Top Values:**
  - `Children Accessories, Swimwear`: 4,615 occurrences
  - `Ladies Accessories`: 6,961 occurrences
  - `Children Sizes 134-170`: 9,214 occurrences
  - `Menswear`: 12,553 occurrences
  - `Ladieswear`: 26,001 occurrences

### index_group_name
- **Unique Values:** 5
- **Average Length:** 10.16 characters
- **Top Values:**
  - `Divided`: 15,149 occurrences
  - `Menswear`: 12,553 occurrences
  - `Baby/Children`: 34,711 occurrences
  - `Sport`: 3,392 occurrences
  - `Ladieswear`: 39,737 occurrences

### section_name
- **Unique Values:** 56
- **Average Length:** 16.74 characters
- **Top Values:**
  - `Ladies Other`: 4 occurrences
  - `Men Suits & Tailoring`: 1,428 occurrences
  - `Young Boy`: 2,352 occurrences
  - `Divided Projects`: 2,364 occurrences
  - `Contemporary Street`: 1,490 occurrences

### garment_group_name
- **Unique Values:** 21
- **Average Length:** 10.95 characters
- **Top Values:**
  - `Jersey Fancy`: 21,445 occurrences
  - `Outdoor`: 4,501 occurrences
  - `Blouses`: 5,838 occurrences
  - `Jersey Basic`: 8,126 occurrences
  - `Special Offers`: 1,061 occurrences

### detail_desc
- **Unique Values:** 43,405
- **Average Length:** 142.16 characters
- **Top Values:**
  - `Long-sleeved dress in lightweight sweatshirt fabric with frills down the front, a gathered seam at the waist and a flared skirt. Unlined. The cotton content of the dress is organic.`: 6 occurrences
  - `Cardigan in a soft, loose, textured knit with 3/4-length sleeves with sewn-in turn-ups. No buttons.`: 7 occurrences
  - `Pyjamas in soft, stretch cotton jersey. V-neck top with narrow, adjustable shoulder straps and a lace trim at the top. Straight-cut bottoms with an elasticated waist and lace-trimmed hems.`: 1 occurrences
  - `Padded ski trousers in windproof, water-repellent functional fabric with closed, waterproof seams at critical points. Reinforced at the knees, hems and back. Zip fly and press-stud, zipped side pockets, a back pocket with a button, and detachable, adjustable elastic braces. Lined. The trousers have a water-repellent coating without fluorocarbons.`: 1 occurrences
  - `Fitted top in airy, ribbed jersey with a V-neck, decorative buttons at the top and long sleeves.`: 2 occurrences

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