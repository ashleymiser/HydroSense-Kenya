import numpy as np


def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Bisection root-finding method.
    Requires f(a) and f(b) to have opposite signs.
    Returns: root, iterations, final error, converged (bool), history
    """
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    history = []
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        error = abs(b - a) / 2
        history.append({"iter": i+1, "root": c, "f(c)": fc, "error": error})
        if abs(fc) < tol or error < tol:
            return c, i+1, error, True, history
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return c, max_iter, error, False, history


def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson root-finding method.
    Requires the function f and its derivative df.
    Returns: root, iterations, final error, converged (bool), history
    """
    x = x0
    history = []
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:
            return x, i, abs(fx), False, history
        x_new = x - fx / dfx
        error = abs(x_new - x)
        history.append({"iter": i+1, "root": x_new, "f(x)": f(x_new), "error": error})
        if error < tol:
            return x_new, i+1, error, True, history
        x = x_new
    return x, max_iter, abs(f(x)), False, history


def secant(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Secant root-finding method.
    Does not require the derivative of f.
    Returns: root, iterations, final error, converged (bool), history
    """
    history = []
    for i in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        if abs(fx1 - fx0) < 1e-12:
            break
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x2 - x1)
        history.append({"iter": i+1, "root": x2, "f(x)": f(x2), "error": error})
        if error < tol:
            return x2, i+1, error, True, history
        x0, x1 = x1, x2
    return x2, max_iter, error, False, history


def forward_diff(f, x, h=1e-5):
    """Forward difference approximation of derivative."""
    return (f(x + h) - f(x)) / h


def backward_diff(f, x, h=1e-5):
    """Backward difference approximation of derivative."""
    return (f(x) - f(x - h)) / h


def central_diff(f, x, h=1e-5):
    """Central difference approximation of derivative (more accurate)."""
    return (f(x + h) - f(x - h)) / (2 * h)


def trapezoidal(y, x):
    """Trapezoidal rule for numerical integration."""
    return np.trapezoid(y, x)


def simpsons(y, h):
    """
    Simpson 1/3 rule for numerical integration.
    Requires an odd number of evenly spaced points.
    """
    n = len(y)
    if n % 2 == 0:
        raise ValueError("Simpson rule requires an odd number of points.")
    result = y[0] + y[-1]
    result += 4 * np.sum(y[1:-1:2])
    result += 2 * np.sum(y[2:-2:2])
    return (h / 3) * result


def gaussian_elimination(A, b):
    """
    Solve the linear system Ax = b using Gaussian elimination
    with partial pivoting.
    Returns the solution vector x.
    """
    n = len(b)
    Ab = np.hstack([A.astype(float), b.reshape(-1, 1).astype(float)])
    for col in range(n):
        max_row = col + np.argmax(np.abs(Ab[col:, col]))
        Ab[[col, max_row]] = Ab[[max_row, col]]
        for row in range(col + 1, n):
            factor = Ab[row, col] / Ab[col, col]
            Ab[row, col:] -= factor * Ab[col, col:]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    return x
