#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * A simple implementation of Matrix Multiplication in C.
 * Demonstrates: Pointers, Dynamic Memory Allocation, and Nested Loops.
 */

// Function to allocate memory for a matrix
double** allocate_matrix(int rows, int cols) {
    double** matrix = (double**)malloc(rows * sizeof(double*));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (double*)malloc(cols * sizeof(double));
    }
    return matrix;
}

// Function to free memory
void free_matrix(double** matrix, int rows) {
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

// Standard Matrix Multiplication: C = A * B
// A is (r1 x c1), B is (r2 x c2)
void multiply_matrices(int r1, int c1, int r2, int c2, double** A, double** B, double** C) {
    if (c1 != r2) {
        printf("Error: Matrix dimensions incompatible for multiplication.\n");
        return;
    }

    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            C[i][j] = 0;
            for (int k = 0; k < c1; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    int r = 3, c = 3;
    
    // 1. Dynamic Allocation
    double** A = allocate_matrix(r, c);
    double** B = allocate_matrix(r, c);
    double** Result = allocate_matrix(r, c);

    // 2. Initialize with dummy data
    printf("--- C Matrix Multiplication Demo ---\n");
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            A[i][j] = i + j;       // Just some numbers
            B[i][j] = (i + j) * 2; // Just some numbers
        }
    }

    // 3. Compute
    multiply_matrices(r, c, r, c, A, B, Result);

    // 4. Print Result
    printf("Result Matrix (Top Left element): %f\n", Result[0][0]);
    printf("Result Matrix (Bottom Right element): %f\n", Result[r-1][c-1]);

    // 5. Memory Cleanup (Crucial in C)
    free_matrix(A, r);
    free_matrix(B, r);
    free_matrix(Result, r);

    return 0;
}
