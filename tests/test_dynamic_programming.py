from PracticeAlgorithms.DynamicProgramming.RobotPathSearch import robot_path
import pytest

@pytest.fixture
def trivial_grid():
    return [[True]]

@pytest.fixture
def sample_grid():
    return [
        [True, True, True],
        [True, True, True],
        [True, True, True],
    ]

@pytest.fixture
def obstacle_grid():
    return [
        [True, True, True],
        [False, True, True],
        [True, False, True],
    ]

def test_against_trvial_grid(trivial_grid):
    result = robot_path(trivial_grid)

    assert result == [(0, 0)]

def test_against_sample_grid(sample_grid):
    result = robot_path(sample_grid)

    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

def test_against_obstacle_grid(obstacle_grid):
    result = robot_path(obstacle_grid)

    assert result == [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]