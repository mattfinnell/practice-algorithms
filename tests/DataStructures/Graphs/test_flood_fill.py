from PracticeAlgorithms.DataStructures.Graphs.FloodFill import (
    flood_fill_dfs, 
    flood_fill_bfs
)

import pytest

def test_flood_fill_dfs_against_sample_1(sample_1):
    assert flood_fill_dfs(sample_1, 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]

def test_flood_fill_dfs_against_sample_2(sample_2):
    assert flood_fill_dfs(sample_2, 1, 1, 1)  == sample_2

def test_flood_fill_bfs_against_sample_1(sample_1):
    assert flood_fill_bfs(sample_1, 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]

def test_flood_fill_bfs_against_sample_2(sample_2):
    assert flood_fill_bfs(sample_2, 1, 1, 1)  == sample_2

@pytest.fixture
def sample_1():
    return [[1,1,1],[1,1,0],[1,0,1]]
    
@pytest.fixture
def sample_2():
    return [[0,0,0],[0,1,1]]