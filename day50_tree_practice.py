
from collections import deque

from day50_check_complete_binary_tree import Node, is_complete


def completeness_report(root):  
    if root is None:
        return (True, None)

    queue = deque([root])
    seen_gap = False

    while queue:

        node = queue.popleft()

        if node is None:
            seen_gap = True
            continue

        if seen_gap:
            return (False, node.value)

        queue.append(node.left)
        queue.append(node.right)

    return (True, None)


def build_tree_a():
   
    return Node(
        10,
        Node(5, Node(3), Node(7)),
        Node(15, Node(12))
    )


def build_tree_b():

    return Node(
        10,
        Node(5, Node(3), Node(7)),
        Node(15, None, Node(20))
    )


def build_tree_c():
    
    return Node(
        10,
        Node(5, Node(3))
    )


def run_tests():

    print("DAY 50: BINARY TREE PRACTICE")
    

    # Part A: Predict and check the three trees.
    tree_a = build_tree_a()
    tree_b = build_tree_b()
    tree_c = build_tree_c()

    print("\nPart A: Tree completeness")

    print("Tree A:", is_complete(tree_a))
    print("Tree B:", is_complete(tree_b))
    print("Tree C:", is_complete(tree_c))

    assert is_complete(tree_a) is True
    assert is_complete(tree_b) is False
    assert is_complete(tree_c) is False

    # Part B: Edge cases.
    print("\nPart B: Additional test cases")

    assert is_complete(None) is True
    print("Empty tree: True")

    assert is_complete(Node(1)) is True
    print("Single-node tree: True")

    assert is_complete(Node(1, Node(2))) is True
    print("Left-child-only tree: True")

    assert is_complete(Node(1, right=Node(2))) is False
    print("Right-child-only tree: False")

    assert is_complete(
        Node(1, Node(2), Node(3))
    ) is True
    print("Perfect three-node tree: True")

    assert is_complete(
        Node(1, Node(2, Node(3)))
    ) is False
    print("Deeper left-only tree: False")

    # Duplicate values do not affect completeness.
    assert is_complete(
        Node(7, Node(7), Node(7))
    ) is True
    print("Duplicate-value tree: True")

    # Part C: Diagnostic report.
    print("\nPart C: Completeness reports")

    report_a = completeness_report(tree_a)
    report_b = completeness_report(tree_b)
    report_c = completeness_report(tree_c)

    print("Tree A report:", report_a)
    print("Tree B report:", report_b)
    print("Tree C report:", report_c)

    assert report_a == (True, None)
    assert report_b == (False, 20)
    assert report_c == (False, 3)

    print("\nAll Day 50 practice tests passed!")


if __name__ == "__main__":
    run_tests()
