# Outlier Analysis Report

**Generated on:** 2025-08-09 11:24:36
**File:** customers_last_3_months.parquet
**Dataset Shape:** 525,075 rows × 7 columns
**Numerical Columns Analysed:** 3

## 📊 Executive Summary

**✅ Clean Data**: 3 columns with <1% outliers


## 🔍 Outlier Detection Methods

This analysis employs four complementary statistical methods:

1. **Interquartile Range (IQR)**: Values beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR
2. **Z-Score**: Values with |z-score| > 3.0 standard deviations from mean
3. **Modified Z-Score**: Uses median absolute deviation, |modified z-score| > 3.5
4. **Percentile**: Values below 1st percentile or above 99th percentile

## 📈 Detailed Analysis by Column

### FN

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 525,075 |
| Min Value | 1.000000 |
| Max Value | 1.000000 |
| Mean | 1.000000 |
| Standard Deviation | 0.000000 |
| Q1 (25th percentile) | 1.000000 |
| Q3 (75th percentile) | 1.000000 |
| IQR | 0.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 0 | 0.00% | [1.000000, 1.000000] |
| Z-Score (±3.0) | 0 | 0.00% | μ±3σ |
| Modified Z-Score (±3.5) | 0 | 0.00% | MAD-based |
| Percentile (1%-99%) | 0 | 0.00% | [1.000000, 1.000000] |

#### Recommendations

- **Clean data** - No significant outlier issues detected

---

### Active

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 525,075 |
| Min Value | 1.000000 |
| Max Value | 1.000000 |
| Mean | 1.000000 |
| Standard Deviation | 0.000000 |
| Q1 (25th percentile) | 1.000000 |
| Q3 (75th percentile) | 1.000000 |
| IQR | 0.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 0 | 0.00% | [1.000000, 1.000000] |
| Z-Score (±3.0) | 0 | 0.00% | μ±3σ |
| Modified Z-Score (±3.5) | 0 | 0.00% | MAD-based |
| Percentile (1%-99%) | 0 | 0.00% | [1.000000, 1.000000] |

#### Recommendations

- **Clean data** - No significant outlier issues detected

---

### age

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 525,075 |
| Min Value | 16.000000 |
| Max Value | 99.000000 |
| Mean | 35.047102 |
| Standard Deviation | 13.896879 |
| Q1 (25th percentile) | 24.000000 |
| Q3 (75th percentile) | 47.000000 |
| IQR | 23.000000 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 200 | 0.04% | [-10.500000, 81.500000] |
| Z-Score (±3.0) | 825 | 0.16% | μ±3σ |
| Modified Z-Score (±3.5) | 825 | 0.16% | MAD-based |
| Percentile (1%-99%) | 10,123 | 1.93% | [18.000000, 69.000000] |

#### Recommendations

- **Clean data** - No significant outlier issues detected

---

## 💡 Data Cleaning Recommendations

### Priority Actions

- **Overall**: Dataset appears clean with minimal outlier concerns

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