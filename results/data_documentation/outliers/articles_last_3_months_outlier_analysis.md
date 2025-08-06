# Outlier Analysis Report

**Generated on:** 2025-08-06 13:47:25
**File:** articles_last_3_months.parquet
**Dataset Shape:** 42,298 rows × 25 columns
**Numerical Columns Analysed:** 8

## 📊 Executive Summary

**🚨 High Priority**: 1 columns with >5% outliers:
- product_type_no (24.2%)

**⚠️ Moderate Priority**: 3 columns with 1-5% outliers:
- product_code (3.0%)
- graphical_appearance_no (2.0%)
- index_group_no (3.1%)

**✅ Clean Data**: 4 columns with <1% outliers


## 🔍 Outlier Detection Methods

This analysis employs four complementary statistical methods:

1. **Interquartile Range (IQR)**: Values beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR
2. **Z-Score**: Values with |z-score| > 3.0 standard deviations from mean
3. **Modified Z-Score**: Uses median absolute deviation, |modified z-score| > 3.5
4. **Percentile**: Values below 1st percentile or above 99th percentile

## 📈 Detailed Analysis by Column

### product_code

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 42,298 |
| Min Value | 108775.000000 |
| Max Value | 956217.000000 |
| Mean | 767829.365360 |
| Standard Deviation | 123654.846711 |
| Q1 (25th percentile) | 710056.000000 |
| Q3 (75th percentile) | 859888.000000 |
| IQR | 149832.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 1,273 | 3.01% | [485308.000000, 1084636.000000] |
| Z-Score (±3.0) | 667 | 1.58% | μ±3σ |
| Modified Z-Score (±3.5) | 900 | 2.13% | MAD-based |
| Percentile (1%-99%) | 841 | 1.99% | [331474.000000, 929980.000000] |

#### Recommendations

- **Some outliers (3.0%)** - Investigate extreme values
- **Methods show different outlier counts** - Data may have complex distribution

---

### product_type_no

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 42,298 |
| Min Value | -1.000000 |
| Max Value | 762.000000 |
| Mean | 237.072438 |
| Standard Deviation | 76.201441 |
| Q1 (25th percentile) | 253.000000 |
| Q3 (75th percentile) | 272.000000 |
| IQR | 19.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 10,218 | 24.16% | [224.500000, 300.500000] |
| Z-Score (±3.0) | 299 | 0.71% | μ±3σ |
| Modified Z-Score (±3.5) | 7,332 | 17.33% | MAD-based |
| Percentile (1%-99%) | 601 | 1.42% | [59.000000, 308.000000] |

#### Recommendations

- **High outlier percentage (24.2%)** - Review data collection process
- **Extremely wide range** - Likely contains data entry errors or different units
- **Methods show different outlier counts** - Data may have complex distribution

---

### graphical_appearance_no

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 42,298 |
| Min Value | -1.000000 |
| Max Value | 1010029.000000 |
| Mean | 1009869.992860 |
| Standard Deviation | 12028.670013 |
| Q1 (25th percentile) | 1010010.000000 |
| Q3 (75th percentile) | 1010016.000000 |
| IQR | 6.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 836 | 1.98% | [1010001.000000, 1010025.000000] |
| Z-Score (±3.0) | 6 | 0.01% | μ±3σ |
| Modified Z-Score (±3.5) | 0 | 0.00% | MAD-based |
| Percentile (1%-99%) | 97 | 0.23% | [1010001.000000, 1010026.000000] |

#### Recommendations

- **Some outliers (2.0%)** - Investigate extreme values
- **Extremely wide range** - Likely contains data entry errors or different units
- **Methods show different outlier counts** - Data may have complex distribution

---

### colour_group_code

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 42,298 |
| Min Value | -1.000000 |
| Max Value | 93.000000 |
| Mean | 29.721051 |
| Standard Deviation | 27.274655 |
| Q1 (25th percentile) | 9.000000 |
| Q3 (75th percentile) | 51.000000 |
| IQR | 42.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 0 | 0.00% | [-54.000000, 114.000000] |
| Z-Score (±3.0) | 0 | 0.00% | μ±3σ |
| Modified Z-Score (±3.5) | 14,047 | 33.21% | MAD-based |
| Percentile (1%-99%) | 394 | 0.93% | [5.000000, 93.000000] |

#### Recommendations

- **Extremely wide range** - Likely contains data entry errors or different units

---

### department_no

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 42,298 |
| Min Value | 1201.000000 |
| Max Value | 9989.000000 |
| Mean | 3936.593503 |
| Standard Deviation | 2606.212622 |
| Q1 (25th percentile) | 1643.000000 |
| Q3 (75th percentile) | 5882.000000 |
| IQR | 4239.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 0 | 0.00% | [-4715.500000, 12240.500000] |
| Z-Score (±3.0) | 0 | 0.00% | μ±3σ |
| Modified Z-Score (±3.5) | 0 | 0.00% | MAD-based |
| Percentile (1%-99%) | 789 | 1.87% | [1212.000000, 9984.000000] |

#### Recommendations

- **Clean data** - No significant outlier issues detected

---

### index_group_no

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 42,298 |
| Min Value | 1.000000 |
| Max Value | 26.000000 |
| Mean | 2.806374 |
| Standard Deviation | 4.343417 |
| Q1 (25th percentile) | 1.000000 |
| Q3 (75th percentile) | 3.000000 |
| IQR | 2.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 1,328 | 3.14% | [-2.000000, 6.000000] |
| Z-Score (±3.0) | 1,328 | 3.14% | μ±3σ |
| Modified Z-Score (±3.5) | 1,328 | 3.14% | MAD-based |
| Percentile (1%-99%) | 0 | 0.00% | [1.000000, 26.000000] |

#### Recommendations

- **Some outliers (3.1%)** - Investigate extreme values

---

### section_no

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 42,298 |
| Min Value | 2.000000 |
| Max Value | 97.000000 |
| Mean | 40.149983 |
| Standard Deviation | 23.385294 |
| Q1 (25th percentile) | 15.000000 |
| Q3 (75th percentile) | 60.000000 |
| IQR | 45.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 0 | 0.00% | [-52.500000, 127.500000] |
| Z-Score (±3.0) | 0 | 0.00% | μ±3σ |
| Modified Z-Score (±3.5) | 0 | 0.00% | MAD-based |
| Percentile (1%-99%) | 364 | 0.86% | [2.000000, 79.000000] |

#### Recommendations

- **Clean data** - No significant outlier issues detected

---

### garment_group_no

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 42,298 |
| Min Value | 1001.000000 |
| Max Value | 1025.000000 |
| Mean | 1010.984940 |
| Standard Deviation | 6.611843 |
| Q1 (25th percentile) | 1005.000000 |
| Q3 (75th percentile) | 1017.000000 |
| IQR | 12.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 0 | 0.00% | [987.000000, 1035.000000] |
| Z-Score (±3.0) | 0 | 0.00% | μ±3σ |
| Modified Z-Score (±3.5) | 0 | 0.00% | MAD-based |
| Percentile (1%-99%) | 0 | 0.00% | [1001.000000, 1025.000000] |

#### Recommendations

- **Clean data** - No significant outlier issues detected

---

## 💡 Data Cleaning Recommendations

### Priority Actions

- **product_code**: **Some outliers (3.0%)** - Investigate extreme values
- **product_code**: **Methods show different outlier counts** - Data may have complex distribution
- **product_type_no**: **High outlier percentage (24.2%)** - Review data collection process
- **product_type_no**: **Extremely wide range** - Likely contains data entry errors or different units
- **product_type_no**: **Methods show different outlier counts** - Data may have complex distribution
- **graphical_appearance_no**: **Some outliers (2.0%)** - Investigate extreme values
- **graphical_appearance_no**: **Extremely wide range** - Likely contains data entry errors or different units
- **graphical_appearance_no**: **Methods show different outlier counts** - Data may have complex distribution
- **colour_group_code**: **Extremely wide range** - Likely contains data entry errors or different units
- **index_group_no**: **Some outliers (3.1%)** - Investigate extreme values

### Methodology Notes

- **IQR Method**: Most robust for skewed distributions
- **Z-Score**: Assumes normal distribution, sensitive to extreme outliers
- **Modified Z-Score**: More robust than standard z-score, uses median
- **Percentile**: Simple and intuitive, good for business rules

### Next Steps

1. **Investigate** extreme values identified by multiple methods
2. **Validate** business logic for outlier values
3. **Consider** transformation techniques (log, Box-Cox) for skewed data
4. **Document** outlier handling decisions for reproducibility

---

_Report generated using H&M Data Analytics - Outlier Analysis Module_