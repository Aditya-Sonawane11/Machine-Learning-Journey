import numpy as np

a = [1, 2, 3]
b = [[1, 2], [2,3], [4,5]]

a_arr = np.array(a) #1D
b_arr = np.array(b) #2D

# 1D array = vector
# 2D array = matrix
# 3D array = tensor

# SHAPE

print(a_arr.shape) # (3,) --> (3 rows, 0 columns)
print(b_arr.shape) # (3,2) --> (3 rows, 2 columns)

# DIMENSIONS

print(a_arr.ndim) # 1
print(b_arr.ndim) # 2

# DATA TYPE

print(a_arr.dtype)

# INDEXING

"""
For 1D arrays - a[index]
For 2D arrays - b[row, column]
"""

# SLICING 

"""
a[starting index (inclusive) : ending index (exclusive)]

2D Arrays:

    Rows:
    b[row_index]

    Columns:
    b[:, column_index]
"""

# RESHAPING

c = np.array([1, 2, 3, 4, 5, 6])
print(c.reshape(2,3))


# STATISTICS

p = np.mean(c)
q = np.median(c)
r = np.max(c)
s = np.min(c)
t = np.sum(c)
u = np.std(c)

print(p, q, r, s, t, u)

# RANDOM NUMBERS

np.random.seed(42)
# print(np.random.rand(5)) # prints 5 random numbers bw 0 - 1
print(np.random.randint(1,100,5)) # prints 5 random integers (not anymore because of seed)

# MATRIX MULTIPLICATION

"""
1. a * b --> Element wise multiplication a(i,j) x b(i,j)
2. a @ b --> Matrix Multiplication
3. np.dot(a,b) = a @ b
"""

# BOOLEAN INDEXING

ages = np.array([18,25,16,40,30])
print(ages[ages >= 18])

