from PracticeAlgorithms.DataStructures.LinkedLists import SinglyLinkedList
import pytest

@pytest.fixture
def linked_list_empty():
    return SinglyLinkedList()

@pytest.fixture
def linked_list_populated():
    linked_list = SinglyLinkedList()
    linked_list.append("foo")
    linked_list.append("bar")
    linked_list.append("baz")

    return linked_list

def test_empty(linked_list_empty):
    assert linked_list_empty.as_list() == []
    assert linked_list_empty.length() is 0 

def test_append(linked_list_empty):
    linked_list_empty.append("foo")

    assert linked_list_empty.as_list() == ["foo"]
    assert linked_list_empty.length() is 1

def test_append_many(linked_list_empty):
    linked_list_empty.append("foo")
    linked_list_empty.append("bar")
    linked_list_empty.append("baz")

    assert linked_list_empty.length() is 3
    assert linked_list_empty.as_list() == ["foo", "bar", "baz"]

def test_insert_by_index_at_beginning_of_populated_linked_list(linked_list_populated):
    linked_list_populated.insert_at_index(0, "new")

    assert linked_list_populated.length() == 4
    assert linked_list_populated.as_list() == ["new", "foo", "bar", "baz"]

def test_insert_by_index_at_middle_of_populated_linked_list(linked_list_populated):
    linked_list_populated.insert_at_index(2, "new")

    assert linked_list_populated.length() == 4
    assert linked_list_populated.as_list() == ["foo", "bar", "new", "baz"]

def test_insert_by_index_at_end_of_populated_linked_list(linked_list_populated):
    linked_list_populated.insert_at_index(3, "new")

    assert linked_list_populated.length() == 4
    assert linked_list_populated.as_list() == ["foo", "bar", "baz", "new"]

def test_insert_by_index_beyond_end_of_populated_linked_list(linked_list_populated):
    linked_list_populated.insert_at_index(10, "new")

    assert linked_list_populated.length() == 4
    assert linked_list_populated.as_list() == ["foo", "bar", "baz", "new"]

def test_insert_by_index_given_empty_linked_list(linked_list_empty):
    linked_list_empty.insert_at_index(10, "new")

    assert linked_list_empty.length() == 1
    assert linked_list_empty.as_list() == ["new"]

def test_search_given_populated_linked_list_and_item_exists(linked_list_populated):
    result = linked_list_populated.search("baz")
    
    assert result is 2

def test_search_given_populated_linked_list_and_item_does_not_exist(linked_list_populated):
    result = linked_list_populated.search("thing")

    assert result is -1

def test_search_given_empty_linked_list(linked_list_empty):
    result = linked_list_empty.search("thing")

    assert result is -1

def test_delete_by_index_given_empty_linked_list(linked_list_empty):
    linked_list_empty.delete_by_index(2)

    assert linked_list_empty.as_list() == []
    assert linked_list_empty.length() == 0

def test_delete_by_index_given_populated_linked_list_and_index_is_first_element(linked_list_populated):
    linked_list_populated.delete_by_index(0)

    assert linked_list_populated.as_list() == ["bar", "baz"]
    assert linked_list_populated.length() == 2

def test_delete_by_index_given_populated_linked_list_and_index_exists(linked_list_populated):
    linked_list_populated.delete_by_index(1)

    assert linked_list_populated.as_list() == ["foo", "baz"]
    assert linked_list_populated.length() == 2

def test_delete_by_index_given_populated_linked_list_and_index_does_not_exist(linked_list_populated):
    linked_list_populated.delete_by_index(10)

    assert linked_list_populated.as_list() == ["foo", "bar", "baz"]
    assert linked_list_populated.length() == 3

def test_delete_by_key_given_empty_linked_list(linked_list_empty):
    linked_list_empty.delete_by_key("bar")

    assert linked_list_empty.as_list() == []
    assert linked_list_empty.length() == 0

def test_delete_by_key_given_populated_linked_list_and_index_is_first_element(linked_list_populated):
    linked_list_populated.delete_by_key("foo")

    assert linked_list_populated.as_list() == ["bar", "baz"]
    assert linked_list_populated.length() == 2

def test_delete_by_key_given_populated_linked_list_and_index_exists(linked_list_populated):
    linked_list_populated.delete_by_key("bar")

    assert linked_list_populated.as_list() == ["foo", "baz"]
    assert linked_list_populated.length() == 2

def test_delete_by_key_given_populated_linked_list_and_index_does_not_exist(linked_list_populated):
    linked_list_populated.delete_by_key("non-existant")

    assert linked_list_populated.as_list() == ["foo", "bar", "baz"]
    assert linked_list_populated.length() == 3