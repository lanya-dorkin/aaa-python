import pytest
from one_hot_encoder import fit_transform


def test_fit_transform_single_arg():
    result = fit_transform("a", "b", "c")
    expected = [("a", [0, 0, 1]), ("b", [0, 1, 0]), ("c", [1, 0, 0])]
    assert result == expected


def test_fit_transform_multiple_args():
    result = fit_transform(["yes", "no", "not_a_number"])
    expected = [
        ("yes", [0, 0, 1]),
        ("no", [0, 1, 0]),
        ("not_a_number", [1, 0, 0])
    ]
    assert result == expected


def test_fit_transform_empty_args():
    with pytest.raises(TypeError):
        fit_transform()


def test_fit_transform_duplicate_args():
    result = fit_transform("a", "b", "a", "c", "b")
    not_expected = [('x', [1, 0, 0]), ('y', [0, 1, 0]), ('z', [0, 0, 1])]
    assert result != not_expected
