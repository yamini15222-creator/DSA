from day48_binary_tree_right_side_view import (
    TreeNode,
    right_side_view,
    right_side_view_dfs,
)


def check_example(label, root, expected):

    print("\n" + label)

    bfs_result = right_side_view(root)

    dfs_result = right_side_view_dfs(root)

    assert bfs_result == expected

    assert dfs_result == expected

    assert bfs_result == dfs_result

    print("BFS right-side view:", bfs_result)

    print("DFS right-side view:", dfs_result)

    print("Both approaches agree: Yes")


def run_practice():

    # Test 1: Main Example
    root1 = TreeNode(
        1,
        TreeNode(2, right=TreeNode(5)),
        TreeNode(3, right=TreeNode(4))
    )

    check_example(
        "Test 1: Main Example",
        root1,
        [1, 3, 4]
    )

    # Test 2: Deeper Left Subtree
    root2 = TreeNode(
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

    check_example(
        "Test 2: Deeper Left Subtree",
        root2,
        [1, 3, 5, 6]
    )

    # Test 3: Day 48 Supplied Tree
    root3 = TreeNode(
        10,
        TreeNode(
            5,
            TreeNode(3),
            TreeNode(7, right=TreeNode(8))
        ),
        TreeNode(15, left=TreeNode(12))
    )

    check_example(
        "Test 3: Day 48 Supplied Tree",
        root3,
        [10, 15, 12, 8]
    )

    # Test 4: Left-Only Chain
    root4 = TreeNode(
        1,
        left=TreeNode(
            2,
            left=TreeNode(3)
        )
    )

    check_example(
        "Test 4: Left-Only Chain",
        root4,
        [1, 2, 3]
    )

    # Test 5: Right-Only Chain
    root5 = TreeNode(
        1,
        right=TreeNode(
            2,
            right=TreeNode(3)
        )
    )

    check_example(
        "Test 5: Right-Only Chain",
        root5,
        [1, 2, 3]
    )

    # Test 6: Rightmost Is Not Maximum
    root6 = TreeNode(
        1,
        TreeNode(100),
        TreeNode(2)
    )

    check_example(
        "Test 6: Rightmost Is Not Maximum",
        root6,
        [1, 2]
    )

    # Test 7: Repeated Values
    root7 = TreeNode(
        5,
        TreeNode(5),
        TreeNode(5)
    )

    check_example(
        "Test 7: Repeated Values",
        root7,
        [5, 5]
    )

    # Test 8: Empty Tree
    check_example(
        "Test 8: Empty Tree",
        None,
        []
    )

    # Test 9: Single Node
    check_example(
        "Test 9: Single Node",
        TreeNode(99),
        [99]
    )

    print("\nAll Day 48 practice tests passed!")


if __name__ == "__main__":

    print("DAY 48: RIGHT SIDE VIEW PRACTICE")

    run_practice()
