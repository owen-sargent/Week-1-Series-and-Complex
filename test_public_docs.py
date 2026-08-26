import pytest
from numpydoc.validate import validate

import series, complexmod


DOCSTRING_TARGETS = [
    series.boas_1_13_22,
    series.boas_1_13_22_plot,
    series.boas_1_13_4,
    series.boas_1_16_1c,
    series.cos_apprx,
    series.harmonic,
    complexmod.complex_impedance,
    complexmod.complex_polar,
    complexmod.nth_root,
    complexmod.plot_rlc
]

DOCSTRING_CHECKS = {
    "GL08",
    "PR01",
    "PR02",
    "PR03",
    "PR04",
    "PR05",
    "PR06",
    "PR07",
    "PR08",
    "PR09",
    "PR10",
    "RT01",
    "RT02",
    "RT03",
    "RT04",
    "RT05",
}


@pytest.mark.parametrize("func", DOCSTRING_TARGETS, ids=lambda func: func.__name__)
def test_numpy_style_docstrings_for_inputs_and_outputs(func):
    validation = validate(f"{func.__module__}.{func.__name__}")
    relevant_errors = [
        f"{code}: {message}"
        for code, message in sorted(validation["errors"])
        if code in DOCSTRING_CHECKS
    ]

    assert not relevant_errors, (
        f"{func.__name__} must document its inputs and outputs in NumPy style:\n"
        + "\n".join(relevant_errors)
    )
