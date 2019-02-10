from PracticeAlgorithms.DataStructures.BinaryTrees import BinarySearchTree
import pytest

@pytest.fixture
def tree_empty():
    return BinarySearchTree()

@pytest.fixture
def tree_balanced():
    tree = BinarySearchTree()

    values = [4, 2, 6, 1, 3, 5, 7]
    for value in values:
        tree.insert(value)
    
    return tree

@pytest.fixture
def tree_imbalanced():
    tree = BinarySearchTree()

    values = [6, 5, 4, 2, 3, 1, 7]
    for value in values:
        tree.insert(value)
    
    return tree

def test_empty_binary_tree(tree_empty : BinarySearchTree):
    assert tree_empty.size() == 0
    assert tree_empty.inorder() == []
    assert tree_empty.preorder() == []
    assert tree_empty.postorder() == []

def test_tree_size_on_balanced_tree(tree_balanced : BinarySearchTree):
    assert tree_balanced.size() == 7

def test_tree_size_on_imbalanced_tree(tree_imbalanced : BinarySearchTree):
    assert tree_imbalanced.size() == 7

def test_tree_size_on_custom_tree():
    tree = BinarySearchTree()

    for item in [5, 3, 1]:
        tree.insert(item)

    assert tree.size() == 3

def test_preorder_traversal_on_balanced_tree(tree_balanced : BinarySearchTree):
    assert tree_balanced.preorder() == [4, 2, 1, 3, 6, 5, 7]

def test_inorder_traversal_on_balanced_tree(tree_balanced : BinarySearchTree):
    assert tree_balanced.inorder() == [1, 2, 3, 4, 5, 6, 7]

def test_postorder_traversal_on_balanced_tree(tree_balanced : BinarySearchTree):
    assert tree_balanced.postorder() == [1, 3, 2, 5, 7, 6, 4]

def test_preorder_traversal_on_imbalanced_tree(tree_imbalanced : BinarySearchTree):
    assert tree_imbalanced.preorder() == [6, 5, 4, 2, 1, 3, 7]

def test_inorder_traversal_on_imbalanced_tree(tree_imbalanced : BinarySearchTree):
    assert tree_imbalanced.inorder() == [1, 2, 3, 4, 5, 6, 7]

def test_postorder_traversal_on_imbalanced_tree(tree_imbalanced : BinarySearchTree):
    assert tree_imbalanced.postorder() == [1, 3, 2, 4, 5, 7, 6]

def test_search_for_item_in_empty_tree(tree_empty : BinarySearchTree):
    assert not tree_empty.search(5)

def test_search_for_existing_item_in_balanced_tree(tree_balanced : BinarySearchTree):
    assert tree_balanced.search(5)

def test_search_for_existing_item_in_imbalanced_tree(tree_imbalanced : BinarySearchTree):
    assert tree_imbalanced.search(5)

def test_search_for_non_existing_item_in_balanced_tree(tree_balanced : BinarySearchTree):
    assert not tree_balanced.search(20)

def test_search_for_non_existing_item_in_imbalanced_tree(tree_imbalanced : BinarySearchTree):
    assert not tree_imbalanced.search(20)