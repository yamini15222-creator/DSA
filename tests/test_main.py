import pytest

from main import (
    TreeNode,
    is_balanced,
    longest_unique_substring,
    search_insert_position,
    subarray_sum_equals_k,
    subsets,
    two_sum,
)


def test_two_sum_normal():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_duplicate_values_use_different_indexes():
    assert two_sum([3, 3], 6) == [0, 1]


def test_two_sum_missing_pair_raises():
    with pytest.raises(ValueError):
        two_sum([1, 2, 3], 10)


def test_longest_unique_substring_normal():
    assert longest_unique_substring("abcabcbb") == 3


def test_longest_unique_substring_empty_and_single():
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("a") == 1


def test_longest_unique_substring_repeated_character():
    assert longest_unique_substring("abba") == 2


def test_subarray_sum_equals_k_normal():
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2


def test_subarray_sum_equals_k_negative_values():
    assert subarray_sum_equals_k([1, -1, 0], 0) == 3


def test_subarray_sum_equals_k_empty():
    assert subarray_sum_equals_k([], 0) == 0


def test_search_insert_position_middle_and_edges():
    nums = [1, 3, 5, 6]
    assert search_insert_position(nums, 5) == 2
    assert search_insert_position(nums, 2) == 1
    assert search_insert_position(nums, 7) == 4
    assert search_insert_position(nums, 0) == 0


def test_search_insert_position_empty():
    assert search_insert_position([], 4) == 0


def test_subsets_all_results_for_two_items():
    result = subsets([1, 2])
    assert len(result) == 4
    assert {tuple(item) for item in result} == {
        (), (1,), (2,), (1, 2)
    }


def test_subsets_empty_input():
    assert subsets([]) == [[]]


def test_balanced_binary_tree_empty_and_single_node():
    assert is_balanced(None) is True
    assert is_balanced(TreeNode(1)) is True


def test_balanced_binary_tree_balanced():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_balanced(root) is True


def test_balanced_binary_tree_unbalanced_chain():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert is_balanced(root) is False
