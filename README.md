# PH 306 Assignment: Taylor Series and Complex Numbers

This assignment has two coding parts:

1. Infinite/Taylor series methods in `series.py`
2. Complex-number methods in `complexmod.py`

Implement the required functions in those two files. **Do not rename files or functions.**

## Files You Should Edit

- `series.py`
- `complexmod.py`

### Required Functions

Implement all stubs currently raising `NotImplementedError`.

#### In `series.py`

- `harmonic`: Implements the harmonic series up to $N$ terms.
  - For High $N$, switch to asymptotic approximation (see below)
    - [StackExchange](https://stackoverflow.com/questions/404346/python-program-to-calculate-harmonic-series): Note that some needed constants are in `scipy` and `numpy`
    - [Wikipedia Calculation](https://en.wikipedia.org/wiki/Harmonic_number#Calculation) or [Wikipedia Application](https://en.wikipedia.org/wiki/Harmonic_number#Applications)
    - Will check up to $N = 10^{100}$
- `boas_1_13_4`: Implements $\ln(1+x)$ as a Taylor Series with a stopping criteria (approximation and iterations should be returned).
- `boas_1_13_22`: Implements $\exp(x)/(1 - x)$ as a Taylor Series with a stopping criteria (approximation and iterations should be returned). **Note:** Only expand the exponential.
- `boas_1_13_22_plot`
  - Implements $f(x) = \exp(x)/(1 - x)$ as a Maclaurin Series up to a fixed number of terms $N$. **Note:** Only expand the exponential.
  - Plots the function $f(x)$ for $-5 < x < 5$ in black
  - Plots the $N$ Maclaurin approximations or $f(x)$ using Matplotlib colors `C0, C1, ..., C<N-1>`.
  - Accepts an optional `filename` argument with default `None`.
  - If `filename` is not `None`, saves the figure to that file.
  - Returns the Matplotlib Figure and Axes objects to user.
  - Example/Comparison plot can be found on Canvas
- `boas_1_16_1c`: Determines the number of books needed to get the necessary book-lengths of overhang. (See Boas 1.16.1c)
  - For High $N$, switch to asymptotic approximation (see below)
    - [StackExchange](https://stackoverflow.com/questions/404346/python-program-to-calculate-harmonic-series): Note that some needed constants are in `scipy` and `numpy`
    - [Wikipedia Calculation](https://en.wikipedia.org/wiki/Harmonic_number#Calculation) or [Wikipedia Application](https://en.wikipedia.org/wiki/Harmonic_number#Applications)
- `cos_apprx`
  - Approximate $\cos$ (instead of $\sin$)
  - From Landau 3.3.1
  - Do Parts 1 and 7
  - Return approximation and number of iterations

#### In `complexmod.py`

- `complex_polar`: Converts a complex number $z = x+iy$ to polar form as a tuple $z = (r, \theta)$.
- `nth_root`: Returns the $n$ roots of $z$ as a tuple ($z_1 = \sqrt[n]{z_0}$)
- `complex_impedance`: Calculates the complex impedance of a driven series RLC circuit (see Boas Equation 2.16.15)
- `plot_rlc`
  - Should plot the current and voltage using complex analysis.
  - Should plot and return the imaginary part of the current/voltage.
  - Should be `astropy` quantity-friendly.
  - Should plot over six (current, not necessarily voltage) periods.
  - Accepts an optional `filename` argument with default `None`.
  - If `filename` is not `None`, saves the figure to that file.
  - Example/comparison plot on Canvas.

## Current Libraries

The currently guaranteed scientific libraries in CodeGrade are:

- `pandas`
- `numpy`
- `scipy`
- `scikit-learn`
- `scikit-image`
- `astropy`
- `matplotlib`

## Local Validation Only

Run the visible tests before submitting:

```bash
pytest
```

Optional style/type checks may be run by course tooling:

```bash
bash test_codegrade_mypy.sh
```
