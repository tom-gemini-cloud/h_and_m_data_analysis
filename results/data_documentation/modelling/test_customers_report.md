# Data Understanding Report
**Generated on:** 2025-08-15 14:03:23
**File:** test_customers.parquet

## 📄 File Information
- **File Path:** `data\modelling_data\test_customers.parquet`
- **File Type:** PARQUET
- **File Size:** 3.54 MB
- **Last Modified:** 2025-08-15 14:00:36

## 📊 Dataset Overview
- **Rows:** 105,015
- **Columns:** 1
- **Total Cells:** 105,015

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| customer_id | String | 0 | 0.0% | 105,015 | 100.0% |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 105,015
- **Average Length:** 64.0 characters
- **Top Values:**
  - `322e8353b1d61a9a2d549d7290a8552c953c818aa44db2fdb1826b67c9a14df2`: 1 occurrences
  - `27a423988d35c04e710fa8cf2a0da6be713ca0e0890a3cf3022ea4f0c6c1b81f`: 1 occurrences
  - `5e2f173b1f993327fe15537cbd4880f9f40e8a6311b33d9956a7ab057f5da852`: 1 occurrences
  - `da4dc4d97c66d76c243bb7c10a7489163c615be195c2a74784b75f75d55b95aa`: 1 occurrences
  - `ac50f752976ea4a3f4a564905df99c4f7b0eb7ef9f862e94d3cc8695ae2857e7`: 1 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 6.41 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 6.4096 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers

---
*Report generated using HnM Data Analytics - Data Understanding Module*