import pytest
from morse import decode


test_cases = [
    ("... --- ...", "SOS"),
    (" .- ...- .. - ---", "AVITO"),
    (" .---- ...-- ...-- --...", "1337")
]


@pytest.mark.parametrize('morse_input, expected_output', test_cases)
def test_decode(morse_input, expected_output):
    assert decode(morse_input) == expected_output
