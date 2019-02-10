from PracticeAlgorithms.LeetCodeQuestions.DynamicProgramming import max_subarray_skip_sum

import pytest

def test_on_sample_1(sample_1):
    assert max_subarray_skip_sum(sample_1) == 12

def test_on_sample_2(sample_2):
    assert max_subarray_skip_sum(sample_2) == 4

def test_on_sample_3(sample_3):
    assert max_subarray_skip_sum(sample_3) == 4

def test_on_sample_4(sample_4):
    assert max_subarray_skip_sum(sample_4) == 14

def test_on_empty_list(sample_4):
    assert max_subarray_skip_sum([]) == 0

@pytest.fixture
def sample_1():
    return [2,7,9,3,1]

@pytest.fixture
def sample_2():
    return [1,2,3,1]

@pytest.fixture
def sample_3():
    return [2,1,1,2]

@pytest.fixture
def sample_4():
    return [4,1,2,7,5,3,1]