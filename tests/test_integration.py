import sys
sys.path.insert(0, '..')
import numpy as np
from src.numerical_methods import trapezoidal, simpsons


def test_trapezoidal_constant_function():
    # integral of 1 from 0 to 10 = 10
    x = np.linspace(0, 10, 100)
    y = np.ones(100)
    assert abs(trapezoidal(y, x) - 10.0) < 0.01

def test_trapezoidal_linear_function():
    # integral of x from 0 to 1 = 0.5
    x = np.linspace(0, 1, 100)
    y = x
    assert abs(trapezoidal(y, x) - 0.5) < 0.01

def test_simpsons_quadratic():
    # integral of x^2 from 0 to 1 = 1/3
    x = np.linspace(0, 1, 101)
    y = x**2
    h = x[1] - x[0]
    assert abs(simpsons(y, h) - 1/3) < 1e-5

def test_simpsons_raises_on_even_points():
    import pytest
    y = np.ones(100)
    with pytest.raises(ValueError):
        simpsons(y, 1.0)
