
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    n = len(preorder)

    # Validate input lengths
    if n != len(inorder):
        raise ValueError("Traversals must have equal lengths")

    # Empty tree
    if n == 0:
        return None

    # Validate unique values
    if len(set(preorder)) != n or len(set(inorder)) != n:
        raise ValueError("Values must be unique")

    # Validate matching values
    if set(preorder) != set(inorder):
        raise ValueError("Traversals must contain the same values")

    # Store each value's inorder index
    positions = {
        value: index
        for index, value in enumerate(inorder)
    }

    pre_index = 0

    def build(left, right):
        nonlocal pre_index

        # No nodes in this inorder section
        if left > right:
            return None

        if pre_index >= n:
            raise ValueError("Inconsistent traversal order")

        # Get the next root from preorder
        value = preorder[pre_index]

        # Find its position in inorder
        middle = positions[value]

        # Check whether root belongs to this section
        if not left <= middle <= right:
            raise ValueError("Inconsistent traversal order")

        # Consume this preorder value
        pre_index += 1

        node = TreeNode(value)

        # Build left subtree first
        node.left = build(left, middle - 1)

        # Build right subtree next
        node.right = build(middle + 1, right)

        return node

    root = build(0, n - 1)

    if pre_index != n:
        raise ValueError("Not all preorder values were consumed")

    return root


# Preorder traversal: Root -> Left -> Right
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


# Inorder traversal: Left -> Root -> Right
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


def print_tree_details(root):
    if root is None:
        print("Tree is empty")
        return

    print("Root:", root.value)
    print("Left child:", root.left.value if root.left else None)
    print("Right child:", root.right.value if root.right else None)


def run_tests():
    print("\n--- DAY 45 IMPLEMENTATION TESTS ---")

    # Test 1: Main example
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = build_tree(preorder, inorder)

    assert root.value == 3
    assert root.left.value == 9
    assert root.right.value == 20
    assert root.right.left.value == 15
    assert root.right.right.value == 7

    assert preorder_values(root) == preorder
    assert inorder_values(root) == inorder

    print("Test 1: Main example - PASSED")
    print_tree_details(root)

    # Test 2: Empty tree
    assert build_tree([], []) is None
    print("Test 2: Empty tree - PASSED")

    # Test 3: Single node
    single = build_tree([7], [7])

    assert single.value == 7
    assert single.left is None
    assert single.right is None

    print("Test 3: Single node - PASSED")

    # Test 4: Left-skewed chain
    chain = build_tree([1, 2, 3], [3, 2, 1])

    assert chain.value == 1
    assert chain.left.value == 2
    assert chain.left.left.value == 3

    print("Test 4: Left-skewed chain - PASSED")

    # Test 5: Inconsistent traversal
    try:
        build_tree([1, 2, 3], [3, 1, 2])
    except ValueError:
        print("Test 5: Inconsistent traversal - PASSED")
    else:
        raise AssertionError("Expected ValueError")

    # Test 6: Different values
    try:
        build_tree([1, 2], [1, 3])
    except ValueError:
        print("Test 6: Different values - PASSED")
    else:
        raise AssertionError("Expected ValueError")

    # Test 7: Duplicate values
    try:
        build_tree([1, 1], [1, 1])
    except ValueError:
        print("Test 7: Duplicate values - PASSED")
    else:
        raise AssertionError("Expected ValueError")

    # Test 8: Unequal lengths
    try:
        build_tree([1, 2], [1])
    except ValueError:
        print("Test 8: Unequal lengths - PASSED")
    else:
        raise AssertionError("Expected ValueError")

    print("\nAll implementation tests passed!")


if __name__ == "__main__":
    print("DAY 45: CONSTRUCT BINARY TREE")

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = build_tree(preorder, inorder)

    print("\nOriginal Preorder:", preorder)
    print("Original Inorder:", inorder)

    print("\nConstructed Tree Details:")
    print_tree_details(root)

    print("\nGenerated Preorder:", preorder_values(root))
    print("Generated Inorder:", inorder_values(root))

    print("\n--- ROUND-TRIP VERIFICATION ---")
    assert preorder_values(root) == preorder
    assert inorder_values(root) == inorder
    print("Both traversals verified successfully!")

    run_tests()
