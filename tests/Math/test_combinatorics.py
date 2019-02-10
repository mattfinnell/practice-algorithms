from PracticeAlgorithms.Math.Combinatorics import (
    factorial,
    combination,
    permutation
)

def test_factorial():
    assert factorial(3) == 6
    assert factorial(5) == 120

def test_permutation():
    assert permutation(52, 5) == 311875200

def test_combination(): 
    assert combination(52, 5) == 2598960