import numpy as np

def gaussian_elimination(A, b):
    """
    Solves Ax = b using Gaussian Elimination with partial pivoting.
    
    Parameters:
    A (numpy.ndarray): Coefficient matrix (n x n)
    b (numpy.ndarray): Dependent variable vector (n)
    
    Returns:
    numpy.ndarray: Solution vector x
    """
    n = len(b)
    # Augment matrix
    M = np.hstack([A, b.reshape(-1, 1)]).astype(float)

    for i in range(n):
        # Partial Pivoting: Swap rows if pivot is zero
        pivot = i + np.argmax(np.abs(M[i:, i]))
        if pivot != i:
            M[[i, pivot]] = M[[pivot, i]]
        
        # Eliminate entries below pivot
        for j in range(i + 1, n):
            factor = M[j, i] / M[i, i]
            M[j, i:] -= factor * M[i, i:]

    # Back Substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i:n], x[i:n])) / M[i, i]
        
    return x

def lu_decomposition(A):
    """
    Performs LU Decomposition of matrix A such that A = L * U.
    """
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy().astype(float)

    for i in range(n):
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
        
    return L, U

if __name__ == "__main__":
    # Test Case: System of Linear Equations
    A_test = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    b_test = np.array([1, 0, 1])
    
    print("--- Gaussian Elimination Test ---")
    x = gaussian_elimination(A_test, b_test)
    print(f"Solution x: {x}")
    
    print("\n--- LU Decomposition Test ---")
    L, U = lu_decomposition(A_test)
    print("L Matrix:\n", L)
    print("U Matrix:\n", U)
