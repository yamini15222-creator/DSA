"""
Day 47: Flatten a Binary Tree to a Linked List
Preorder order: Root -> Left -> Right.
The original nodes are rewired in place; no replacement nodes are created.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flatten(root, attachment_log=None):
    """Flatten in place using O(1) auxiliary space. Returns None."""
    current = root

    while current is not None:
        if current.left is not None:
            tail = current.left

            # Find the rightmost node along the left subtree's right chain.
            while tail.right is not None:
                tail = tail.right

            # Preserve the original right subtree before overwriting current.right.
            original_right = current.right

            if attachment_log is not None:
                attachment_log.append((
                    current.value,
                    tail.value,
                    original_right.value if original_right is not None else None,
                ))

            tail.right = original_right
            current.right = current.left
            current.left = None

        current = current.right


def preorder_nodes(root):
    """Return original node objects in preorder (used by tests)."""
    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node)

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return result


def flattened_nodes(root):
    """Read the flattened chain and ensure each node has no left child."""
    result = []
    current = root

    while current is not None:
        if current.left is not None:
            raise AssertionError(f"Node {current.value} still has a left child")
        result.append(current)
        current = current.right

    return result


def assert_flattened(root, expected_nodes):
    actual = flattened_nodes(root)
    assert len(actual) == len(expected_nodes)
    assert all(a is e for a, e in zip(actual, expected_nodes))
    assert len({id(node) for node in actual}) == len(actual)


def build_day47_example():
    return TreeNode(
        10,
        TreeNode(
            5,
            TreeNode(3),
            TreeNode(7, left=TreeNode(6)),
        ),
        TreeNode(15, right=TreeNode(20)),
    )

