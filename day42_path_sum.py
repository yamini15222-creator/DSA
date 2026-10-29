class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def has_path_sum(root, target):
    if root is None:
        return False

    remaining = target - root.value

    if root.left is None and root.right is None:
        return remaining == 0

    return (
        has_path_sum(root.left, remaining)
        or has_path_sum(root.right, remaining)
    )


# Build the Day 42 assignment tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)

root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)

root.left.left.left = TreeNode(-2)
root.left.right.right = TreeNode(1)


# Assignment tests
assert has_path_sum(root, 16) is True
assert has_path_sum(root, 18) is True
assert has_path_sum(root, 15) is False
assert has_path_sum(root, 7) is False
assert has_path_sum(root, 100) is False

# Empty tree and single-node tests
assert has_path_sum(None, 0) is False
assert has_path_sum(TreeNode(7), 7) is True
assert has_path_sum(TreeNode(7), 0) is False
assert has_path_sum(TreeNode(0), 0) is True

# Negative-value test
negative_path = TreeNode(5, left=TreeNode(-3))
assert has_path_sum(negative_path, 2) is True

# Internal-node match test
internal_match = TreeNode(5, left=TreeNode(2))
assert has_path_sum(internal_match, 5) is False

# Zero-valued child test
zero_path = TreeNode(5, left=TreeNode(0))
assert has_path_sum(zero_path, 5) is True

# Warm-up test: 4 -> -4, target 0
warmup = TreeNode(4, left=TreeNode(-4))
assert has_path_sum(warmup, 0) is True

print("All Day 42 tests passed!")