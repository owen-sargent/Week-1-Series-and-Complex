"""Student assignment implementation file for Infinite Series and Taylor Series expansions."""
import numpy as np
from math import log
import matplotlib.pyplot as plt
from numba import njit

# --- Student Assignment --- #
# --- Boas --- #
# Harmonic Series
def harmonic(n_terms):
    """Computes the sum of the first n terms of the harmonic series.
        Parameters
        ----------
        n_terms : int
            The number of terms to sum in the harmonic series.
        Returns
        -------
        float
            The sum of the first n terms of the harmonic series.
    """
    total_sum = 0
    n_terms = int(n_terms)

    if not isinstance(n_terms, (int, np.integer)) or n_terms <= 0:
        raise ValueError("n_terms must be a positive integer.")

    if n_terms < 50:
        for i in range(1, n_terms + 1):
            total_sum += 1 / i
        return total_sum

    n_terms = float(n_terms)
    recipical = 1 / n_terms
    return (
        log(n_terms)
        + 0.5772156649015329
        + recipical / 2
        - recipical**2 / 12
        + recipical**4 / 120
    )

# Boas, 3rd Edition, Equation 1.13.4
def boas_1_13_4(
    x: float, rel_tol: float = 1e-8, max_iter: int = 100
) -> tuple[float, int]:
    """Computes the series of ln(1 + x).
        Parameters
        ----------
        x : float
            The value to compute the series for.
        rel_tol : float, optional
            The relative tolerance for convergence. Default is 1e-8.
        max_iter : int, optional
            The maximum number of iterations to perform. Default is 100.
        Returns
        -------
        tuple[float, int]
            A tuple containing the sum of the series and the number of iterations used.
    """
    total_sum = 0
    term = x
    n = 1

    while abs(term) > rel_tol and n <= max_iter:
        total_sum += term
        n += 1
        term *= -x * (n - 1) / n

    return total_sum, n


# Boas, Problem 1.13.22
def boas_1_13_22(x, rel_tol = 1e-8, max_iter = 100):
    """Computes the sum of the Maclaurin series for exp(x)/(1 - x).
        Parameters
        ----------
        x : float
            The value to compute the series for.
        rel_tol : float, optional
            The relative tolerance for convergence. Default is 1e-8.
        max_iter : int, optional
            The maximum number of iterations to perform. Default is 100.
        Returns
        -------
        tuple[float, int]
            A tuple containing the sum of the series and the number of iterations used.
    """
    total_sum = 1
    term = 1
    n = 1
    p_n = 1
    f_n = 1
    s_n = 1

    while abs(term) > rel_tol and n <= max_iter:
        p_n *= x
        f_n /= n
        s_n += f_n
        term = p_n * s_n
        total_sum += term
        n += 1
    return total_sum, n


# Plots the first N terms of the series expansion of exp(x)/(1 - x)
def boas_1_13_22_plot(n_terms, filename=None):
    """Plots the first N terms of the series expansion of exp(x)/(1 - x)
        Parameters
        ----------
        n_terms : int
            The number of terms to plot in the series expansion.
        filename : str, optional
            The filename to save the plot. If None, the plot will be displayed.
        Returns
        -------
        Tuple[x, y]
            A tuple containing the x and y values of the plot.
    """
    @njit
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    x = np.linspace(-2, 2, 100)
    y = np.exp(x) / (1 - x)

    plt.plot(x, y, label="exp(x)/(1 - x)", color="blue")

    for n in range(1, n_terms + 1):
        term = (x**n) / factorial(n)
        plt.plot(x, term, label=f"Term {n}", linestyle="--")

    plt.title(f"First {n_terms} Terms of the Series Expansion of exp(x)/(1 - x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()

    if filename:
        plt.savefig(filename)
    else:
        plt.show()

    return (x, y)

# Boas, Problem 1.16.1c
def boas_1_16_1c(n_books_overhang):
    """Compute how many books can be stacked on a table with a given overhang."""
    raise NotImplementedError("Student assignment not yet implemented.")



# --- Landau --- #
# The following questions are from Landau 3.3.1
# HOWEVER, these should be completed with cos instead of sin
def cos_apprx(x, rel_tol = 1e-8, max_iter = 100):
    """Compute the approximation of cos(x) using the Taylor series expansion.

    This function computes the Taylor series of cos(x) until the series converges
    or maximum number of iterations is reached. The function returns the approximation
    of cos(x) and the number of iterations used to compute the approximation and makes
    use of the identity cos(x) = cos(x + 2*pi*n) for any integer n to reduce the input
    x to the range [0, 2*pi].

    """
    raise NotImplementedError("Student assignment not yet implemented.")
