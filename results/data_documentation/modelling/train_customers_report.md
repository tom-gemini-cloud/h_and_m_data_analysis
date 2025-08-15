# Data Understanding Report
**Generated on:** 2025-08-15 14:03:23
**File:** train_customers.parquet

## 📄 File Information
- **File Path:** `data\modelling_data\train_customers.parquet`
- **File Type:** PARQUET
- **File Size:** 14.16 MB
- **Last Modified:** 2025-08-15 14:00:36

## 📊 Dataset Overview
- **Rows:** 420,060
- **Columns:** 1
- **Total Cells:** 420,060

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| customer_id | String | 0 | 0.0% | 420,060 | 100.0% |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 420,060
- **Average Length:** 64.0 characters
- **Top Values:**
  - `1b4124fb61495a9acc3dcd99b50852f89f694a89a1698cc2ffb75dae988d5400`: 1 occurrences
  - `7e0fdf0556d37e136bd359baf72d903a43634e6a47f122c414178e4f7d9d96f8`: 1 occurrences
  - `ffd5cf1df9213f4c3b1b3b8155dc10c8f39fcd328c0b3a44b4c24733b7b377d9`: 1 occurrences
  - `82a63518583fa432adcfedfe0fa37d6f510cde81b04a807bb686808a8723c01f`: 1 occurrences
  - `7d80a1d8faa6d9154e134c4d2d5fef8dd5697332ad954ef46d2f6d967ce343bf`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 25.64 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 25.6384 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers

---
*Report generated using HnM Data Analytics - Data Understanding Module*