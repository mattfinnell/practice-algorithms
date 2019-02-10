from PracticeAlgorithms.DataStructures.Graphs import Graph, build_adjacency_table, Solution

import pytest

def test_build_adjacency_table_from_matrix(sample_matrix):
    result = build_adjacency_table(sample_matrix)

    assert result == {1 : [0], 0: [1], 2 : []}

def test_breadth_first_search_on_gg_graph(gg_graph : Graph):
    assert list(gg_graph.breadth_first_search(1)) == [1, 2, 3, 4, 5, 6]

def test_depth_first_search_on_gg_graph(gg_graph : Graph):
    assert list(gg_graph.depth_first_search(1)) == [1, 2, 4, 5, 3, 6]

def test_disjoint_count_on_graph_of_two_disjoints(disjoint_graphs_1):
    pass

def test_disjoint_count_on_graph_of_one_disjoints(disjoint_graphs_2):
    pass

def test_foo(islands_1):
    solution = Solution()

    assert solution.numIslands(islands_1) == 1

def test_bar(islands_2):
    solution = Solution()

    assert solution.numIslands(islands_2) == 3

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

@pytest.fixture
def sample_matrix():
    return [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

@pytest.fixture
def gg_graph():
    adjacency_table = {
        1 : [2, 3],
        2 : [1, 4, 5],
        3 : [1, 5],
        4 : [2, 5, 6],
        5 : [3, 2, 4, 6],
        6 : [4, 5]
    }

    return Graph(adjacency_table)

@pytest.fixture
def disjoint_graphs_1():
    return [[1,1,0],[1,1,0],[0,0,1]]

@pytest.fixture
def disjoint_graphs_2():
    return [[1,1,0],[1,1,1],[0,1,1]]