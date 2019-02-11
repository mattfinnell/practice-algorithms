from PracticeAlgorithms.SortingAlgorithms import (
    insertion_sort,
    selection_sort,
    bubble_sort,
    heap_sort,
    merge_sort,
    quick_sort
)

from functools import reduce

import pytest

def test_insertion_sort_on_reversed_list(reversed_values):
    assert is_sorted(insertion_sort(reversed_values))

def test_insertion_sort_on_random_list(random_values):
    assert is_sorted(insertion_sort(random_values))

def test_insertion_sort_on_sorted_list(sorted_values):
    assert is_sorted(insertion_sort(sorted_values))

def test_selection_sort_on_reversed_list(reversed_values):
    assert is_sorted(selection_sort(reversed_values))

def test_selection_sort_on_random_list(random_values):
    assert is_sorted(selection_sort(random_values))

def test_selection_sort_on_sorted_list(sorted_values):
    assert is_sorted(selection_sort(sorted_values))

def test_bubble_sort_on_reversed_list(reversed_values):
    assert is_sorted(bubble_sort(reversed_values))

def test_bubble_sort_on_random_list(random_values):
    assert is_sorted(bubble_sort(random_values))

def test_bubble_sort_on_sorted_list(sorted_values):
    assert is_sorted(bubble_sort(sorted_values))

def test_heap_sort_on_reversed_list(reversed_values):
    assert is_sorted(heap_sort(reversed_values))

def test_heap_sort_on_random_list(random_values):
    assert is_sorted(heap_sort(random_values))

def test_heap_sort_on_sorted_list(sorted_values):
    assert is_sorted(heap_sort(sorted_values))

def test_merge_sort_on_reversed_list(reversed_values):
    assert is_sorted(merge_sort(reversed_values))

def test_merge_sort_on_random_list(random_values):
    assert is_sorted(merge_sort(random_values))

def test_merge_sort_on_sorted_list(sorted_values):
    assert is_sorted(merge_sort(sorted_values))

def test_quick_sort_on_reversed_list(reversed_values):
    assert is_sorted(quick_sort(reversed_values))

def test_quick_sort_on_random_list(random_values):
    assert is_sorted(quick_sort(random_values))

def test_quick_sort_on_sorted_list(sorted_values):
    assert is_sorted(quick_sort(sorted_values))

@pytest.fixture
def sorted_values():
    return list(range(1, 30))

@pytest.fixture
def reversed_values():
    return list(reversed(range(1, 30)))

@pytest.fixture
def random_values():
    return [1,-5,7,6,-2,6,-7,4,-1]

def is_sorted(Arr): 
    return reduce(lambda a, b: a < b, Arr)