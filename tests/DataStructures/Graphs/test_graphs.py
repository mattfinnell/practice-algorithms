from PracticeAlgorithms.DataStructures.Graphs import Graph, build_adjacency_table

import pytest

def test_build_adjacency_table_from_matrix(sample_matrix):
    result = build_adjacency_table(sample_matrix)

    assert result == {1 : [0], 0: [1], 2 : []}

def test_breadth_first_search_on_gg_graph(gg_graph : Graph):
    assert list(gg_graph.breadth_first_search(1)) == [1, 2, 3, 4, 5, 6]

def test_depth_first_search_on_gg_graph(gg_graph : Graph):
    assert list(gg_graph.depth_first_search(1)) == [1, 2, 4, 5, 3, 6]

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