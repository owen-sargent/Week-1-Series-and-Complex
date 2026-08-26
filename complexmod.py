"""Student assignment implementation file for complex analysis."""


# --- Student Assignment --- #
# --- General --- #
def complex_polar(z):
    """Convert a complex number to polar form.

    This function takes a complex number z and returns its polar form as a tuple
    (r, theta), where r is the magnitude of z and theta is the angle in radians.

    """
    raise NotImplementedError("Student assignment not yet implemented.")


def nth_root(z, n):
    """Compute the n-th roots of a complex number.

    This function takes a complex number z and an integer n, and returns
    all of the  the n-th roots (see Boas 2.10) of z as a complex number
    as a numpy array.

    """
    raise NotImplementedError("Student assignment not yet implemented.")


# --- Boas --- #
def complex_impedance(resistance, inductance, capacitance, omega):
    """Compute the complex impedance of a series RLC circuit.

    This function takes the resistance R, inductance L, capacitance C, and angular frequency omega
    of a series RLC circuit and returns the complex impedance Z as a complex number.

    """
    raise NotImplementedError("Student assignment not yet implemented.")


# See Boas Example 2.16 - Electricity
def plot_rlc(resistance, inductance, capacitance, omega, time, max_current, filename=None):
    """Plot the current and voltage time series of a series RLC circuit.

    This function takes the resistance R, inductance L, capacitance C, angular frequencies
    omega, and time array and generates the voltage and current signal for the
    series RLC circuit. The function also returns the current (first) and voltage (second)
    signals as numpy arrays.

    If filename is not None, save the generated figure to that filename.

    """
    raise NotImplementedError("Student assignment not yet implemented.")
