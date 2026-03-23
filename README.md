# 📊 Retail Sales Data Cleaning & Feature Engineering

A end-to-end data cleaning and feature engineering mini-project using a retail sales dataset. The notebook covers exploratory data analysis (EDA), null value handling, duplicate detection, data type fixing, and customer-level feature creation.

---

## 📁 Project Structure

```
├── Data_Cleaning_P1.ipynb   # Main Jupyter notebook
├── SQL_Sale.csv             # Source dataset
└── README.md
```

---

## 🗂️ Dataset

**File:** `SQL_Sale.csv`  
**Rows:** 2,000 transactions  
**Columns:** 11

| Column | Description |
|---|---|
| `transactions_id` | Unique transaction identifier |
| `sale_date` | Date of the sale |
| `sale_time` | Time of the sale |
| `customer_id` | Customer identifier |
| `gender` | Customer gender |
| `age` | Customer age |
| `category` | Product category (Clothing, Beauty, Electronics) |
| `quantiy` | Quantity purchased *(note: typo in source data)* |
| `price_per_unit` | Price per unit |
| `cogs` | Cost of goods sold |
| `total_sale` | Total sale amount |

---

## 🔍 Notebook Walkthrough

### 1. Exploratory Data Analysis (EDA)
- Load the dataset using `pd.read_csv()`
- Inspect data with `.head()`, `.tail()`, `.sample()`, `.info()`, `.shape()`, `.columns`, `.describe()`, `.nunique()`

### 2. Handling Missing Values
Null counts identified:

| Column | Null Count |
|---|---|
| `age` | 10 |
| `quantiy` | 3 |
| `price_per_unit` | 3 |
| `cogs` | 3 |
| `total_sale` | 3 |

**Strategy:** All missing values are filled using **median imputation** via a loop over affected columns. A working copy `df2` is created to preserve the original dataframe.

### 3. Duplicate Detection
- Checked using `df2.duplicated()`
- No duplicates found in the dataset

### 4. Data Type Fixing
- `age` column cast to `float64` using `.astype(float)`
- `sale_date` and `sale_time` remain as `object` (strings)

### 5. Feature Engineering

| New Feature | Description |
|---|---|
| `total_amount` | `quantity × price_per_unit` |
| `value_status` | `"High Value"` if `total_sale > 1000`, else `"Low Value"` |
| `customer_total` (CLV) | Total spending per customer across all transactions |
| `purchase_freq` | Number of purchases per customer |
| `buyer_type` | `"Frequent Buyer"` if `purchase_freq > 10`, else `"Occasional Buyer"` |
| `AOV` | Average Order Value — mean `total_sale` per customer |

---

## 🛠️ Tech Stack

- **Python 3.13**
- **pandas** — data manipulation
- **numpy** — numerical operations
- **Jupyter Notebook**

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy jupyter
```

### Run the Notebook

```bash
jupyter notebook Data_Cleaning_P1.ipynb
```

Make sure `SQL_Sale.csv` is in the same directory as the notebook before running.

---

## 📌 Notes

- The column `quantiy` is a typo in the source data (should be `quantity`) — kept as-is to match the original dataset.
- `df2` is a working copy of the original `df` — all cleaning and feature engineering is applied to `df2`.
- The `clv` / `customer_total` columns were created at different stages; the final retained column is `customer_total`.


---

## 📬 Author

**Muhammad Talha**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/muhammad-talha12b/)

---

> _If you found this project helpful, please consider giving it a ⭐ on GitHub!_
