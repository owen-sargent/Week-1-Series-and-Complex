import astropy.units as u
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pytest

import complexmod as complex_module


def test_complex_polar_matches_expected_magnitude_and_angle():
    """Polar conversion should return magnitude and principal angle in radians."""
    result = complex_module.complex_polar(1.0 + 1.0j)
    r, theta = result
    assert r == pytest.approx(np.sqrt(2.0), rel=1e-12, abs=1e-12)
    assert theta == pytest.approx(np.pi / 4.0, rel=1e-12, abs=1e-12)

    result = complex_module.complex_polar(-1.0 + 1.0j)
    r, theta = result
    assert r == pytest.approx(np.sqrt(2.0), rel=1e-12, abs=1e-12)
    assert theta == pytest.approx(3.0 * np.pi / 4.0, rel=1e-12, abs=1e-12)


def test_nth_root_returns_n_valid_roots():
    """Each returned root should satisfy root**n = z within floating-point tolerance."""
    z = 16.0 + 0.0j
    n = 4
    roots = complex_module.nth_root(z, n)

    assert hasattr(roots, "__len__")
    assert len(roots) == n

    powered = np.asarray(roots, dtype=complex) ** n
    assert np.allclose(powered, z, rtol=1e-9, atol=1e-9)


def test_nth_root_of_one_contains_expected_unit_roots():
    """The 4th roots of unity should include +/-1 and +/-i."""
    roots = np.asarray(complex_module.nth_root(1.0 + 0.0j, 4), dtype=complex)
    assert roots.size == 4

    expected = np.array([1.0 + 0.0j, -1.0 + 0.0j, 0.0 + 1.0j, 0.0 - 1.0j], dtype=complex)
    for target in expected:
        assert np.any(np.isclose(roots, target, rtol=1e-8, atol=1e-8))


def test_complex_impedance_matches_reference_value():
    """Impedance should match an independently computed reference for this case."""
    resistance = 10.0
    inductance = 0.2
    capacitance = 1.0e-3
    omega = 50.0

    z = complex_module.complex_impedance(resistance, inductance, capacitance, omega)
    expected = 10.0 - 10.0j
    assert z == pytest.approx(expected, rel=1e-12, abs=1e-12)


def test_plot_rlc_returns_series_and_draws_plot():
    """RLC helper should return voltage/current arrays and create at least one plot line."""
    plt.close("all")

    resistance = 10.0
    inductance = 0.1
    capacitance = 1.0e-3
    omega = 20.0
    time = np.linspace(0.0, 1.0, 200)
    max_current = 2.0

    result = complex_module.plot_rlc(resistance, inductance, capacitance, omega, time, max_current)

    assert isinstance(result, tuple)
    assert len(result) == 2
    current, voltage = result
    assert np.shape(voltage) == np.shape(time)
    assert np.shape(current) == np.shape(time)

    assert plt.gcf().axes
    assert len(plt.gca().lines) >= 1

    plt.close("all")


def test_plot_rlc_accepts_astropy_quantities():
    """RLC plotting should work with astropy quantities and still return plottable arrays."""
    plt.close("all")

    resistance = u.Quantity(12.0, u.ohm)
    inductance = u.Quantity(15.0e-3, u.henry)
    capacitance = u.Quantity(220.0e-6, u.farad)
    omega = 2.0 * np.pi * 60.0 / u.s
    time = np.linspace(0.0, 6.0 / 60.0, 300) * u.s
    max_current = u.Quantity(1.5, u.ampere)

    result = complex_module.plot_rlc(resistance, inductance, capacitance, omega, time, max_current)

    assert isinstance(result, tuple)
    assert len(result) == 2
    current, voltage = result
    assert np.shape(voltage) == np.shape(time)
    assert np.shape(current) == np.shape(time)

    assert plt.gcf().axes
    assert len(plt.gca().lines) >= 1

    plt.close("all")
