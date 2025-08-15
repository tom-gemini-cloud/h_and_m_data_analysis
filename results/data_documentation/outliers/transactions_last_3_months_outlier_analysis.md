# Outlier Analysis Report

**Generated on:** 2025-08-09 12:33:41
**File:** transactions_last_3_months.parquet
**Dataset Shape:** 3,904,391 rows × 5 columns
**Numerical Columns Analysed:** 1

## 📊 Executive Summary

**⚠️ Moderate Priority**: 1 columns with 1-5% outliers:
- price (3.9%)


## 🔍 Outlier Detection Methods

This analysis employs four complementary statistical methods:

1. **Interquartile Range (IQR)**: Values beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR
2. **Z-Score**: Values with |z-score| > 3.0 standard deviations from mean
3. **Modified Z-Score**: Uses median absolute deviation, |modified z-score| > 3.5
4. **Percentile**: Values below 1st percentile or above 99th percentile

## 📈 Detailed Analysis by Column

### price

#### Statistical Summary

| Metric | Value |
| ------ | ----- |
| Total Values | 3,904,391 |
| Min Value | 0.000136 |
| Max Value | 0.506780 |
| Mean | 0.026647 |
| Standard Deviation | 0.018024 |
| Q1 (25th percentile) | 0.015237 |
| Q3 (75th percentile) | 0.033881 |
| IQR | 0.018644 |

#### Outlier Detection Results

| Method | Outliers | Percentage | Bounds/Threshold |
| ------ | -------- | ---------- | ---------------- |
| IQR (1.5×) | 153,189 | 3.92% | [-0.012729, 0.061847] |
| Z-Score (±3.0) | 61,111 | 1.57% | μ±3σ |
| Modified Z-Score (±3.5) | 64,932 | 1.66% | MAD-based |
| Percentile (1%-99%) | 68,196 | 1.75% | [0.003542, 0.084729] |

#### Recommendations

- **Some outliers (3.9%)** - Investigate extreme values
- **Extremely wide range** - Likely contains data entry errors or different units
- **Methods show different outlier counts** - Data may have complex distribution

---

## 💡 Data Cleaning Recommendations

### Priority Actions

- **price**: **Some outliers (3.9%)** - Investigate extreme values
- **price**: **Extremely wide range** - Likely contains data entry errors or different units
- **price**: **Methods show different outlier counts** - Data may have complex distribution

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