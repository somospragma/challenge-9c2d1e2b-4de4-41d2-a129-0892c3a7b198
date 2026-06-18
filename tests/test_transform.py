import pytest
from src.transform import transform_data

def test_transform_data():
    data = [1, 2, 3, 4]
    transformation_function = lambda x: x * 2
    expected_result = [2, 4, 6, 8]
    assert list(transform_data(data, transformation_function)) == expected_result