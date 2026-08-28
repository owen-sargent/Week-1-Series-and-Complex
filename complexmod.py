"""Student assignment implementation file for complex analysis."""
import cmath as cm
import numpy as np
from astropy import units as u
from astropy.units import Quantity as Q
import matplotlib.pyplot as plt

# --- Student Assignment --- #
# --- General --- #
def complex_polar(z):
    """Convert a complex number to polar form.

    Parameters
    ----------
    z : complex
        The complex number to convert.

    Returns
    -------
    tuple
        A tuple containing the magnitude (r) and phase (theta) in radians.
    """
    r = abs(z)
    theta = cm.phase(z)
    return (r, theta)
    


def nth_root(z, n):
    """Find all n-th roots of a complex number.

    Parameters
    ----------
    z : complex
        The complex number to find the roots of.
    n : int
        The degree of the root.

    Returns
    -------
    numpy.ndarray
        An array containing all n-th roots of z.

    """
    r = abs(z)
    theta = np.angle(z)

    k = np.arange(n)

    root = r ** (1/n)
    root_theta = (theta + 2 * np.pi * k) / n

    roots = root * (np.cos(root_theta) + 1j * np.sin(root_theta))


    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    return np.array(roots)

# --- Boas --- #
@u.quantity_input
def complex_impedance(R, L, C, W):
    """Calculate the complex impedance of a series RLC circuit.

    Parameters
    ----------
    R : float
        The resistance.
    L : float
        The inductance.
    C : float
        The capacitance.
    W : float
        The angular frequency.

    Returns
    -------
    complex
        The complex impedance Z as a complex number.
    """
    impedance = R + 1j*(W*L-1/(W*C))

    return impedance


# See Boas Example 2.16 - Electricity
def plot_rlc(resistance, inductance, capacitance, omega, time, max_current, filename=None):
    """Plot the current and voltage in a series RLC circuit over time.

    Parameters
    ----------
    resistance : float
        The resistance.
    inductance : float
        The inductance.
    capacitance : float
        The capacitance.
    omega : float
        The angular frequency.
    time : numpy.ndarray
        The time array.
    max_current : float
        The maximum current.
    filename : str, optional
        The filename to save the plot to.

    Returns
    -------
    tuple
        A tuple containing the current and voltage arrays.
    """

    resistance = getattr(resistance, 'value', resistance)
    inductance = getattr(inductance, 'value', inductance)
    capacitance = getattr(capacitance, 'value', capacitance)
    omega = getattr(omega, 'value', omega)
    time = getattr(time, 'value', time)
    max_current = getattr(max_current, 'value', max_current)

    impedance = complex_impedance(resistance, inductance, capacitance, omega)

    current = max_current * np.sin(omega * time)

    phase_angle = np.angle(impedance)

    angle = omega*time

    max_voltage = max_current * abs(impedance)
    voltage = max_voltage * np.sin(angle + phase_angle)

    plt.figure(figsize=(10, 6))
    plt.plot(time, current, label='Current (A)', color='blue')
    plt.plot(time, voltage, label='Voltage (V)', color='orange')
    plt.title('Current and Voltage in a Series RLC Circuit')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    return current, voltage
