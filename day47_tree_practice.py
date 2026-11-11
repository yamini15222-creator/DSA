


from day47_flatten_binary_tree import (
    TreeNode,
    flatten,
    preorder_nodes,
    flattened_nodes,
    assert_flattened,
)


def make_main_example():
    return TreeNode(
        10,
        TreeNode(5, TreeNode(3), TreeNode(7, left=TreeNode(6))),
        TreeNode(15, right=TreeNode(20)),
    )


def check_example(label, root, expected_values):
    print("\n" + label)
    expected_nodes = preorder_nodes(root)
    flatten(root)
    assert_flattened(root, expected_nodes)

    actual_values = [node.value for node in flattened_nodes(root)]
    assert actual_values == expected_values

    print("Flattened chain:", " -> ".join(map(str, actual_values)))
    print("All left pointers are None: Yes")
    print("Original node identities preserved: Yes")


def run_practice():
    check_example(
        "Test 1: Main example",
        make_main_example(),
        [10, 5, 3, 7, 6, 15, 20],
    )
    check_example(
        "Test 2: Left-only chain",
        TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1)))),
        [4, 3, 2, 1],
    )
    check_example(
        "Test 3: Already flattened right-only chain",
        TreeNode(1, right=TreeNode(2, right=TreeNode(3))),
        [1, 2, 3],
    )
    check_example(
        "Test 4: Repeated values",
        TreeNode(5, TreeNode(5), TreeNode(5)),
        [5, 5, 5],
    )
    check_example("Test 5: Empty tree", None, [])
    check_example("Test 6: Single node", TreeNode(100), [100])

    print("\nAll Day 47 practice tests passed!")


if __name__ == "__main__":
    print("DAY 47: FLATTEN BINARY TREE PRACTICE")
    run_practice()
