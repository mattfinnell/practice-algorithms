from PracticeAlgorithms.DataStructures.Arrays.Hourglass import (
    apply_hourglass_filter, 
    calculate_hourglass_sum,
    hourglass_max_sum
)

import pytest

@pytest.fixture
def sample_grid():
    return [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

@pytest.fixture
def small_grid():
    return [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

@pytest.fixture
def medium_grid():
    return [
        [1,2,3,4],
        [5,6,7,8],
        [9,0,1,2],
    ]

def test_filter_on_small_grid(small_grid):
    expected_hourglass = [
        [1,2,3],
        [0,5,0],
        [7,8,9]
    ]

    assert apply_hourglass_filter(small_grid, 0, 0) == expected_hourglass

def test_filter_on_medium_grid(medium_grid):
    expected_hourglass_a = [
        [1,2,3],
        [0,6,0],
        [9,0,1]
    ]

    expected_hourglass_b = [
        [2,3,4],
        [0,7,0],
        [0,1,2]
    ]

    assert apply_hourglass_filter(medium_grid, 0, 0) == expected_hourglass_a
    assert apply_hourglass_filter(medium_grid, 0, 1) == expected_hourglass_b

def test_hourglass_sum_on_small_grid(small_grid):
    result = calculate_hourglass_sum(apply_hourglass_filter(small_grid, 0, 0)) 

    assert result == 35

def test_hourglass_max_sum_on_sample_grid(sample_grid):
    assert hourglass_max_sum(sample_grid) == 19