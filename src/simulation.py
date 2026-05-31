import numpy as np


def dSdt(S, R, ET, drainage_coeff, field_capacity, I=0):
    """
    Rate of change of soil moisture.
    D = drainage only when moisture exceeds field capacity.
    """
    D = drainage_coeff * max(0, S - field_capacity)
    return R - ET - D + I


def euler_simulation(S0, rainfall, et_series, irrigation, params, dt=1.0):
    """
    Simulate soil moisture over time using the Euler method.

    Parameters:
        S0        : initial soil moisture (%)
        rainfall  : array of daily rainfall values
        et_series : array of daily ET values
        irrigation: array of daily irrigation amounts
        params    : dict with drainage_coefficient and field_capacity_pct
        dt        : time step in days (default 1)
    Returns:
        array of soil moisture values (length = len(rainfall) + 1)
    """
    S = [S0]
    dc = params['drainage_coefficient']
    fc = params['field_capacity_pct']
    for t in range(len(rainfall)):
        dS = dSdt(S[-1], rainfall[t], et_series[t], dc, fc, irrigation[t])
        S.append(S[-1] + dt * dS)
    return np.array(S)


def rk4_simulation(S0, rainfall, et_series, irrigation, params, dt=1.0):
    """
    Simulate soil moisture over time using the 4th-order Runge-Kutta method.

    Parameters: same as euler_simulation
    Returns:
        array of soil moisture values (length = len(rainfall) + 1)
    """
    S = [S0]
    dc = params['drainage_coefficient']
    fc = params['field_capacity_pct']
    for t in range(len(rainfall)):
        R  = rainfall[t]
        ET = et_series[t]
        I  = irrigation[t]
        k1 = dSdt(S[-1],            R, ET, dc, fc, I)
        k2 = dSdt(S[-1]+dt*k1/2,    R, ET, dc, fc, I)
        k3 = dSdt(S[-1]+dt*k2/2,    R, ET, dc, fc, I)
        k4 = dSdt(S[-1]+dt*k3,      R, ET, dc, fc, I)
        S.append(S[-1] + (dt/6) * (k1 + 2*k2 + 2*k3 + k4))
    return np.array(S)
