from PracticeAlgorithms.DataStructures.MinHeap import MinHeap, heapsort

import pytest
import math

def test_heap_sort():
    assert heapsort([5,4,3,2,1]) == [1,2,3,4,5]
    assert heapsort([4,3,5,2,1]) == [1,2,3,4,5]

def test_arrange_min_heap_from_reversed_list(min_heap):
    assert min_heap._arr == [1,2,4,5,3]

def test_pop_item_from_min_heap(min_heap):
    assert min_heap.pop() == 1
    assert min_heap._arr == [2,3,4,5]

    assert min_heap.pop() == 2
    assert min_heap._arr == [3,5,4]

def test_min_child_index(min_heap):
    assert min_heap._min_child_index(0) == 1
    assert min_heap._min_child_index(1) == 4
    assert min_heap._min_child_index(2) == min_heap.MAXINT

def test_parent_index_calculations(min_heap):
    assert min_heap._parent_index(0) == -1
    assert min_heap._parent_index(1) == 0
    assert min_heap._parent_index(2) == 0
    assert min_heap._parent_index(3) == 1
    assert min_heap._parent_index(4) == 1
    assert min_heap._parent_index(5) == 2

def test_left_child_index_calculations(min_heap):
    assert min_heap._left_child_index(0) == 1
    assert min_heap._left_child_index(1) == 3
    assert min_heap._left_child_index(2) == 5
    assert min_heap._left_child_index(3) == 7
    assert min_heap._left_child_index(4) == 9
    assert min_heap._left_child_index(5) == 11

def test_right_child_index_calculations(min_heap):
    assert min_heap._right_child_index(0) == 2
    assert min_heap._right_child_index(1) == 4
    assert min_heap._right_child_index(2) == 6
    assert min_heap._right_child_index(3) == 8
    assert min_heap._right_child_index(4) == 10
    assert min_heap._right_child_index(5) == 12

@pytest.fixture
def min_heap():
    return MinHeap(REVERSED_LIST)

REVERSED_LIST = [5, 4, 3, 2, 1]