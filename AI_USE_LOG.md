# AI Use Log — HydroSense-Kenya

| Prompt Used | AI Output Summary | Accepted? | Modified? | Validation Method |
|-------------|-------------------|-----------|-----------|-------------------|
| What does forward fill mean for missing values? | Explained that ffill replaces NaN with the previous row value | Yes | No | Read pandas documentation to confirm |
| Why does 0.1 + 0.2 not equal 0.3 in Python? | Explained binary floating point representation | Yes | No | Tested in Python interpreter |
| What is the difference between bisection and Newton-Raphson? | Explained that bisection brackets the root while Newton-Raphson uses the derivative to converge faster | Yes | No | Compared iteration counts in our results |
| How does np.maximum differ from max? | Explained that np.maximum works element-wise on arrays while max returns a single value | Yes | No | Tested both on a small array |
| What is partial pivoting in Gaussian elimination? | Explained that it swaps rows to avoid division by small numbers | Yes | No | Verified solution against np.linalg.solve |
| Why was np.trapz giving an AttributeError? | Explained that np.trapz was removed in newer NumPy versions and should be replaced with np.trapezoid | Yes | No | Ran the corrected code and confirmed it worked |
| How do I set up a virtual environment on Linux? | Explained python3 -m venv and pip install workflow | Yes | No | Successfully installed all dependencies |
