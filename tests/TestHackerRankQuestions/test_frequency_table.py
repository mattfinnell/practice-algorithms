from PracticeAlgorithms.HackerRankQuestions.Utilities import FrequencyTable

import pytest

@pytest.fixture
def basic_table():
    return FrequencyTable([1, 2, 2])

@pytest.fixture
def string_a():
    return "aaaabbbccdefghi"

@pytest.fixture
def string_b():
    return "aabbbdehi"

def test_frequency_table_is_initializable(string_a):
    assert FrequencyTable(string_a)

def test_frequency_table_with_intersectable_iterables(string_a, string_b):
    table_a = FrequencyTable(string_a)
    table_b = FrequencyTable(string_b)

    result = table_a.intersection(table_b)

    expected = { 'a': 2, 'b': 3, 'd': 1, 'e': 1, 'h': 1, 'i': 1 } 

    assert result == expected

def test_frequency_table_when_adding_a_new_element(basic_table):
    basic_table[3]

    assert basic_table == {1:1, 2: 2, 3: 1}

def test_frequency_table_when_removing_an_element_with_one_occurance(basic_table):
    del basic_table[1]

    assert basic_table == {2: 2}

def test_frequency_table_when_removing_an_element_with_multiple_occurances(basic_table):
    del basic_table[2]

    assert basic_table == {1:1, 2: 1}

def test_frequency_table_when_iterating_over_key_value_pairs(basic_table):
    result = [(key, value) for key, value in basic_table.items()]

    assert result == [item for item in [(1, 1), (2, 2)]]