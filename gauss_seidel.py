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
def gauss_seidel(A, B, tol=1e-6, max_iterations=100):
    n = len(A)
    X = np.zeros(n, dtype=float)
    for k in range(max_iterations):
        X_old = X.copy()
        for i in range(n):
            sum_before = sum(A[i][j] * X[j] for j in range(i))
            sum_after = sum(A[i][j] * X_old[j] for j in range(i+1, n))
            X[i] = (B[i] - sum_before - sum_after) / A[i][i]
        print(f"Iteration {k+1}: {X}")
        if np.allclose(X, X_old, atol=tol):
            return X
    return X
# Function solves AX=B using Gauss-Seidel iterative method
def read_float(msg):
    while True:
        value = input(msg)
        if value.strip() == "":
            print("Invalid input. Try again.")
            continue
        try:
            return float(value)
        except ValueError:
            print("Invalid number. Try again.")
# Function to safely read a float from user

def read_matrix(n):
    A = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            A[i][j] = read_float(f"A[{i+1}][{j+1}]: ")
    return A

def read_vector(n):
    B = np.zeros(n, dtype=float)
    for i in range(n):
        B[i] = read_float(f"B[{i+1}]: ")
    return B
# Functions to read matrix A and vector B from user

def main():
    n = int(read_float("Enter number of variables: "))
    A = read_matrix(n)
    B = read_vector(n)

    if not is_diagonally_dominant(A):
        print("Matrix is not diagonally dominant.")
        return

    X = gauss_seidel(A, B)
    print("Final solution:", X)
# Main function to run the program

