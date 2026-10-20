# 🧮 NumPy Cheat Sheet for Machine Learning

```python
import numpy as np
```

---

# 📌 1. Creating Arrays

```python
# 1D Array
a = np.array([1, 2, 3])

# 2D Array
b = np.array([
    [1, 2],
    [3, 4]
])

# Arrays of zeros
np.zeros((2, 3))

# Arrays of ones
np.ones((3, 2))

# Identity Matrix
np.eye(3)

# Range
np.arange(0, 10, 2)

# Evenly spaced values
np.linspace(0, 1, 5)
```

---

# 📌 2. Array Information

```python
a.shape      # Shape (rows, columns)
a.ndim       # Number of dimensions
a.size       # Total elements
a.dtype      # Data type
```

Example:

```python
a = np.array([1,2,3])

a.shape
# (3,)

a.ndim
# 1
```

---

# 📌 3. Indexing

```python
a[0]        # First element
a[-1]       # Last element

A[1,2]      # Row 1, Column 2
```

---

# 📌 4. Slicing

```python
a[1:4]

A[0]        # First row

A[:,1]      # Second column

A[1:,0]     # Rows after first, first column
```

---

# 📌 5. Reshaping

```python
a.reshape(2,3)

a.reshape(3,2)

a.flatten()

a.T          # Transpose
```

⚠️ Total number of elements must remain the same.

---

# 📌 6. Vectorized Operations

```python
a + 2

a - 2

a * 5

a / 2

a ** 2

np.sqrt(a)
```

No loops required.

---

# 📌 7. Operations Between Arrays

```python
a + b

a - b

a * b        # Element-wise multiplication

a / b
```

---

# 📌 8. Matrix Multiplication

```python
a @ b

np.dot(a, b)
```

Difference:

```python
a * b
```

➡️ Element-wise multiplication

```python
a @ b
```

➡️ Matrix multiplication

---

# 📌 9. Broadcasting

```python
a = np.array([1,2,3])

a + 10
```

Output

```python
[11 12 13]
```

Another example

```python
A = np.array([
    [1,2,3],
    [4,5,6]
])

A + np.array([10,20,30])
```

Output

```python
[[11 22 33]
 [14 25 36]]
```

NumPy automatically expands compatible arrays.

---

# 📌 10. Statistics

```python
np.mean(a)

np.median(a)

np.min(a)

np.max(a)

np.sum(a)

np.std(a)

np.var(a)
```

Useful during Exploratory Data Analysis (EDA).

---

# 📌 11. Boolean Indexing

```python
a[a > 5]

a[a % 2 == 0]

a[(a > 2) & (a < 10)]
```

Very useful for filtering datasets.

---

# 📌 12. Random Numbers

```python
np.random.seed(42)

np.random.rand(5)

np.random.randn(5)

np.random.randint(1, 10, 5)
```

Use `seed(42)` for reproducible results.

---

# 📌 13. Useful Utility Functions

```python
np.unique(a)

np.sort(a)

np.concatenate((a,b))

np.vstack((a,b))

np.hstack((a,b))
```

---

# 📌 14. Frequently Used Attributes

| Attribute | Meaning |
|-----------|---------|
| `shape` | Dimensions |
| `ndim` | Number of dimensions |
| `size` | Total elements |
| `dtype` | Data type |
| `T` | Transpose |

---

# 📌 15. ML Workflow

```text
Load Data
     │
     ▼
NumPy Array
     │
     ▼
Check shape & dtype
     │
     ▼
Index / Slice
     │
     ▼
Filter
     │
     ▼
Vectorized Operations
     │
     ▼
Statistics
     │
     ▼
Reshape
     │
     ▼
Machine Learning Model
```

---

# ⭐ NumPy Functions You'll Use Most

| Function | Purpose |
|----------|---------|
| `np.array()` | Create array |
| `.shape` | Get dimensions |
| `.ndim` | Number of dimensions |
| `.dtype` | Data type |
| `.reshape()` | Change dimensions |
| `+ - * /` | Vectorized math |
| `@` / `np.dot()` | Matrix multiplication |
| `np.mean()` | Average |
| `np.std()` | Standard deviation |
| `np.sum()` | Sum |
| Boolean Indexing | Filter rows |
| `np.random.seed()` | Reproducibility |

---

# 💡 ML Tip

Whenever you get an error while working with NumPy, check these **in order**:

1. `array.shape`
2. `array.dtype`
3. Indexing/Slicing
4. Broadcasting compatibility
5. Matrix dimensions (`@` / `dot`)

Most NumPy errors in ML come from one of these five issues.

---

# 🚀 Remember

- **NumPy = Fast numerical computation**
- **Everything is an array**
- **Avoid Python loops whenever possible**
- **Think in vectors and matrices**
- **Learn `shape` like the back of your hand**