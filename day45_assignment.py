class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    n = len(preorder)

    if n != len(inorder):
        raise ValueError("Traversal lengths must match")

    if n == 0:
        return None

    if len(set(preorder)) != n or len(set(inorder)) != n:
        raise ValueError("Duplicate values are not allowed")

    if set(preorder) != set(inorder):
        raise ValueError("Traversal values must match")

    positions = {
        value: index
        for index, value in enumerate(inorder)
    }

    pre_index = 0

    def build(left, right):
        nonlocal pre_index

        if left > right:
            return None

        if pre_index >= n:
            raise ValueError("Inconsistent traversal order")

        value = preorder[pre_index]
        middle = positions[value]

        if middle < left or middle > right:
            raise ValueError("Inconsistent traversal order")

        pre_index += 1

        node = TreeNode(value)

        node.left = build(left, middle - 1)
        node.right = build(middle + 1, right)

        return node

    root = build(0, n - 1)

    if pre_index != n:
        raise ValueError("Not all preorder values were consumed")

    return root


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


def print_tree(root, level=0, label="Root"):
    if root is None:
        return

    print(" " * (level * 4) + label + ": " + str(root.value))

    print_tree(root.left, level + 1, "Left")
    print_tree(root.right, level + 1, "Right")


def run_tests():
    print("DAY 45: TREE CONSTRUCTION PRACTICE")
    print("=" * 45)

    # Example 1: Balanced binary tree
    preorder1 = [10, 5, 3, 7, 15, 12, 18]
    inorder1 = [3, 5, 7, 10, 12, 15, 18]

    root1 = build_tree(preorder1, inorder1)

    print("\nExample 1: Balanced Binary Tree")
    print_tree(root1)

    assert preorder_values(root1) == preorder1
    assert inorder_values(root1) == inorder1

    print("Example 1: PASSED")

    # Example 2: Ordinary binary tree, not a BST
    preorder2 = [1, 9, 2]
    inorder2 = [9, 1, 2]

    root2 = build_tree(preorder2, inorder2)

    print("\nExample 2: Non-BST Binary Tree")
    print_tree(root2)

    assert root2.value == 1
    assert root2.left.value == 9
    assert root2.right.value == 2

    assert preorder_values(root2) == preorder2
    assert inorder_values(root2) == inorder2

    print("Example 2: PASSED")

    # Example 3: Left-skewed tree
    preorder3 = [4, 3, 2, 1]
    inorder3 = [1, 2, 3, 4]

    root3 = build_tree(preorder3, inorder3)

    print("\nExample 3: Left-Skewed Tree")
    print_tree(root3)

    assert preorder_values(root3) == preorder3
    assert inorder_values(root3) == inorder3

    print("Example 3: PASSED")

    # Example 4: Right-skewed tree
    preorder4 = [1, 2, 3, 4]
    inorder4 = [1, 2, 3, 4]

    root4 = build_tree(preorder4, inorder4)

    print("\nExample 4: Right-Skewed Tree")
    print_tree(root4)

    assert preorder_values(root4) == preorder4
    assert inorder_values(root4) == inorder4

    print("Example 4: PASSED")

    # Example 5: Single-node tree
    root5 = build_tree([7], [7])

    assert root5.value == 7
    assert root5.left is None
    assert root5.right is None

    print("\nSingle-Node Test: PASSED")

    # Example 6: Empty tree
    assert build_tree([], []) is None

    print("Empty-Tree Test: PASSED")

    # Example 7: Invalid traversal order
    try:
        build_tree([1, 2, 3], [3, 1, 2])
    except ValueError:
        print("Invalid Traversal Test: PASSED")
    else:
        raise AssertionError("Expected ValueError")

    # Example 8: Different values
    try:
        build_tree([1, 2], [1, 3])
    except ValueError:
        print("Different Values Test: PASSED")
    else:
        raise AssertionError("Expected ValueError")

    # Example 9: Duplicate values
    try:
        build_tree([1, 1], [1, 1])
    except ValueError:
        print("Duplicate Values Test: PASSED")
    else:
        raise AssertionError("Expected ValueError")

    # Example 10: Unequal lengths
    try:
        build_tree([1, 2], [1])
    except ValueError:
        print("Unequal Lengths Test: PASSED")
    else:
        raise AssertionError("Expected ValueError")

    print("\n" + "=" * 45)
    print("ALL TESTS PASSED!")


if __name__ == "__main__":
    run_tests()