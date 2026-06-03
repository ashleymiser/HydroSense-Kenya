import pytest
import sys
sys.path.insert(0, '..')
from src.numerical_methods import bisection, newton_raphson, secant


def f(x):
    return x**2 - 4   # roots at x=2 and x=-2

def df(x):
    return 2*x


def test_bisection_finds_root():
    root, _, _, converged, _ = bisection(f, 0, 3)
    assert converged
    assert abs(root - 2.0) < 1e-5

def test_bisection_wrong_bracket_raises():
    # both f(3) and f(5) are positive, no sign change, should raise
    with pytest.raises(ValueError):
        bisection(f, 3, 5)

def test_newton_raphson_finds_root():
    root, _, _, converged, _ = newton_raphson(f, df, 3.0)
    assert converged
    assert abs(root - 2.0) < 1e-5

def test_secant_finds_root():
    root, _, _, converged, _ = secant(f, 1.0, 3.0)
    assert converged
    assert abs(root - 2.0) < 1e-5
