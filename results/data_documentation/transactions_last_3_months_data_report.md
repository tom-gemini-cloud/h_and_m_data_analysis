# Data Understanding Report

**Generated on:** 2025-08-05 15:30:02
**File:** transactions_last_3_months.parquet

## 📄 File Information

- **File Path:** `..\data\processed\transactions_last_3_months.parquet`
- **File Type:** PARQUET
- **File Size:** 52.83 MB
- **Last Modified:** 2025-08-05 13:24:06

## 📊 Dataset Overview

- **Rows:** 3,904,391
- **Columns:** 5
- **Total Cells:** 19,521,955

## 🔍 Data Quality Summary

- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 327,155 (8.38%)
  **NOTE:** These are not actually duplicates they represent multiple articles bought on the same day

## 📋 Schema Information

| Column           | Data Type | Null Count | Null % | Unique Count | Unique % |
| ---------------- | --------- | ---------- | ------ | ------------ | -------- |
| t_dat            | Date      | 0          | 0.0%   | 91           | 0.0%     |
| customer_id      | String    | 0          | 0.0%   | 525,075      | 13.45%   |
| article_id       | Int64     | 0          | 0.0%   | 42,298       | 1.08%    |
| price            | Float64   | 0          | 0.0%   | 5,622        | 0.14%    |
| sales_channel_id | Int64     | 0          | 0.0%   | 2            | 0.0%     |

## 📈 Statistical Summary (Numeric Columns)

| Column           | Count   | Mean           | Std | Min                    | 25% | 50% | 75% | Max                |
| ---------------- | ------- | -------------- | --- | ---------------------- | --- | --- | --- | ------------------ |
| article_id       | 3904391 | 791482176.6992 | N/A | 108775015              | N/A | N/A | N/A | 956217002          |
| price            | 3904391 | 0.0266         | N/A | 0.00013559322033898305 | N/A | N/A | N/A | 0.5067796610169492 |
| sales_channel_id | 3904391 | 1.653          | N/A | 1                      | N/A | N/A | N/A | 2                  |

## 📝 Categorical Column Analysis

### customer_id

- **Unique Values:** 525,075
- **Average Length:** 64.0 characters
- **Top Values:**
  - `d702d08296bf8a9deef9b48a66dfddf7d21774060248c1053adaffa790e5d766`: 7 occurrences
  - `b38f815771fa6d1a754161f193effd569dfeee321e59bb2f2b2dac0714a9784d`: 2 occurrences
  - `7723987c3160f42d45636d93ac4f4065204aa59c21b9863ceb35acdbb36e692c`: 24 occurrences
  - `ee4dc7ef4e49f96a1275aed58f38a0541a0029221d288c72ba2bf8e040f37e67`: 4 occurrences
  - `6cae7fbdb8d894f1c2136314d55fa2c1ee4b1a18936daf1bd251812e87c1fdb7`: 3 occurrences

## 💾 Memory Usage

- **Estimated Total Memory:** 342.56 MB

### Memory by Column

| Column           | Memory (MB) |
| ---------------- | ----------- |
| t_dat            | 14.8941     |
| customer_id      | 238.3051    |
| article_id       | 29.7881     |
| price            | 29.7881     |
| sales_channel_id | 29.7881     |

## 💡 Data Quality Recommendations

- **Significant duplicates found** - Review and consider deduplication

  **NOTE:** These are not actually duplicates they represent multiple articles bought on the same day. In otherwords the customer probably ordered more than 1 of the articles.

- **Low cardinality columns:** sales_channel_id - Good candidates for categorical encoding

---

_Report generated using HnM Data Analytics - Data Understanding Module_
