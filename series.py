"""Student assignment implementation file for Infinite Series and Taylor Series expansions."""


# --- Student Assignment --- #
# --- Boas --- #
# Harmonic Series
def harmonic(n_terms):
    """Compute the sum of the first n terms of the harmonic series."""
    raise NotImplementedError("Student assignment not yet implemented.")


# Boas, 3rd Edition, Equation 1.13.4
def boas_1_13_4(
    x: float, rel_tol: float = 1e-8, max_iter: int = 100
) -> tuple[float, int]:
    """Compute the series of ln(1 + x)."""
    raise NotImplementedError("Student assignment not yet implemented.")


# Boas, Problem 1.13.22
def boas_1_13_22(x, rel_tol = 1e-8, max_iter = 100):
    """Compute the sum of the series exp(x)/(1 - x)."""
    raise NotImplementedError("Student assignment not yet implemented.")


# Plots the first N terms of the series expansion of exp(x)/(1 - x)
def boas_1_13_22_plot(n_terms, filename=None):
    """Plot the first N terms of the series expansion of exp(x)/(1 - x)

    This function generates a plot similar to the one in Boas, Figure 1.13.1
    (but with all N approximations on a single plot).

    If filename is not None, save the generated figure to that filename.

    """
    raise NotImplementedError("Student assignment not yet implemented.")


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
