"""
Day 46: Serialize and Deserialize a Binary Tree

Serialization:
    Binary Tree -> String

Deserialization:
    String -> Binary Tree

Traversal:
    Preorder (Root -> Left -> Right)

Missing child:
    #
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Serialize Binary Tree into String
def serialize(root):
    tokens = []

    def preorder(node):
        if node is None:
            tokens.append("#")
            return

        tokens.append(str(node.value))

        preorder(node.left)
        preorder(node.right)

    preorder(root)

    return ",".join(tokens)


# Deserialize String into Binary Tree
def deserialize(data):

    if not isinstance(data, str):
        raise TypeError("Tree data must be a string")

    if data == "":
        raise ValueError("Use '#' for an empty tree")

    tokens = data.split(",")
    index = 0

    def build_tree():
        nonlocal index

        if index >= len(tokens):
            raise ValueError("Incomplete tree data")

        token = tokens[index]
        index += 1

        if token == "#":
            return None

        try:
            value = int(token)
        except ValueError as exc:
            raise ValueError(
                f"Invalid integer token: {token!r}"
            ) from exc

        node = TreeNode(value)

        node.left = build_tree()
        node.right = build_tree()

        return node

    root = build_tree()

    if index != len(tokens):
        raise ValueError("Extra tokens after the tree")

    return root


# Preorder Traversal
def preorder_values(root):
    result = []

    def visit(node):
        if node is None:
            return

        result.append(node.value)
        visit(node.left)
        visit(node.right)

    visit(root)

    return result


# Inorder Traversal
def inorder_values(root):
    result = []

    def visit(node):
        if node is None:
            return

        visit(node.left)
        result.append(node.value)
        visit(node.right)

    visit(root)

    return result


# Test Cases
def run_tests():

    # Test 1: Main Example
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            TreeNode(5)
        )
    )

    expected = "1,2,#,#,3,4,#,#,5,#,#"

    encoded = serialize(root)

    assert encoded == expected

    restored = deserialize(encoded)

    assert serialize(restored) == expected
    assert restored is not root

    # Test 2: Empty Tree
    assert serialize(None) == "#"
    assert deserialize("#") is None

    # Test 3: Single Node
    single = TreeNode(0)

    assert serialize(single) == "0,#,#"

    # Test 4: Left-Skewed Tree
    left = TreeNode(
        1,
        left=TreeNode(2)
    )

    assert serialize(left) == "1,2,#,#,#"

    # Test 5: Right-Skewed Tree
    right = TreeNode(
        1,
        right=TreeNode(2)
    )

    assert serialize(right) == "1,#,2,#,#"

    # Test 6: Negative and Duplicate Values
    duplicate = TreeNode(
        -1,
        TreeNode(-1),
        TreeNode(0)
    )

    encoded = serialize(duplicate)

    assert serialize(deserialize(encoded)) == encoded

    # Test 7: Invalid Inputs
    invalid_inputs = [
        "",
        "1,#",
        "1,#,#,9",
        "x,#,#",
        "#,#",
        "1,,#,#,#"
    ]

    for invalid in invalid_inputs:
        try:
            deserialize(invalid)

        except ValueError:
            pass

        else:
            raise AssertionError(
                f"Expected ValueError for {invalid!r}"
            )

    print("All Day 46 tests passed!")


# Main Program
if __name__ == "__main__":

    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            TreeNode(5)
        )
    )

    encoded = serialize(root)

    restored = deserialize(encoded)

    print("DAY 46: SERIALIZE AND DESERIALIZE A BINARY TREE")

    print("Serialized:", encoded)

    print("Restored preorder:", preorder_values(restored))

    print("Restored inorder:", inorder_values(restored))

    print("Same object:", restored is root)

    print()

    run_tests()