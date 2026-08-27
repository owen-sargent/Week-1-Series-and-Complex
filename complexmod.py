"""Student assignment implementation file for complex analysis."""
import cmath as cm
import math
import numpy as np
from astropy import units as u
from astropy.units import Quantity as Q
import matplotlib.pyplot as plt

# --- Student Assignment --- #
# --- General --- #
def complex_polar(z):
    """Convert a complex number to polar form.

    This function takes a complex number z and returns its polar form as a tuple
    (r, theta), where r is the magnitude of z and theta is the angle in radians.

    """
    r = abs(z)
    theta = cm.phase(z)
    theta_deg = math.degrees(theta)
    return (r, theta)
    


def nth_root(z, n):
    """Compute the n-th roots of a complex number.

    This function takes a complex number z and an integer n, and returns
    all of the  the n-th roots (see Boas 2.10) of z as a complex number
    as a numpy array.

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
    """Compute the complex impedance of a series RLC circuit.

    This function takes the resistance R, inductance L, capacitance C, and angular frequency omega
    of a series RLC circuit and returns the complex impedance Z as a complex number.

    """
    impedance = R + 1j*(W*L-1/(W*C))

    return impedance


# See Boas Example 2.16 - Electricity
def plot_rlc(resistance, inductance, capacitance, omega, time, max_current, filename=None):
    """Plot the current and voltage time series of a series RLC circuit.

    This function takes the resistance R, inductance L, capacitance C, angular frequencies
    omega, and time array and generates the voltage and current signal for the
    series RLC circuit. The function also returns the current (first) and voltage (second)
    signals as numpy arrays.

    If filename is not None, save the generated figure to that filename.

    Must be astropy quantitiy friendly (could be a non astorpy quantity, but if it is an astropy quantity, it should be handled correctly).

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

    angle = omega * time

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
