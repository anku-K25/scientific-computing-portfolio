import numpy as np

def simpsons_rule(f, a, b, n):
    """
    Approximates the definite integral of f from a to b using Simpson's 1/3 Rule.
    n must be even.
    """
    if n % 2 == 1:
        n += 1 # Ensure n is even
        
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    S = h/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

def monte_carlo_integration(f, a, b, num_samples=10000):
    """
    Estimates integral using Monte Carlo sampling (probabilistic approach).
    """
    x_random = np.random.uniform(a, b, num_samples)
    y_random = f(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

if __name__ == "__main__":
    # Test: Integral of x^2 from 0 to 1 (Exact = 1/3 approx 0.3333)
    def func(x):
        return x**2
        
    simp = simpsons_rule(func, 0, 1, 100)
    mc = monte_carlo_integration(func, 0, 1, 10000)
    
    print(f"Simpson's Rule Result: {simp:.6f}")
    print(f"Monte Carlo Result:    {mc:.6f}")
