from PracticeAlgorithms.HackerRankQuestions.StepsOfDavid import step_perms

import pytest

hackerrank_values = [
    (5, 13),
    (7, 44),
    (8, 81),
]

def test_base_cases():
    assert step_perms(0) == 0
    assert step_perms(1) == 1
    assert step_perms(2) == 2
    assert step_perms(3) == 4

def test_first_non_base_case():
    assert step_perms(4) == 7

@pytest.mark.parametrize("n, expected", hackerrank_values)
def test_on_hackerrank_values(n, expected):
    assert step_perms(n) == expected