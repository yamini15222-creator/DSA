
"""
Day 49: Maximum Width of a Binary Tree
Practice Examples and Dry Run
"""

from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def maximum_width(root):
    if root is None:
        return 0

    queue = deque([(root, 0)])
    best = 0

    while queue:

        level_size = len(queue)
        base = queue[0][1]
        last_position = 0

        for _ in range(level_size):

            node, raw_position = queue.popleft()

            position = raw_position - base
            last_position = position

            if node.left is not None:
                queue.append(
                    (node.left, 2 * position + 1)
                )

            if node.right is not None:
                queue.append(
                    (node.right, 2 * position + 2)
                )

        current_width = last_position + 1
        best = max(best, current_width)

    return best


def build_day49_tree():
    """
    Practice tree:

              10
             /  \
            5    15
           /       \
          3         20
           \\       /
            4     18

    Expected maximum width: 6
    """

    return TreeNode(
        10,
        TreeNode(
            5,
            TreeNode(3, right=TreeNode(4))
        ),
        TreeNode(
            15,
            right=TreeNode(20, TreeNode(18))
        )
    )


def build_main_example():
    """
            1
           / \
          3   2
         / \\   \
        5   3   9

    Expected maximum width: 4
    """

    return TreeNode(
        1,
        TreeNode(3, TreeNode(5), TreeNode(3)),
        TreeNode(2, right=TreeNode(9))
    )


def print_level_positions(root):
    """
    Display raw positions, normalized positions,
    and width for every level.
    """

    if root is None:
        print("Tree is empty.")
        return

    queue = deque([(root, 0)])
    level_number = 1

    while queue:

        level_size = len(queue)
        base = queue[0][1]

        raw_positions = []
        normalized_positions = []

        for _ in range(level_size):

            node, raw_position = queue.popleft()

            position = raw_position - base

            raw_positions.append(raw_position)
            normalized_positions.append(position)

            if node.left is not None:
                queue.append(
                    (node.left, 2 * position + 1)
                )

            if node.right is not None:
                queue.append(
                    (node.right, 2 * position + 2)
                )

        width = normalized_positions[-1] + 1

        print(f"\nLevel {level_number}")
        print("Raw positions:", raw_positions)
        print("Base:", base)
        print("Normalized positions:", normalized_positions)
        print("Width:", width)

        level_number += 1


def run_practice_tests():

    # Test 1: Empty tree
    assert maximum_width(None) == 0

    # Test 2: Single node
    assert maximum_width(TreeNode(7)) == 1

    # Test 3: Main example
    assert maximum_width(build_main_example()) == 4

    # Test 4: Day 49 practice tree
    assert maximum_width(build_day49_tree()) == 6

    # Test 5: Left-only chain
    left_chain = TreeNode(
        1,
        TreeNode(2, TreeNode(3))
    )
    assert maximum_width(left_chain) == 1

    # Test 6: Right-only chain
    right_chain = TreeNode(
        1,
        right=TreeNode(2, right=TreeNode(3))
    )
    assert maximum_width(right_chain) == 1

    # Test 7: Sparse tree
    sparse = TreeNode(
        1,
        TreeNode(2, left=TreeNode(4)),
        TreeNode(3, right=TreeNode(5))
    )
    assert maximum_width(sparse) == 4

    # Test 8: Duplicate values
    duplicates = TreeNode(
        5,
        TreeNode(5, left=TreeNode(5)),
        TreeNode(5, right=TreeNode(5))
    )
    assert maximum_width(duplicates) == 4

    print("\nAll Day 49 practice tests passed!")


if __name__ == "__main__":

    print("DAY 49: MAXIMUM WIDTH PRACTICE")
    print("=" * 40)

    # Example 1
    print("\nTest 1: Main example")

    main_tree = build_main_example()

    print("Expected width: 4")
    print("Actual width:", maximum_width(main_tree))

    # Example 2
    print("\nTest 2: Day 49 practice tree")

    practice_tree = build_day49_tree()

    print("Expected width: 6")
    print("Actual width:", maximum_width(practice_tree))

    # Dry run
    print("\nTest 3: Position index dry run")

    print_level_positions(practice_tree)

    # Additional tests
    print("\nTest 4: Empty tree")
    print("Width:", maximum_width(None))

    print("\nTest 5: Single node")
    print("Width:", maximum_width(TreeNode(99)))

    print("\nTest 6: Right-only chain")
    right_chain = TreeNode(
        1,
        right=TreeNode(2, right=TreeNode(3))
    )
    print("Width:", maximum_width(right_chain))

    # Run all assertions
    run_practice_tests()
