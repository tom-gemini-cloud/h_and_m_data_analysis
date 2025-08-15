# Data Understanding Report
**Generated on:** 2025-08-15 18:32:43
**File:** customers_features_final.parquet
**Note:** Analysis based on sample of 50,000 records

## 📄 File Information
- **File Path:** `../data/features/final/customers_features_final.parquet`
- **File Type:** PARQUET
- **File Size:** 81.95 MB
- **Last Modified:** 2025-08-15 18:32:42

## 📊 Dataset Overview
- **Rows:** 50,000
- **Columns:** 16
- **Total Cells:** 800,000

## 🔍 Data Quality Summary
- **Completeness Score:** 100.0%
- **Missing Values:** 0 (0.0%)
- **Duplicate Rows:** 0 (0.0%)

## 📋 Schema Information
| Column | Data Type | Null Count | Null % | Unique Count | Unique % |
|--------|-----------|------------|---------|--------------|----------|
| customer_id | String | 0 | 0.0% | 50,000 | 100.0% |
| FN | Float64 | 0 | 0.0% | 2 | 0.0% |
| Active | Float64 | 0 | 0.0% | 2 | 0.0% |
| club_member_status | Categorical | 0 | 0.0% | 4 | 0.01% |
| fashion_news_frequency | Categorical | 0 | 0.0% | 3 | 0.01% |
| age | Float64 | 0 | 0.0% | 72 | 0.14% |
| postal_code | Categorical | 0 | 0.0% | 43,606 | 87.21% |
| recency | Int64 | 0 | 0.0% | 91 | 0.18% |
| frequency | UInt32 | 0 | 0.0% | 126 | 0.25% |
| monetary | Float64 | 0 | 0.0% | 26,050 | 52.1% |
| purchase_diversity_score | Float64 | 0 | 0.0% | 4,295 | 8.59% |
| price_sensitivity_index | Float64 | 0 | 0.0% | 31,061 | 62.12% |
| colour_preference_entropy | Float64 | 0 | 0.0% | 4,716 | 9.43% |
| style_consistency_score | Float64 | 0 | 0.0% | 5,060 | 10.12% |
| dataset_created_at | String | 0 | 0.0% | 1 | 0.0% |
| created_by | String | 0 | 0.0% | 1 | 0.0% |

## 📈 Statistical Summary (Numeric Columns)
| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| FN | 50000 | 0.4206 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| Active | 50000 | 0.4131 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |
| age | 50000 | 35.0329 | N/A | 16.0 | N/A | N/A | N/A | 92.0 |
| recency | 50000 | 38.2717 | N/A | 1 | N/A | N/A | N/A | 91 |
| monetary | 50000 | 204.6296 | N/A | 2.39 | N/A | N/A | N/A | 10500.579999999987 |
| purchase_diversity_score | 50000 | 0.9613 | N/A | -0.0 | N/A | N/A | N/A | 3.094588496642341 |
| price_sensitivity_index | 50000 | 0.4689 | N/A | 0.0 | N/A | N/A | N/A | 2.502406831175997 |
| colour_preference_entropy | 50000 | 1.4587 | N/A | -0.0 | N/A | N/A | N/A | 4.249743855419998 |
| style_consistency_score | 50000 | 0.3288 | N/A | 0.0 | N/A | N/A | N/A | 1.0 |

## 📝 Categorical Column Analysis
### customer_id
- **Unique Values:** 50,000
- **Average Length:** 64.0 characters
- **Top Values:**
  - `ae58b44c69873b890c72d7b0bc63d25a4b31a38478f06a80cc6a553dba2954c9`: 1 occurrences
  - `d49e40dcd0ffa905ce4b5708fc069f27bbee8547fa8752151a66000272f10bdb`: 1 occurrences
  - `c8800a5662abc5b5f5a416524e78332a70cc4dbdba929493521415b94ac7782f`: 1 occurrences
  - `e733651dbfd9d1fa7acad6f69afb4599035747aca73d3b74de180da8a384471b`: 1 occurrences
  - `e5341990108c4542bf5f383fae6121a6b3942fc75a18fb5e075457a4c79f9ec6`: 1 occurrences

### club_member_status
- **Unique Values:** 4
- **Top Values:**
  - `LEFT CLUB`: 6 occurrences
  - `ACTIVE`: 48,891 occurrences
  - `PRE-CREATE`: 1,032 occurrences
  - `NONE`: 71 occurrences

### fashion_news_frequency
- **Unique Values:** 3
- **Top Values:**
  - `Regularly`: 21,065 occurrences
  - `NONE`: 28,921 occurrences
  - `Monthly`: 14 occurrences

### postal_code
- **Unique Values:** 43,606
- **Top Values:**
  - `f2e545e054068651874a02572e39d598114043841ca920c6b5da6ee33b7554cf`: 1 occurrences
  - `a0b15fe6aacecb4c1f3cc0033f52cc4f500798d407947183a58a52ac62d7a49e`: 1 occurrences
  - `b5425ebd9c567df6efdc76cdab9953c444e917e2424da406c11291829a5a3484`: 1 occurrences
  - `76cbf73f14cd40ffabb4e1cd89d086c56634c682c95cff2e4e060f9143ae732b`: 1 occurrences
  - `c873d025e742599ff1f770d47b29ebb1436525ba87f938071b7459b2b2afb50c`: 1 occurrences

### dataset_created_at
- **Unique Values:** 1
- **Average Length:** 26.0 characters
- **Top Values:**
  - `2025-08-15T18:32:42.029421`: 50,000 occurrences

### created_by
- **Unique Values:** 1
- **Average Length:** 34.0 characters
- **Top Values:**
  - `customer_feature_engineering.ipynb`: 50,000 occurrences

## 💾 Memory Usage
- **Estimated Total Memory:** 10.11 MB

### Memory by Column
| Column | Memory (MB) |
|--------|-------------|
| customer_id | 3.0518 |
| FN | 0.3815 |
| Active | 0.3815 |
| club_member_status | 0.1907 |
| fashion_news_frequency | 0.1907 |
| age | 0.3815 |
| postal_code | 0.1907 |
| recency | 0.3815 |
| frequency | 0.1907 |
| monetary | 0.3815 |
| purchase_diversity_score | 0.3815 |
| price_sensitivity_index | 0.3815 |
| colour_preference_entropy | 0.3815 |
| style_consistency_score | 0.3815 |
| dataset_created_at | 1.2398 |
| created_by | 1.6212 |

## 💡 Data Quality Recommendations
- **Potential ID columns detected:** customer_id - Verify if these should be used as identifiers
- **Low cardinality columns:** FN, Active, club_member_status, fashion_news_frequency - Good candidates for categorical encoding

---
*Report generated using HnM Data Analytics - Data Understanding Module*