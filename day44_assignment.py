class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_path_sum(root, target):
    # Store prefix sums and their frequencies
    prefix_count = {0: 1}

    def dfs(node, running):
        # Base case
        if node is None:
            return 0

        # Step 1: Update running prefix sum
        running += node.value

        # Step 2: Find required earlier prefix sum
        needed = running - target

        # Step 3: Count matching paths
        total = prefix_count.get(needed, 0)

        # Step 4: Add current prefix sum
        prefix_count[running] = (
            prefix_count.get(running, 0) + 1
        )

        # Step 5: Explore left subtree
        total += dfs(node.left, running)

        # Step 6: Explore right subtree
        total += dfs(node.right, running)

        # Step 7: Backtracking - remove current prefix
        prefix_count[running] -= 1

        if prefix_count[running] == 0:
            del prefix_count[running]

        return total

    return dfs(root, 0)


# Build the assignment binary tree
def build_assignment_tree():
    return TreeNode(
        1,
        TreeNode(
            -1,
            TreeNode(1)
        ),
        TreeNode(
            1,
            right=TreeNode(-1)
        )
    )


# Run assignment test cases
def run_assignment():
    root = build_assignment_tree()

    print("DAY 44 ASSIGNMENT - PATH SUM III")
    print("--------------------------------")
    test_cases = [
    (1, 5),
    (0, 3),
    (-1, 2),
    (5, 0),
]
   
    for target, expected in test_cases:
        result = count_path_sum(root, target)

        print(
            f"Target: {target}, "
            f"Count: {result}, "
            f"Expected: {expected}"
        )

        assert result == expected, (
            f"Test failed for target {target}"
        )

    # Additional test: Empty tree
    empty_result = count_path_sum(None, 0)
    assert empty_result == 0
    print("Empty tree test: Passed")

    # Additional test: Single node
    single_node = TreeNode(5)
    assert count_path_sum(single_node, 5) == 1
    assert count_path_sum(single_node, 10) == 0
    print("Single node test: Passed")

    # Additional test: Three zero-valued nodes
    zero_tree = TreeNode(
        0,
        TreeNode(0, TreeNode(0))
    )

    assert count_path_sum(zero_tree, 0) == 6
    print("Repeated prefix sum test: Passed")

    print("\nAll assignment test cases passed!")


if __name__ == "__main__":
    run_assignment()
