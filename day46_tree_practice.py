"""
Day 46: Serialize and Deserialize Binary Tree
Practice Examples
"""

from day46_serialize_deserialize_binary_tree import (
    TreeNode,
    deserialize,
    inorder_values,
    preorder_values,
    serialize,
)


def check_tree(label, root):

    print("\n" + label)

    # Serialize the tree
    encoded = serialize(root)

    print("Serialized Tree:", encoded)

    # Deserialize the string
    restored = deserialize(encoded)

    print("Preorder Traversal:", preorder_values(restored))
    print("Inorder Traversal:", inorder_values(restored))

    # Verify the original and restored trees
    assert serialize(restored) == encoded

    print("Verification: Successful")


def run_tests():

    # Test 1: Given Tree Example
    root = TreeNode(
        10,
        TreeNode(
            -2,
            right=TreeNode(4)
        ),
        TreeNode(
            10,
            left=TreeNode(0)
        )
    )

    expected = "10,-2,#,4,#,#,10,0,#,#,#"

    assert serialize(root) == expected

    check_tree("Test 1: Given Tree Example", root)

    # Test 2: Tree with Duplicate Values
    root2 = TreeNode(
        5,
        TreeNode(5),
        TreeNode(5)
    )

    check_tree("Test 2: Duplicate Values", root2)

    # Test 3: Left-Skewed Tree
    root3 = TreeNode(
        4,
        left=TreeNode(
            3,
            left=TreeNode(
                2,
                left=TreeNode(1)
            )
        )
    )

    check_tree("Test 3: Left-Skewed Tree", root3)

    # Test 4: Right-Skewed Tree
    root4 = TreeNode(
        1,
        right=TreeNode(
            2,
            right=TreeNode(3)
        )
    )

    check_tree("Test 4: Right-Skewed Tree", root4)

    # Test 5: Empty Tree
    check_tree("Test 5: Empty Tree", None)

    # Test 6: Single Node
    root6 = TreeNode(100)

    check_tree("Test 6: Single Node", root6)

    # Test 7: Invalid Serialized Data
    invalid_inputs = [
        "",
        "1,#",
        "1,#,#,7",
        "abc,#,#",
        "#,#"
    ]

    print("\nTest 7: Invalid Input Validation")

    for data in invalid_inputs:

        try:
            deserialize(data)

        except ValueError:
            print("Correctly rejected:", repr(data))

        else:
            raise AssertionError(
                f"Invalid input accepted: {data!r}"
            )

    print("\nAll Day 46 practice tests passed!")


if __name__ == "__main__":

    print("DAY 46: BINARY TREE PRACTICE")

    run_tests()