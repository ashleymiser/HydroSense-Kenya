import sys
sys.path.insert(0, '..')
import numpy as np
from src.numerical_methods import gaussian_elimination


def test_gaussian_2x2():
    A = np.array([[2.0, 1.0], [1.0, 3.0]])
    b = np.array([5.0, 10.0])
    x = gaussian_elimination(A, b)
    expected = np.linalg.solve(A, b)
    np.testing.assert_allclose(x, expected, atol=1e-10)

def test_gaussian_3x3():
    A = np.array([[1.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [1.0, 1.0, 1.0]])
    b = np.array([10.4, 11.3, 34.1])
    x = gaussian_elimination(A, b)
    expected = np.linalg.solve(A, b)
    np.testing.assert_allclose(x, expected, atol=1e-10)
