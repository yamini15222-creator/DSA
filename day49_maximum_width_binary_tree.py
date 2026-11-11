
"""
Day 49: Maximum Width of a Binary Tree

Find the maximum positional width of a binary tree using BFS.

Important:
- Width includes missing positions between existing nodes.
- Each node is stored with its position index.
- Positions are normalized at every level.
"""

from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def maximum_width(root):
    """
    Calculate the maximum positional width of a binary tree.

    Args:
        root: Root node of the binary tree.

    Returns:
        Maximum positional width as an integer.
    """

    if root is None:
        return 0

    # Store each node with its position index.
    queue = deque([(root, 0)])

    # Store the maximum width.
    best = 0

    while queue:

        # Number of existing nodes in the current level.
        level_size = len(queue)

        # First position of the current level.
        base = queue[0][1]

        last_position = 0

        for _ in range(level_size):

            node, raw_position = queue.popleft()

            # Normalize the position.
            position = raw_position - base

            # Update the last position.
            last_position = position

            # Add left child.
            if node.left is not None:
                left_position = 2 * position + 1
                queue.append((node.left, left_position))

            # Add right child.
            if node.right is not None:
                right_position = 2 * position + 2
                queue.append((node.right, right_position))

        # First normalized position is always zero.
        current_width = last_position + 1

        best = max(best, current_width)

    return best


def build_example_tree():
    """
    Build the main Day 49 example tree.

            1
           / \
          3   2
         / \\   \
        5   3   9
    """

    return TreeNode(
        1,
        TreeNode(3, TreeNode(5), TreeNode(3)),
        TreeNode(2, right=TreeNode(9))
    )


def run_tests():

    # Test 1: Empty tree
    assert maximum_width(None) == 0

    # Test 2: Single node
    assert maximum_width(TreeNode(7)) == 1

    # Test 3: Main example
    root = build_example_tree()
    assert maximum_width(root) == 4

    # Test 4: Right-only chain
    chain = TreeNode(
        1,
        right=TreeNode(
            2,
            right=TreeNode(3)
        )
    )
    assert maximum_width(chain) == 1

    # Test 5: Sparse tree
    sparse = TreeNode(
        1,
        TreeNode(2, left=TreeNode(4)),
        TreeNode(3, right=TreeNode(5))
    )
    assert maximum_width(sparse) == 4

    # Test 6: Duplicate values
    duplicates = TreeNode(
        5,
        TreeNode(5, left=TreeNode(5)),
        TreeNode(5, right=TreeNode(5))
    )
    assert maximum_width(duplicates) == 4

    print("All Day 49 main tests passed!")


if __name__ == "__main__":

    root = build_example_tree()

    print("DAY 49: MAXIMUM WIDTH OF A BINARY TREE")
    print("--------------------------------------")

    result = maximum_width(root)

    print("Maximum width:", result)

    run_tests()
