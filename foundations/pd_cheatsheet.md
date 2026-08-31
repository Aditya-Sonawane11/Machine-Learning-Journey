# 🐼 Pandas Cheat Sheet for Machine Learning

```python
import pandas as pd
```

---

# 📌 1. Reading Data

### Read CSV

```python
df = pd.read_csv("data.csv")
```

**Does:** Loads a CSV file into a DataFrame.

**Returns:** DataFrame

---

### Read Excel

```python
df = pd.read_excel("data.xlsx")
```

**Does:** Loads an Excel file.

**Returns:** DataFrame

---

# 📌 2. Viewing Data

### First 5 rows

```python
df.head()
```

**Does:** Shows the first 5 rows.

**Returns:** DataFrame

---

### Last 5 rows

```python
df.tail()
```

**Does:** Shows the last 5 rows.

**Returns:** DataFrame

---

### Shape

```python
df.shape
```

**Does:** Returns dataset dimensions.

**Returns:**

```python
(rows, columns)
```

Example

```python
(20640, 10)
```

---

### Column Names

```python
df.columns
```

**Does:** Lists all column names.

**Returns:** Index object

Example

```python
Index(['Age', 'Salary', 'City'])
```

---

### Information

```python
df.info()
```

**Does:**

Shows

- Number of rows
- Number of columns
- Data types
- Missing values
- Memory usage

**Returns:** Prints summary (returns `None`)

---

### Statistical Summary

```python
df.describe()
```

**Does:** Gives summary statistics for numerical columns.

Returns

- Mean
- Std
- Min
- Max
- Quartiles

---

# 📌 3. Selecting Data

### Single Column

```python
df["Age"]
```

**Does:** Selects one column.

**Returns:** Series

---

### Multiple Columns

```python
df[["Age", "Salary"]]
```

**Does:** Selects multiple columns.

**Returns:** DataFrame

---

# 📌 4. Indexing

### iloc (Integer Location)

```python
df.iloc[0]
```

**Does:** Selects the first row using row number.

**Returns:** Series

---

```python
df.iloc[0:5]
```

**Does:** Selects first five rows.

**Returns:** DataFrame

---

```python
df.iloc[0,2]
```

**Does:** Selects one cell using row and column number.

**Returns:** Single value

---

### loc (Label Location)

```python
df.loc[0]
```

**Does:** Selects row whose index label is 0.

---

```python
df.loc[:, "Age"]
```

**Does:** Selects the entire Age column.

**Returns:** Series

---

# 📌 5. Filtering Rows

```python
df[df["Age"] > 30]
```

**Does:** Keeps only rows satisfying the condition.

**Returns:** DataFrame

---

Multiple conditions

```python
df[(df["Age"] > 30) & (df["Salary"] > 50000)]
```

Use

```python
&
|
~
```

instead of

```python
and
or
not
```

---

# 📌 6. Missing Values

### Find Missing Values

```python
df.isnull()
```

**Does:** Shows whether each value is missing.

**Returns:** Boolean DataFrame

---

### Count Missing Values

```python
df.isnull().sum()
```

**Does:** Counts missing values column-wise.

**Returns:** Series

---

### Fill Missing Values

```python
df.fillna(0)
```

**Does:** Replaces missing values.

**Returns:** New DataFrame

---

```python
df["Age"].fillna(df["Age"].mean())
```

**Does:** Replaces missing ages with the average age.

---

### Remove Missing Values

```python
df.dropna()
```

**Does:** Removes rows containing missing values.

---

# 📌 7. Sorting

```python
df.sort_values("Salary")
```

**Does:** Sorts by Salary.

---

Descending

```python
df.sort_values("Salary", ascending=False)
```

---

# 📌 8. Creating Columns

```python
df["Yearly Salary"] = df["Salary"] * 12
```

**Does:** Creates a new column.

---

# 📌 9. Renaming Columns

```python
df.rename(columns={"Salary":"Monthly Salary"})
```

**Does:** Renames columns.

---

# 📌 10. Dropping Columns

```python
df.drop(columns=["Salary"])
```

**Does:** Removes unwanted columns.

---

# 📌 11. Unique Values

```python
df["Gender"].unique()
```

**Does:** Returns unique values.

Example

```python
['Male', 'Female']
```

---

### Count Unique Values

```python
df["Gender"].value_counts()
```

**Does:** Counts frequency of each unique value.

Example

```python
Male      500
Female    480
```

---

# 📌 12. GroupBy ⭐

```python
df.groupby("Department")["Salary"].mean()
```

**Does:** Groups data by Department and calculates average salary.

Very useful for data analysis.

---

# 📌 13. Apply Function

```python
df["Salary"].apply(lambda x: x * 12)
```

**Does:** Applies a function to every value.

---

# 📌 14. Duplicates

### Check

```python
df.duplicated()
```

**Does:** Finds duplicate rows.

Returns

```python
True / False
```

---

### Remove

```python
df.drop_duplicates()
```

**Does:** Removes duplicate rows.

---

# 📌 15. Correlation

```python
df.corr(numeric_only=True)
```

**Does:** Calculates correlation between numerical columns.

Returns

```python
Correlation Matrix
```

Useful before training ML models.

---

# 📌 16. Merge DataFrames

```python
pd.merge(df1, df2, on="ID")
```

**Does:** Combines two DataFrames using a common column.

---

# 📌 17. Save Data

```python
df.to_csv("cleaned.csv", index=False)
```

**Does:** Saves DataFrame as CSV.

---

# 📌 18. Most Used Attributes

| Attribute | Meaning |
|------------|---------|
| `shape` | Dataset dimensions |
| `columns` | Column names |
| `index` | Row labels |
| `dtypes` | Data types |
| `values` | NumPy array of data |

---

# 📌 19. Typical ML Workflow

```text
Read CSV
    │
    ▼
head()
info()
describe()
shape
    │
    ▼
Handle Missing Values
    │
    ▼
Filter Rows
    │
    ▼
Create New Features
    │
    ▼
Group / Analyze
    │
    ▼
Correlation
    │
    ▼
Save Clean Data
```

---

# ⭐ Pandas Functions You'll Use Most

| Function | What it does |
|----------|--------------|
| `pd.read_csv()` | Load CSV file |
| `head()` | First 5 rows |
| `tail()` | Last 5 rows |
| `info()` | Dataset information |
| `describe()` | Summary statistics |
| `shape` | Dataset dimensions |
| `columns` | Column names |
| `iloc[]` | Integer indexing |
| `loc[]` | Label indexing |
| `isnull().sum()` | Count missing values |
| `fillna()` | Fill missing values |
| `dropna()` | Remove missing values |
| `sort_values()` | Sort rows |
| `groupby()` | Aggregate grouped data |
| `value_counts()` | Count occurrences |
| `unique()` | Unique values |
| `corr()` | Correlation matrix |
| `merge()` | Join DataFrames |
| `to_csv()` | Save DataFrame |

---

# 💡 ML Tip

Whenever you load a new dataset, run these **five commands first**:

```python
df.head()
df.info()
df.describe()
df.shape
df.isnull().sum()
```

These five commands tell you almost everything you need to know before cleaning or modeling the data.

---

# 🚀 Remember

- **NumPy** → Numerical computation
- **Pandas** → Data manipulation & cleaning
- **Matplotlib** → Data visualization

**A typical ML pipeline is:**

```text
CSV → Pandas → NumPy → Matplotlib → Scikit-Learn
```