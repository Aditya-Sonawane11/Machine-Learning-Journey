# 🎨 Matplotlib Cheat Sheet for Machine Learning



```python
import matplotlib.pyplot as plt
```

---

# 📌 1. Create a Figure

```python
plt.figure(figsize=(8,5))
```

**Does:** Creates a new plotting area.

**Returns:** A Figure object.

**Use when:** You want to control the plot size.

---

# 📌 2. Line Plot

```python
plt.plot(x, y)
```

**Does:** Draws a line connecting all points.

**Returns:** A list of `Line2D` objects.

**Best For:**

- Trends
- Time series
- Continuous data

Example

```python
x = [1,2,3,4]
y = [2,4,6,8]

plt.plot(x,y)
```

---

# 📌 3. Scatter Plot ⭐

```python
plt.scatter(x, y)
```

**Does:** Draws individual data points.

**Returns:** A `PathCollection`.

**Best For:**

- Relationship between two variables
- Correlation
- Outliers
- Clusters

Example

```python
plt.scatter(df["Age"], df["Salary"])
```

---

# 📌 4. Histogram ⭐

```python
plt.hist(data)
```

**Does:** Shows the frequency distribution of a feature.

**Returns:** Histogram values, bin edges, and patches.

**Best For:**

- Feature distributions
- Detecting skewness
- Detecting outliers

Example

```python
plt.hist(df["Salary"])
```

---

# 📌 5. Bar Chart

```python
plt.bar(categories, values)
```

**Does:** Compares categorical values.

**Returns:** A `BarContainer`.

Example

```python
cities = ["Pune", "Delhi", "Mumbai"]
sales = [20,35,15]

plt.bar(cities, sales)
```

---

# 📌 6. Pie Chart

```python
plt.pie(values, labels=labels)
```

**Does:** Shows proportions of a whole.

**Returns:** Wedges, texts, and autotexts (if enabled).

Mostly used for presentations rather than ML.

---

# 📌 7. Title

```python
plt.title("House Prices")
```

**Does:** Adds a title to the graph.

---

# 📌 8. Axis Labels

```python
plt.xlabel("House Size")

plt.ylabel("Price")
```

**Does:** Labels the x-axis and y-axis.

Always label your plots.

---

# 📌 9. Legend

```python
plt.plot(x, y1, label="2024")
plt.plot(x, y2, label="2025")

plt.legend()
```

**Does:** Displays labels for plotted data.

Use when plotting multiple datasets.

---

# 📌 10. Grid

```python
plt.grid(True)
```

**Does:** Adds grid lines.

Makes graphs easier to read.

---

# 📌 11. Display Plot

```python
plt.show()
```

**Does:** Displays the current figure.

Without this, your graph may not appear (outside notebooks).

---

# 📌 12. Save Plot

```python
plt.savefig("plot.png")
```

**Does:** Saves the current figure.

Supported formats

- PNG
- JPG
- PDF
- SVG

---

# 📌 13. Multiple Plots

```python
plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.legend()

plt.show()
```

**Does:** Draws multiple datasets on the same graph.

Useful for comparison.

---

# 📌 14. Common Customization

### Line Color

```python
plt.plot(x, y, color="red")
```

---

### Line Style

```python
plt.plot(x, y, linestyle="--")
```

Options

- `"-"` Solid
- `"--"` Dashed
- `":"` Dotted
- `"-."` Dash-dot

---

### Marker Style

```python
plt.plot(x, y, marker="o")
```

Common markers

- `"o"` Circle
- `"s"` Square
- `"^"` Triangle
- `"*"` Star
- `"x"` Cross

---

### Line Width

```python
plt.plot(x, y, linewidth=3)
```

---

# 📌 15. Matplotlib + Pandas ⭐

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("housing.csv")

plt.scatter(
    df["median_income"],
    df["median_house_value"]
)

plt.xlabel("Median Income")
plt.ylabel("House Value")

plt.title("Income vs House Value")

plt.show()
```

This is how you'll usually use Matplotlib in ML.

---

# 📌 16. Typical Plot Template

```python
plt.figure(figsize=(8,5))

plt.plot(x, y)

plt.title("Title")

plt.xlabel("X-axis")

plt.ylabel("Y-axis")

plt.grid(True)

plt.show()
```

This is the template you'll write most often.

---

# 📌 17. Which Plot Should I Use?

| Plot | Best For |
|------|----------|
| `plot()` | Trends over time or continuous data |
| `scatter()` | Relationship between two numerical variables |
| `hist()` | Distribution of a feature |
| `bar()` | Compare categories |
| `pie()` | Show proportions (rare in ML) |

---

# ⭐ Most Used Matplotlib Functions

| Function | What it does |
|----------|--------------|
| `plt.figure()` | Creates a new figure |
| `plt.plot()` | Draws a line plot |
| `plt.scatter()` | Draws a scatter plot |
| `plt.hist()` | Draws a histogram |
| `plt.bar()` | Draws a bar chart |
| `plt.pie()` | Draws a pie chart |
| `plt.title()` | Adds a title |
| `plt.xlabel()` | Labels x-axis |
| `plt.ylabel()` | Labels y-axis |
| `plt.legend()` | Displays plot labels |
| `plt.grid()` | Adds grid lines |
| `plt.show()` | Displays the graph |
| `plt.savefig()` | Saves the graph |

---

# 📊 Typical ML Visualization Workflow

```text
Load Dataset (Pandas)
        │
        ▼
Select Features
        │
        ▼
Choose Plot
        │
        ├── plot()      → Trends
        ├── scatter()   → Correlation
        ├── hist()      → Distribution
        ├── bar()       → Categories
        ▼
Customize
(title, labels, legend, grid)
        │
        ▼
plt.show()
```

---

# 💡 ML Tip

Before training any model, visualize your data.

A good starting checklist:

```python
# Distribution of a feature
plt.hist(df["Age"])

# Relationship between two features
plt.scatter(df["Age"], df["Salary"])

# Trend
plt.plot(x, y)

plt.show()
```

You'll often spot missing patterns, outliers, or relationships that aren't obvious from looking at the raw numbers.

---

# 🚀 Remember

- **NumPy** → Numerical computation
- **Pandas** → Data manipulation
- **Matplotlib** → Data visualization

**The standard ML workflow is:**

```text
CSV
 ↓
Pandas
 ↓
NumPy
 ↓
Matplotlib
 ↓
Scikit-Learn
```

---

# ⭐ Quick Revision

| Library | Primary Purpose |
|----------|-----------------|
| **NumPy** | Fast numerical computation |
| **Pandas** | Load, clean, manipulate data |
| **Matplotlib** | Visualize data |
