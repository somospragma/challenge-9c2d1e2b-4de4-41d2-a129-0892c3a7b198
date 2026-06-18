import pytest
from src.filter import filter_data

def test_filter_data():
    data = [1, 2, 3, 4]
    filter_function = lambda x: x % 2 == 0
    expected_result = [2, 4]
    assert list(filter_data(data, filter_function)) == expected_result