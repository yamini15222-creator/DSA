
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_path_sum(root):
    if root is None:
        raise ValueError("A nonempty tree is required")

    best = root.value

    def gain(node):
        nonlocal best

        if node is None:
            return 0

        left_gain = max(0, gain(node.left))
        right_gain = max(0, gain(node.right))

        candidate = node.value + left_gain + right_gain
        best = max(best, candidate)

        return node.value + max(left_gain, right_gain)

    gain(root)
    return best


if __name__ == "__main__":
    root = TreeNode(
        -10,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )

    print("Maximum path sum:", max_path_sum(root))

    all_negative = TreeNode(-3, TreeNode(-5), TreeNode(-2))
    print("All-negative tree:", max_path_sum(all_negative))

    print("Single node:", max_path_sum(TreeNode(-8)))
