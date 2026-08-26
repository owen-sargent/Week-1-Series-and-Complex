import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pytest

import series


def test_harmonic_sums_first_terms():
    """The harmonic series should sum the first n reciprocal terms."""
    assert series.harmonic(1) == pytest.approx(1.0)
    assert series.harmonic(5) == pytest.approx(2.283333333333333)
    assert series.harmonic(1e100) == pytest.approx(230.836, rel=1e-3)

def test_harmonic_raises_value_error_for_non_positive_n_terms():
    """The harmonic series should raise a ValueError for non-positive n_terms."""
    with pytest.raises(ValueError):
        series.harmonic(0)
    with pytest.raises(ValueError):
        series.harmonic(-5)


def test_boas_1_13_4_matches_log1p():
    """The logarithm series should match ln(1 + x) for valid x values."""
    value, iterations = series.boas_1_13_4(0.0)
    assert value == pytest.approx(0.0)
    assert isinstance(iterations, int)

    value, iterations = series.boas_1_13_4(0.5)
    assert value == pytest.approx(np.log(1.5), rel=1e-7, abs=1e-12)
    assert isinstance(iterations, int)

    value, iterations = series.boas_1_13_4(-0.5)
    assert value == pytest.approx(np.log(0.5), rel=1e-7, abs=1e-12)
    assert isinstance(iterations, int)


def test_boas_1_13_22_matches_rational_exp_expression():
    """The function should evaluate the closed form exp(x) / (1 - x)."""
    value, iterations = series.boas_1_13_22(0.0, 1e-8, 100)
    assert value == pytest.approx(1.0)
    assert isinstance(iterations, int)

    value, iterations = series.boas_1_13_22(0.5, 1e-8, 100)
    assert value == pytest.approx(np.exp(0.5) / (1.0 - 0.5), rel=1e-7, abs=1e-12)
    assert isinstance(iterations, int)

    value, iterations = series.boas_1_13_22(-0.5, 1e-8, 100)
    assert value == pytest.approx(np.exp(-0.5) / (1.0 + 0.5), rel=1e-7, abs=1e-12)
    assert isinstance(iterations, int)


def test_boas_1_13_22_plot_creates_a_plot():
    """The plotting helper should generate a figure with at least one plotted curve."""
    plt.close("all")
    figure, axes = series.boas_1_13_22_plot(5)

    assert figure.axes
    assert len(axes.lines) >= 1
    if axes is not None:
        assert hasattr(axes, "lines") or hasattr(axes, "axes")

    plt.close("all")


def test_boas_1_16_1c_matches_harmonic_overhang_rule():
    """The stack problem uses the harmonic series to determine the minimum books."""
    assert series.boas_1_16_1c(0.5) == 2
    assert series.boas_1_16_1c(0.75) == 3
    assert series.boas_1_16_1c(1) >= 3
    assert series.boas_1_16_1c(2) == 32
    assert series.boas_1_16_1c(3) == 228
    assert series.boas_1_16_1c(10) >= 2.7e8
    assert series.boas_1_16_1c(10) <= 2.8e8
    assert series.boas_1_16_1c(100) >= 4.0e86
    assert series.boas_1_16_1c(100) <= 4.1e86


def test_cos_apprx_matches_cosine_taylor_series():
    """The cosine approximation should converge to the expected value for standard inputs."""
    value, n_terms = series.cos_apprx(0.0, rel_tol=1e-12, max_iter=1000)
    assert value == pytest.approx(1.0, rel=1e-12, abs=1e-12)
    assert isinstance(n_terms, int)
    assert n_terms >= 1

    value, n_terms = series.cos_apprx(np.pi / 3.0 + 2*np.pi, rel_tol=1e-12, max_iter=1000)
    assert value == pytest.approx(0.5, rel=1e-8, abs=1e-8)
    assert isinstance(n_terms, int)
    assert n_terms >= 1

    neg_value, _ = series.cos_apprx(-np.pi / 3.0, rel_tol=1e-12, max_iter=1000)
    assert neg_value == pytest.approx(value, rel=1e-8, abs=1e-8)
