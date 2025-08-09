# Data Understanding Report
**Generated on:** 2025-08-09 12:33:41
**File:** transactions_last_3_months.parquet

## 📄 File Information
- **File Path:** `..\data\processed\transactions_last_3_months.parquet`
- **File Type:** PARQUET
- **File Size:** 52.83 MB
- **Last Modified:** 2025-08-09 11:18:04

## 📊 Dataset Overview
- **Rows:** 3,904,391
- **Columns:** 5
- **Total Cells:** 19,521,955

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 327,155 (8.38%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| t_dat | Date | 0 | 0.0% | 91 | 0.0% |
| customer_id | String | 0 | 0.0% | 525,075 | 13.45% |
| article_id | Int64 | 0 | 0.0% | 42,298 | 1.08% |
| price | Float64 | 0 | 0.0% | 5,622 | 0.14% |
| sales_channel_id | Int64 | 0 | 0.0% | 2 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| article_id | 3904391 | 791482176.6992 | N/A | 108775015 | N/A | N/A | N/A | 956217002 |
| price | 3904391 | 0.0266 | N/A | 0.00013559322033898305 | N/A | N/A | N/A | 0.5067796610169492 |
| sales_channel_id | 3904391 | 1.653 | N/A | 1 | N/A | N/A | N/A | 2 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `d278f0d79659722af0046bf7f3864dca0fc4f008aa3cc691dbf9a628534dd6d8`: 1 occurrences
  - `675a13e1a6d442aab04d857d6ebd5cc01d653537a46d562c544beaf65b493d03`: 3 occurrences
  - `3dabf8e98a72c03474678b52a5eb26a842d4f639dcad125d3f59d4cc965c4a48`: 2 occurrences
  - `a9c6b2ef7af2422ad7dd98ce624898ae4c26ac7fb21ca5624875f0f05a5cb5f8`: 12 occurrences
  - `68ca18a481bcf71bda0894e6016b8dbcd5b4678e5a8898dca950c6c3511a98e3`: 3 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 342.56 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| t_dat | 14.8941 |
| customer_id | 238.3051 |
| article_id | 29.7881 |
| price | 29.7881 |
| sales_channel_id | 29.7881 |

## 💡 Data Quality Recommendations
- **Significant duplicates found** - Review and consider deduplication
- **Low cardinality columns:** sales_channel_id - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*