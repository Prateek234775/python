# 📘 Day 14 – Data Cleaning

## 🎯 Objective

Learn:
- Missing values
- Duplicate data
- Data cleaning techniques

---

# Why Data Cleaning?

Real-world data is messy.

Problems:
- Missing values
- Duplicate rows
- Incorrect values

Cleaning data is one of the most important tasks in Data Science.

---

# Missing Values

Check missing values:

```python
df.isnull()
```

Count missing values:

```python
df.isnull().sum()
```

---

# Remove Missing Values

```python
df.dropna()
```

---

# Fill Missing Values

```python
df["Marks"] = df["Marks"].fillna(0)
```

---

# Duplicate Data

Check duplicates:

```python
df.duplicated()
```

Remove duplicates:

```python
df.drop_duplicates()
```

---

# Skills Learned

✅ Detect missing values

✅ Fill missing values

✅ Remove duplicates

✅ Clean datasets

---

# Real World Importance

Every AI/ML project requires:
- clean data
- proper preprocessing
- handling missing values

Without cleaning:
❌ ML models perform badly

---

# Next Topic

Day 15:
- Data Visualization
- Matplotlib
- Charts & Graphs