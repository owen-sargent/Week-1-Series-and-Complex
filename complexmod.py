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
        fig, current_ax = plt.subplots(figsize=(10, 6))
        voltage_ax = current_ax.twinx()

        current_line = current_ax.plot(
            time,
            current,
            color="C0",
            label="Current",
        )

        voltage_line = voltage_ax.plot(
            time,
            voltage,
            color="C1",
            label="Voltage",
        )

        current_ax.set_title(
            "Current and Voltage in a Series RLC Circuit"
        )
        current_ax.set_xlabel("Time")
        current_ax.set_ylabel("Current", color="C0")
        voltage_ax.set_ylabel("Voltage", color="C1")

        current_ax.tick_params(axis="y", colors="C0")
        voltage_ax.tick_params(axis="y", colors="C1")
        current_ax.grid()

        lines = current_line + voltage_line
        current_ax.legend(
            lines,
            [line.get_label() for line in lines],
        )

        if filename is not None:
            fig.savefig(filename)
    return current, voltage
