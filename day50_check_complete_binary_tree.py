
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_complete(root):
    if root is None:
        return True

    queue = deque([root])
    seen_gap = False

    while queue:

        node = queue.popleft()

        # An empty position has been found.
        if node is None:
            seen_gap = True
            continue

        # A real node after an empty position
        # means the tree is not complete.
        if seen_gap:
            return False

        # Add both children, including None.
        queue.append(node.left)
        queue.append(node.right)

    return True


def build_complete_tree():
    
    root = Node(
        1,
        Node(2, Node(4), Node(5)),
        Node(3, Node(6))
    )

    return root


def build_incomplete_tree():
   

    root = Node(
        1,
        Node(2, Node(4)),
        Node(3, Node(6), Node(7))
    )

    return root


if __name__ == "__main__":

    print("DAY 50: CHECK WHETHER A BINARY TREE IS COMPLETE")


    complete_tree = build_complete_tree()
    incomplete_tree = build_incomplete_tree()

    print(
        "Complete tree:",
        is_complete(complete_tree)
    )

    print(
        "Incomplete tree:",
        is_complete(incomplete_tree)
    )

    # Basic test cases
    assert is_complete(None) is True
    assert is_complete(Node(1)) is True

    assert is_complete(complete_tree) is True
    assert is_complete(incomplete_tree) is False

    # Left child only is allowed.
    assert is_complete(Node(1, Node(2))) is True

    # Right child only is not allowed.
    assert is_complete(Node(1, right=Node(2))) is False

    print("\nAll Day 50 main tests passed!")
