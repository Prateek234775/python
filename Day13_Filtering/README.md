# 📘 Day 13 – Filtering & Sorting Data

## 🎯 Objective

Learn how to:

- Select columns
- Filter rows
- Apply conditions
- Sort datasets

---

# Selecting Columns

```python
df["Name"]
```

Multiple columns:

```python
df[["Name", "Marks"]]
```

---

# Filtering

Students scoring above 80:

```python
df[df["Marks"] > 80]
```

---

# Multiple Conditions

```python
df[(df["Marks"] > 80) & (df["Age"] > 20)]
```

---

# Sorting

Ascending:

```python
df.sort_values("Marks")
```

Descending:

```python
df.sort_values("Marks", ascending=False)
```

---

# Skills Learned

✅ Column selection

✅ Data filtering

✅ Multiple conditions

✅ Sorting

---

# Real World Use

These operations are used daily by:

- Data Scientists
- ML Engineers
- Business Analysts

---

# Next Topic

Day 14:
- Data Cleaning
- Missing Values
- Duplicate Values