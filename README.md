# Scientific Computing Portfolio

## Overview
This repository contains Python implementations of fundamental numerical algorithms developed during my **M.Sc. coursework in Scientific Computing** (MAT3021) at IISER Thiruvananthapuram.

The goal of this collection is to demonstrate the algorithmic understanding of continuous mathematics, bridging the gap between theoretical analysis and computational implementation.

## Contents

### 1. Numerical Linear Algebra (`linear_algebra_solvers.py`)
- **Gaussian Elimination (with Partial Pivoting):** Solves linear systems $Ax=b$. Implemented from scratch to understand algorithmic stability.
- **LU Decomposition:** Factorizes a matrix into Lower (L) and Upper (U) triangular matrices, essential for efficient numerical solvers.

### 2. Ordinary Differential Equations (`ode_solvers.py`)
- **Runge-Kutta Methods (RK4):** Implements the 4th-order Runge-Kutta method for solving initial value problems (IVPs) with high accuracy.
- Used to model dynamical systems where analytical solutions are difficult to derive.

### 3. Numerical Integration (`numerical_integration.py`)
- **Simpson's 1/3 Rule:** Deterministic quadrature rule for approximating definite integrals.
- **Monte Carlo Integration:** Probabilistic approach to integration, demonstrating the application of random sampling in numerical analysis.

- ### 4. Low-Level Optimization (`matrix_ops.c`)
- **Language:** C
- **Concept:** Manual memory management and pointer arithmetic for Matrix Multiplication.
- **Why C?** While Python is excellent for prototyping, C is used here to demonstrate an understanding of the underlying memory operations required for high-performance numerical computing.

## Technical Context
- **Language:** Python 3.x
- **Libraries:** `numpy` (for vectorized operations), `matplotlib` (for visualization).
