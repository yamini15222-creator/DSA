
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_path_sum(root, target):
    prefix_count = {0: 1}

    def dfs(node, running):
        if node is None:
            return 0

        # 1. Update the current prefix sum
        running += node.value

        # 2. Count matching earlier prefixes
        needed = running - target
        total = prefix_count.get(needed, 0)

        # 3. Add the current prefix
        prefix_count[running] = prefix_count.get(running, 0) + 1

        # 4. Explore left and right subtrees
        total += dfs(node.left, running)
        total += dfs(node.right, running)

        # 5. Undo the current prefix before returning
        prefix_count[running] -= 1

        if prefix_count[running] == 0:
            del prefix_count[running]

        return total

    return dfs(root, 0)


def build_tree():
    return TreeNode(
        10,
        TreeNode(
            5,
            TreeNode(3, TreeNode(3), TreeNode(-2)),
            TreeNode(2, right=TreeNode(1))
        ),
        TreeNode(-3, right=TreeNode(11))
    )


def run_tests():
    root = build_tree()

    print("DAY 44 - PATH SUM III")
    print("----------------------")

    test_cases = [
        (8, 3),
        (18, 3),
        (10, 1),
        (100, 0),
    ]

    for target, expected in test_cases:
        result = count_path_sum(root, target)
        print(
            f"Target: {target}, "
            f"Count: {result}, "
            f"Expected: {expected}"
        )
        assert result == expected

    # Empty tree
    assert count_path_sum(None, 0) == 0

    # Single node
    assert count_path_sum(TreeNode(5), 5) == 1
    assert count_path_sum(TreeNode(5), 10) == 0

    # Repeated prefix sums: three zero-valued nodes
    zero_tree = TreeNode(0, TreeNode(0, TreeNode(0)))
    assert count_path_sum(zero_tree, 0) == 6

    # Negative values
    negative_tree = TreeNode(-2, TreeNode(-1), TreeNode(3))
    assert count_path_sum(negative_tree, -3) == 1

    print("\nAll test cases passed!")


if __name__ == "__main__":
    run_tests()
