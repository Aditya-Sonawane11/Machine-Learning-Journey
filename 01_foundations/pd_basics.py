import pandas as pd

# Reading Datasets

# CSV File
df = pd.read_csv("housing.csv")

# Excel sheet 
# df = pd.read_excel("housing.xlsx")

# Printing a single column
# df["column_name"]

print(df["population"]) # --> Series

# df.head() --> first 5 rows

print(df.head())

# df.tail() --> last 5 rows

print(df.tail())

# df.shape() --> (rows, columns)

# print(df.shape())

# df.columns() --> shows all column names

# df.info() --> shows dataset information like rows, columns, datatypes, missing values

# df.describe() --> shows statistics summary

# Selecting data -->
    # Single column --> df["column_name"]
    # Multiple columns --> df[["c1", "c2"]] {we use 2 squared braces}

# Indexing (iloc - integer location)

# df.iloc[0] --> prints first row
# df.iloc[0,2] --> prints row 0, column 2

# df.iloc[0:5] --> first 5 rows (0 inclusive, 5 exclusive)
# df.loc[:, "population"] --> Entire population column

# Filtering
df[df["population"] < 40000]

df[(df["population"] > 20000) & (df["total_rooms"] < 500)]

# Missing Values

print(df.isnull()) # boolean

print(df.isnull().sum()) # no. of null values in each column

# Filling missing values

df.fillna(0)

df.dropna() # delete missing rows
