"""Six DSA checkpoint solutions from the Days 1–40 revision plan."""

from typing import Optional


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indexes of two different elements whose sum is target.

    Contract:
    - Returns the first matching pair found during a left-to-right scan.
    - Raises ValueError if no pair exists.
    - Does not modify nums.

    Expected time: O(n); auxiliary space: O(n).
    """
    seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        needed = target - value
        if needed in seen:
            return [seen[needed], index]
        seen[value] = index
    raise ValueError("No two numbers add up to target")


def longest_unique_substring(s: str) -> int:
    """Return the length of the longest substring without repeated characters.

    Expected time: O(n); auxiliary space: O(min(n, alphabet size)).
    """
    last_seen: dict[str, int] = {}
    left = 0
    best = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        best = max(best, right - left + 1)

    return best


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """Count contiguous subarrays whose sum equals k.

    Works with positive, zero, and negative integers.
    Expected time: O(n); auxiliary space: O(n).
    """
    prefix_count = {0: 1}
    prefix_sum = 0
    answer = 0

    for value in nums:
        prefix_sum += value
        answer += prefix_count.get(prefix_sum - k, 0)
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return answer


def search_insert_position(nums: list[int], target: int) -> int:
    """Return target's index, or its insertion position in sorted nums.

    Contract:
    - nums must be sorted in nondecreasing order.
    - Returns an index in [0, len(nums)].
    - Does not modify nums.

    Time: O(log n); auxiliary space: O(1).
    """
    left, right = 0, len(nums)  # half-open interval [left, right)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def subsets(nums: list[int]) -> list[list[int]]:
    """Return all subsets of nums.

    Assumes nums contains distinct values, so each subset is unique.
    Time: O(n * 2^n) including copying results.
    Auxiliary working space: O(n), excluding output.
    """
    result: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        result.append(path.copy())
        for index in range(start, len(nums)):
            path.append(nums[index])   # choose
            backtrack(index + 1)       # explore
            path.pop()                 # undo

    backtrack(0)
    return result


class TreeNode:
    """A binary-tree node."""
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode | None) -> bool:
    """Return whether every node's subtree heights differ by at most one.

    Helper returns a height in nodes, or -1 if that subtree is unbalanced.
    Time: O(n); auxiliary recursive stack: O(h), where h is tree height.
    """
    def height_or_failure(node: TreeNode | None) -> int:
        if node is None:
            return 0

        left_height = height_or_failure(node.left)
        if left_height == -1:
            return -1

        right_height = height_or_failure(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return height_or_failure(root) != -1


def demo() -> None:
    print("Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("Longest unique substring:", longest_unique_substring("abcabcbb"))
    print("Subarray sum equals K:", subarray_sum_equals_k([1, 1, 1], 2))
    print("Search insert position:", search_insert_position([1, 3, 5, 6], 2))
    print("Subsets:", subsets([1, 2]))

    balanced_tree = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Balanced binary tree:", is_balanced(balanced_tree))


if __name__ == "__main__":
    demo()
