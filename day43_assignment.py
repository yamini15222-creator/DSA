
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

        # Choose
        path.append(node.value)
        remaining -= node.value

        is_leaf = node.left is None and node.right is None

        if is_leaf:
            if remaining == 0:
                results.append(path.copy())
        else:
            # Explore left first, then right
            dfs(node.left, remaining)
            dfs(node.right, remaining)

        # Undo
        path.pop()

    dfs(root, target)
    return results


def count_path_sums(root, target):
    if root is None:
        return 0

    remaining = target - root.value

    if root.left is None and root.right is None:
        return 1 if remaining == 0 else 0

    return (
        count_path_sums(root.left, remaining)
        + count_path_sums(root.right, remaining)
    )


# Build the assignment tree
root = TreeNode(
    10,
    left=TreeNode(
        5,
        left=TreeNode(
            3,
            left=TreeNode(-2)
        ),
        right=TreeNode(
            2,
            right=TreeNode(1)
        )
    ),
    right=TreeNode(
        -3,
        right=TreeNode(11)
    )
)


# Print results
print("Target 18:", path_sum(root, 18))
print("Target 16:", path_sum(root, 16))
print("Target 15:", path_sum(root, 15))
print("Target 100:", path_sum(root, 100))

print("\nNumber of matching paths:")
print("Target 18:", count_path_sums(root, 18))
print("Target 16:", count_path_sums(root, 16))
print("Target 15:", count_path_sums(root, 15))


# Tests
def run_tests():
    assert path_sum(None, 0) == []
    assert path_sum(root, 18) == [
        [10, 5, 2, 1],
        [10, -3, 11]
    ]
    assert path_sum(root, 16) == [
        [10, 5, 3, -2]
    ]
    assert path_sum(root, 15) == []
    assert path_sum(root, 100) == []

    # Two different paths with the same values
    duplicate_tree = TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(2)
    )
    assert path_sum(duplicate_tree, 3) == [
        [1, 2],
        [1, 2]
    ]

    assert count_path_sums(root, 18) == 2
    assert count_path_sums(root, 16) == 1
    assert count_path_sums(root, 15) == 0

    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()
