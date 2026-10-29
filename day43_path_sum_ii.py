
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def path_sum(root, target):
    results = []
    path = []

    def dfs(node, remaining):
        if node is None:
            return

        # Choose: add the current node.
        path.append(node.value)
        remaining -= node.value

        is_leaf = node.left is None and node.right is None

        if is_leaf:
            # Save a copy only when the leaf matches.
            if remaining == 0:
                results.append(path.copy())
        else:
            # Explore both branches in left-first DFS order.
            dfs(node.left, remaining)
            dfs(node.right, remaining)

        # Undo: restore the working path.
        path.pop()

    dfs(root, target)
    return results


# --------------------------------------------------
# Build the original lesson tree
# --------------------------------------------------

root = TreeNode(
    5,
    left=TreeNode(
        4,
        left=TreeNode(
            11,
            left=TreeNode(7),
            right=TreeNode(2)
        )
    ),
    right=TreeNode(
        8,
        left=TreeNode(13),
        right=TreeNode(
            4,
            left=TreeNode(5),
            right=TreeNode(1)
        )
    )
)


# --------------------------------------------------
# Tests
# --------------------------------------------------

def run_tests():
    # Empty tree
    assert path_sum(None, 0) == []

    # Single-node tree
    assert path_sum(TreeNode(7), 7) == [[7]]
    assert path_sum(TreeNode(7), 8) == []

    # Original lesson: two matching paths
    assert path_sum(root, 22) == [
        [5, 4, 11, 2],
        [5, 8, 4, 5]
    ]

    # No matching path
    assert path_sum(root, 9) == []

    # Matching an internal prefix is not sufficient.
    assert path_sum(root, 9) == []

    # Negative values
    negative_tree = TreeNode(
        5,
        left=TreeNode(-3)
    )
    assert path_sum(negative_tree, 2) == [[5, -3]]

    # Zero-valued leaf
    assert path_sum(TreeNode(0), 0) == [[0]]

    # Two different routes with identical values
    duplicate_tree = TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(2)
    )
    assert path_sum(duplicate_tree, 3) == [
        [1, 2],
        [1, 2]
    ]

    # Separate calls must not share results
    assert path_sum(TreeNode(0), 0) == [[0]]
    assert path_sum(None, 0) == []

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()

    print("\nMatching paths for target 22:")
    print(path_sum(root, 22))
