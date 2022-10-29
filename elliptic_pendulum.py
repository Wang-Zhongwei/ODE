# solve second order ODE for the angle of an elliptic pendulum

import numpy as np

def solver1(vEval, x0, tSpan):
    """First order ODE solver

    Args:
        vEval (array): first order derivatives evaluated at tSpan 
        x0 (double): initial value of zeroth derivative
        tSpan (array): time steps

    Returns:
        array: zeroth derivatives evaluated at tSpan
    """
    n = len(tSpan) # number of time steps
    dt = tSpan[1] - tSpan[0] # time step size
    x = np.zeros(n + 1) # initialize x array
    
    x[0] = x0 
    for i in range(1, n + 1):
        x[i] = x[i - 1] + vEval[i - 1] * dt
    return (x[:n] + x[1:]) / 2

def solver2(a, x0, v0, tSpan, *args):
    """Second order ODE solver

    Args:
        a (function): mapping from zeroth derivatives to second derivatives
        x0 (double): initial value of zeroth derivative
        v0 (double): initial value of first derivative
        tSpan (array): time steps

    Returns:
        array: zeroth derivatives evaluated at tSpan
    """
    n = len(tSpan) # number of time steps
    dt = tSpan[1] - tSpan[0] # time step size
    xEval = np.zeros(n) # initialize x array
    
    xEval[0] = x0 
    prev_v = v0 # v_{-1}
    for i in range(1, n):
        cur_a = a(xEval[i - 1], *args)
        cur_v = prev_v + cur_a * dt
        xEval[i] = xEval[i - 1] + cur_v * dt
        prev_v = cur_v
    return xEval

# elliptic pendulum
def theta_double_dot(theta, Omega0, omega0):
    """_summary_

    Args:
        theta (double): Euler's angle theta
        Omega0 (double): angular momentum of the elliptic pendulum
        omega0 (double): angular frequency of the small angle 1D pendulum 

    Returns:
        double: second derivative of theta
    """
    return np.cos(theta) / np.sin(theta)**3 * Omega0**2 - omega0**2 * np.sin(theta)
    
def phi_dot(theta, Omega0):
    return Omega0 / np.sin(theta)**2

def projection(theta, phi, l):
    """_summary_

    Args:
        theta (double): Euler's angle theta
        phi (double): Euler's angle phi

    Returns:
        double: x coordinate
        double: y coordinate
    """
    return l * np.sin(theta) * np.cos(phi), l * np.sin(theta) * np.sin(phi)




