import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_4(f, y0, t0, t_end, h):
    """
    Solves dy/dt = f(t, y) using the 4th Order Runge-Kutta method (RK4).
    
    Parameters:
    f : function f(t, y)
    y0: Initial condition
    t0: Start time
    t_end: End time
    h : Step size
    """
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        y = y_values[i-1]
        
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5*h, y + 0.5*k1)
        k3 = h * f(t + 0.5*h, y + 0.5*k2)
        k4 = h * f(t + h, y + k3)
        
        y_values[i] = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        
    return t_values, y_values

if __name__ == "__main__":
    # Example: dy/dt = -2y, y(0) = 1 (Solution is y = e^(-2t))
    def decay_model(t, y):
        return -2 * y

    t, y = runge_kutta_4(decay_model, y0=1, t0=0, t_end=5, h=0.1)
    
    print(f"Solved ODE over interval [0, 5]. Final value: {y[-1]:.4f}")
    
    # Optional: Plotting code commented out for standard script usage
    # plt.plot(t, y, label='RK4 Approximation')
    # plt.plot(t, np.exp(-2*t), '--', label='Exact Solution')
    # plt.legend()
    # plt.show()
