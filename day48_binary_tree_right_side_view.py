
"""
Day 48: Binary Tree Right Side View

Return the rightmost node value at every depth.

Includes:
1. BFS using a queue
2. DFS using right-first recursion
"""

from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# BFS Approach
def right_side_view(root):

    if root is None:
        return []

    view = []
    queue = deque([root])

    while queue:

        level_size = len(queue)

        for index in range(level_size):

            node = queue.popleft()

            # Save the last node at each level.
            if index == level_size - 1:
                view.append(node.value)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    return view


# DFS Approach
def right_side_view_dfs(root):

    view = []

    def visit(node, depth):

        if node is None:
            return

        # First node visited at this depth is rightmost.
        if depth == len(view):
            view.append(node.value)

        # Visit right subtree first.
        visit(node.right, depth + 1)

        # Then visit left subtree.
        visit(node.left, depth + 1)

    visit(root, 0)

    return view


# Build Example Tree
def build_example_tree():

    root = TreeNode(
        1,
        TreeNode(2, right=TreeNode(5)),
        TreeNode(3, right=TreeNode(4))
    )

    return root


# Test Cases
def run_tests():

    # Test 1: Empty Tree
    assert right_side_view(None) == []
    assert right_side_view_dfs(None) == []

    # Test 2: Single Node
    single = TreeNode(7)

    assert right_side_view(single) == [7]
    assert right_side_view_dfs(single) == [7]

    # Test 3: Normal Binary Tree
    root = build_example_tree()

    assert right_side_view(root) == [1, 3, 4]
    assert right_side_view_dfs(root) == [1, 3, 4]

    # Test 4: Deeper Left Subtree
    left_extension = TreeNode(
        1,
        TreeNode(
            2,
            right=TreeNode(
                5,
                right=TreeNode(6)
            )
        ),
        TreeNode(3)
    )

    assert right_side_view(left_extension) == [1, 3, 5, 6]
    assert right_side_view_dfs(left_extension) == [1, 3, 5, 6]

    # Test 5: Left-Only Chain
    left_chain = TreeNode(
        1,
        left=TreeNode(
            2,
            left=TreeNode(3)
        )
    )

    assert right_side_view(left_chain) == [1, 2, 3]
    assert right_side_view_dfs(left_chain) == [1, 2, 3]

    # Test 6: Rightmost Is Not Maximum
    different_values = TreeNode(
        1,
        TreeNode(100),
        TreeNode(2)
    )

    assert right_side_view(different_values) == [1, 2]
    assert right_side_view_dfs(different_values) == [1, 2]

    # Test 7: Duplicate Values
    duplicates = TreeNode(
        5,
        TreeNode(5),
        TreeNode(5)
    )

    assert right_side_view(duplicates) == [5, 5]
    assert right_side_view_dfs(duplicates) == [5, 5]

    print("All Day 48 tests passed!")


# Main Program
if __name__ == "__main__":

    root = build_example_tree()

    print("DAY 48: BINARY TREE RIGHT SIDE VIEW")

    print("BFS result:", right_side_view(root))
    print("DFS result:", right_side_view_dfs(root))

    print()

    run_tests()
