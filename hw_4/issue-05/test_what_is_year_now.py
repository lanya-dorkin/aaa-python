import pytest
from unittest.mock import patch, mock_open
from what_is_year_now import what_is_year_now
import json


def test_what_is_year_now_with_valid_YMD_format():
    mock_file = mock_open(
        read_data=json.dumps({"currentDateTime": "2023-11-06"})
    )
    with patch('urllib.request.urlopen', mock_file):
        result = what_is_year_now()
        assert result == 2023


def test_what_is_year_now_with_valid_DMY_format():
    mock_file = mock_open(
        read_data=json.dumps({"currentDateTime": "06.11.2023"})
    )
    with patch('urllib.request.urlopen', mock_file):
        result = what_is_year_now()
        assert result == 2023


def test_what_is_year_now_with_invalid_YMD_format():
    mock_file = mock_open(
        read_data=json.dumps({"currentDateTime": "2023/11/06"})
    )
    with patch('urllib.request.urlopen', mock_file):
        with pytest.raises(ValueError):
            what_is_year_now()
