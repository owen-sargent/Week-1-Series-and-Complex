"""Student assignment implementation file for Infinite Series and Taylor Series expansions."""
import numpy as np
from math import log
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


# --- Student Assignment --- #
# --- Boas --- #
# Harmonic Series
def harmonic(n_terms: int) -> float:
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
    total_sum = 0.0
    n_terms = int(n_terms)

    if not isinstance(n_terms, (int, np.integer)) or n_terms <= 0:
        raise ValueError("n_terms must be a positive integer.")

    if n_terms < 50:
        for i in range(1, n_terms + 1):
            total_sum += 1 / i
        return total_sum

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
    total_sum: float = 0.0
    term: float = x
    n: int = 1

    while abs(term) > rel_tol and n <= max_iter:
        total_sum += term
        n += 1
        term *= -x * (n - 1) / n

    return total_sum, n


# Boas, Problem 1.13.22
def boas_1_13_22(x: float, rel_tol: float = 1e-8, max_iter: int = 100) -> tuple[float, int]:
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
    total_sum: float = 1.0
    term: float = 1.0
    n: int = 1
    p_n: float = 1.0
    f_n: float = 1.0
    s_n: float = 1.0

    while abs(term) > rel_tol and n <= max_iter:
        p_n *= x
        f_n /= n
        s_n += f_n
        term = p_n * s_n
        total_sum += term
        n += 1
    return total_sum, n


# Plots the first N terms of the series expansion of exp(x)/(1 - x)
def boas_1_13_22_plot(n_terms: int, filename: str | None = None) -> tuple[Figure, Axes]:
    """Plots the first N terms of the series expansion of exp(x)

    Parameters
    ----------
    n_terms : int
        The number of terms to plot in the series expansion.
    filename : str, optional
        The filename to save the plot. If None, the plot will be displayed.

    Returns
    -------
        tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]
            A tuple containing the figure and axes objects for the plot.
    """

    x = np.linspace(-5, 5, 1000)

    fig, ax = plt.subplots()

    exact = np.exp(x)
    ax.plot(
        x,
        exact,
        color="black",
        label=r"$e^x$",
    )

    exp_approx = np.zeros_like(x)
    term = np.ones_like(x)

    for n in range(n_terms):
        if n > 0:
            term *= x / n

        exp_approx += term

    ax.plot(
            x,
            exp_approx,
            label=f"n = {n + 1}",
        )

    ax.set_xlim(-5.0, 5.0)
    ax.set_title(f"First {n_terms} Terms of the Series Expansion of $e^x$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid()

    if filename:
        fig.savefig(filename)
    else:
        fig.show()

    return fig, ax


# Boas, Problem 1.16.1c
def boas_1_16_1c(overhang_d: float) -> int:
    """Computes how many books can be stacked on a table with a given overhang.

    Parameters
    ----------
    overhang_d : float
        The desired overhang distance.

    Returns
    -------
    int
        Minimum number of books that can be stacked on a table with the given overhang.
    """
    if overhang_d < 0:
        raise ValueError("overhang_d must be a positive real number or zero.")
    elif overhang_d == 0:
        return 0

    n_books = 0
    total_overhang = 0.0

    if overhang_d < 5:
        n_books = 0
        total_overhang = 0.0

        while total_overhang < overhang_d:
            n_books += 1
            total_overhang += 1 / (2 * n_books)
        return n_books + 1

    gamma = 0.5772156649015329
    n_books = np.exp(2 * overhang_d - gamma)
    # not - 0.5 + (1 / (12 * overhang_d)) - (1 / (288 * overhang_d**3))
    # due to those terms actually being the correction for n_books

    return int(np.ceil(n_books))


# --- Landau --- #
# The following questions are from Landau 3.3.1
# HOWEVER, these should be completed with cos instead of sin
def cos_apprx(x: float, rel_tol: float = 1e-8, max_iter: int = 100) -> tuple[float, int]:
    """Computes the Taylor series expansion of cos(x) until convergence or maximum iterations reached.

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
    float
            The approximation of cos(x).
    int
        The number of iterations used to compute the approximation.
    """

    x = x % (2 * np.pi)  # Reduces x to the range [0, 2π] from the periodicity of the cosine function

    if x > np.pi:
        x -= 2 * np.pi  # Reduces x to the range [-π, π] for better convergence of the Taylor series

    term: float = 1.0
    total_sum: float = 1.0
    n: int = 1
    iter_count: int = 1

    while abs(term / total_sum) > rel_tol and iter_count <= max_iter:
        term *= -x*x / (2 * n * (2 * n - 1))
        total_sum += term
        n += 1
        iter_count += 1

    return total_sum, iter_count
