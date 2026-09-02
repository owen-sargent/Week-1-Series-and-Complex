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

    if not isinstance(n_terms, (int, np.integer)) or n_terms <= 0:  # check if n_terms is a positive integer
        raise ValueError("n_terms must be a positive integer.")  # raise an error if n_terms is not a positive integer

    if n_terms < 50:  # compute the sum directly for small n_terms
        for i in range(1, n_terms + 1):  # compute the sum of the first n_terms of the harmonic series
            total_sum += 1 / i
        return total_sum

    recipical = 1 / n_terms  # makes the computation more efficient for large n_terms
    return (
        log(n_terms)
        + 0.5772156649015329
        + recipical / 2
        - recipical**2 / 12
        + recipical**4 / 120
    )  # compute the sum of the first n_terms of the harmonic series using the asymptotic expansion for large n_terms


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
    term: float = x  # Initialize the first term of the series
    n: int = 1  # Initialize n to 1 since the first term corresponds to n=1
    # Continue until the term is smaller than the relative tolerance or the maximum number of iterations is reached
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

    # Loops until the term is smaller than the relative tolerance or the maximum number of iterations is reached
    while abs(term) > rel_tol and n <= max_iter:
        p_n *= x  # Update p_n to be x^n
        f_n /= n  # Update f_n to be 1/n!
        s_n += f_n  # Update s_n to be the sum of 1/k! for k=0 to n
        term = p_n * s_n  # Compute the current term of the series
        total_sum += term  # Update the total sum of the series
        n += 1  # Increment n for the next iteration
    return total_sum, n


# Plots the first N terms of the series expansion of exp(x)/(1 - x)
def boas_1_13_22_plot(n_terms: int, filename: str | None = None) -> tuple[Figure, Axes]:
    """Plots the first N terms of the series expansion of exp(x)/(1 - x)

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
# Create an array of 1000 points between -2 and 2 for plotting the function and its approximations
    x = np.linspace(-2, 2, 1000)

    fig, ax = plt.subplots()  # Create a new figure and axes for the plot
# Compute the exact values of the function exp(x)/(1 - x) for the array of x values
    exact = np.exp(x) / (1.0 - x)
    ax.plot(
        x,
        exact,
        color="black",
        label="True Function",
    )
    # Initialize series approximation and current term using NumPy arrays of zeros and ones.
    exp_approx = np.zeros_like(x)
    term = np.ones_like(x)

    for n in range(n_terms):  # Loop over the number of terms to compute and plot the series expansion approximations
        if n > 0:
            term *= x / n  # Update the current term of the series expansion to be x^n/n! for the next iteration

        exp_approx += term  # Update the approximation of the series expansion by adding the current term
        # Compute the approximation of the function exp(x)/(1 - x) using the current series expansion approximation
        approximation = exp_approx / (1.0 - x)

        ax.plot(
            x,
            approximation,
            color=f"C{n}",
            linestyle=":",
            label=f"Approximation (n={n + 1})",
        )

    ax.set_ylim(-10.0, 10.0)
    ax.set_title(r"Series Expansion of $\frac{e^x}{1 - x}$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.legend(loc="upper left")

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
    if overhang_d < 0:  # Check if the overhang distance is negative
        raise ValueError("overhang_d must be a positive real number or zero.")
    elif overhang_d == 0:  # Check if the overhang distance is zero
        return 1  # Return 1 since at least one book is needed to have an overhang of zero

    n_books = 0  # Initialize the number of books to zero
    total_overhang = 0.0  # Initialize the total overhang to zero

    if overhang_d < 5:  # Use a simple loop to compute the number of books for small overhang distances
        n_books = 0
        total_overhang = 0.0
        # Loop until the total overhang is greater than or equal to the desired overhang distance
        while total_overhang < overhang_d:
            n_books += 1
            # Update the total overhang by adding the contribution of the next book in the stack
            total_overhang += 1 / (2 * n_books)
        return n_books + 1

    gamma = 0.5772156649015329
    # Estimates the number of books needed for larger overhang distances using the asymptotic expansion.
    n_books = np.exp(2 * overhang_d - gamma)
    # not - 0.5 + (1 / (12 * overhang_d)) - (1 / (288 * overhang_d**3))
    # due to those terms actually being the correction for n_books

    return int(np.ceil(n_books)) + 1


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

    if x > np.pi:  # Reduces x to the range [-π, π] for better convergence of the Taylor series
        x -= 2 * np.pi

    term: float = 1.0  # Initialize the first term of the series (cos(0) = 1)
    total_sum: float = 1.0
    n: int = 1  # Initialize n to 1 since the first term corresponds to n=0
    iter_count: int = 0

    while abs(term / total_sum) > rel_tol and iter_count < max_iter:
        # Update the current term of the series using the recurrence relation for the Taylor series of cos(x)
        term *= -x*x / (2 * n * (2 * n - 1))
        total_sum += term
        n += 1
        iter_count += 1

    return total_sum, iter_count
