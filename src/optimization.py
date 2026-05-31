import numpy as np
from src.simulation import euler_simulation


def total_irrigation_cost(irrigation_schedule, rainfall, et_series, params):
    """
    Objective function for irrigation optimization.
    Minimizes total water used, with a large penalty for days below minimum moisture.
    """
    PENALTY = 1000
    S = euler_simulation(
        params['S0'], rainfall, et_series,
        irrigation_schedule, params
    )
    water_used  = np.sum(irrigation_schedule)
    stress_days = np.sum(S[1:] < params['min_moisture_pct'])
    return water_used + PENALTY * stress_days


def optimize_irrigation(rainfall, et_series, params, n_days=30):
    """
    Find the irrigation schedule that minimizes total water use
    while keeping soil moisture above the minimum threshold.

    Uses scipy L-BFGS-B with bounds 0 to 20 mm per day.
    Returns the scipy OptimizeResult object.
    """
    from scipy.optimize import minimize

    x0     = np.ones(n_days) * 2.0
    bounds = [(0, 20)] * n_days

    result = minimize(
        total_irrigation_cost,
        x0,
        args=(rainfall, et_series, params),
        method='L-BFGS-B',
        bounds=bounds
    )
    return result
