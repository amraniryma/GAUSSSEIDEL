# gauss_seidel.py
# This is the main file for the Gauss-Seidel method project
import numpy as np  # Import numpy for array operations
def is_diagonally_dominant(A):
    n = len(A)
    for i in range(n):
        if abs(A[i][i]) <= sum(abs(A[i][j]) for j in range(n) if j != i):
            return False
    return True
# Function checks if matrix A is diagonally dominant

