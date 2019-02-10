from PracticeAlgorithms.DataStructures.Graphs.IslandCount import Solution

import pytest

def test_foo(solution, islands_1):
    assert solution.numIslands(islands_1) == 1

def test_bar(solution, islands_2):
    assert solution.numIslands(islands_2) == 3

@pytest.fixture
def solution():
    return Solution()

@pytest.fixture
def islands_2():
    return [
        ["1","1","0","0","0"], 
        ["1","1","0","0","0"], 
        ["0","0","1","0","0"], 
        ["0","0","0","1","1"]
    ]

@pytest.fixture
def islands_1():
    return [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]