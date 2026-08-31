"""Student assignment implementation file for complex analysis."""
import cmath as cm
import numpy as np
from astropy import units as u
from astropy.units import Quantity as Q
from astropy.visualization import quantity_support
import matplotlib.pyplot as plt
from typing import Any
from numpy.typing import NDArray


# --- Student Assignment --- #
# --- General --- #
def complex_polar(z: complex) -> tuple[float, float]:
    """Convert a complex number to polar form.

    Parameters
    ----------
    z : complex
        The complex number to convert.

    Returns
    -------
    tuple[float, float]
        A tuple containing the magnitude (r) and phase (theta) in radians.
    """
    r = abs(z)
    theta = cm.phase(z)
    return (r, theta)


def nth_root(z: complex, n: int) -> NDArray[np.complex128]:
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
def complex_impedance(R: float, L: float, C: float, W: float) -> complex:
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
def plot_rlc(
        resistance: float,
        inductance: float,
        capacitance: float,
        omega: float,
        time: NDArray[np.float64],
        max_current: float,
        filename: str | None = None
        ) -> tuple[Any, Any]:
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

    impedance = complex_impedance(resistance, inductance, capacitance, omega)

    angle = omega * time

    if isinstance(angle, Q):
        angle = angle.to(
            u.rad,
            equivalencies=u.dimensionless_angles(),
            )

    current = max_current * np.sin(angle)

    phase_angle = np.arctan2(impedance.imag, impedance.real)

    max_voltage = max_current * abs(impedance)
    voltage = max_voltage * np.sin(angle + phase_angle)

    with quantity_support():
        fig, axes = plt.subplots(2, 1, sharex=True)

        axes[0].plot(
            time,
            current,
        )

        axes[1].plot(
            time,
            voltage,
        )

        axes[0].set_title(
            "Current and Voltage in Series RLC Circuit"
        )

        axes[0].set_ylabel("Current (A)")
        axes[1].set_ylabel("Voltage (V)")
        axes[1].set_xlabel("Time (s)")

        if filename is not None:
            fig.savefig(filename)
    return current, voltage
