import sys
sys.path.insert(0, '..')
import numpy as np
from src.simulation import euler_simulation, rk4_simulation

PARAMS = {
    'drainage_coefficient': 0.18,
    'field_capacity_pct': 41.0,
    'min_moisture_pct': 22.0,
    'S0': 33.20
}

def test_euler_output_length():
    S = euler_simulation(33.0, np.zeros(10), np.ones(10)*3.0, np.zeros(10), PARAMS)
    assert len(S) == 11

def test_euler_decreases_without_rain():
    S = euler_simulation(35.0, np.zeros(10), np.ones(10)*3.0, np.zeros(10), PARAMS)
    assert S[-1] < S[0]

def test_rk4_output_length():
    S = rk4_simulation(33.0, np.zeros(10), np.ones(10)*3.0, np.zeros(10), PARAMS)
    assert len(S) == 11

def test_euler_rk4_close_for_small_dt():
    rain = np.ones(10) * 2.0
    et   = np.ones(10) * 1.5
    irr  = np.zeros(10)
    S_euler = euler_simulation(33.0, rain, et, irr, PARAMS)
    S_rk4   = rk4_simulation(33.0, rain, et, irr, PARAMS)
    np.testing.assert_allclose(S_euler, S_rk4, atol=0.5)
