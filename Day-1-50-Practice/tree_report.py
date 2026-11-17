
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def maximum_depth(root):
    if root is None:
        return 0

    return 1 + max(
        maximum_depth(root.left),
        maximum_depth(root.right)
    )


def diameter(root):
    result = 0

    def height(node):
        nonlocal result

        if node is None:
            return 0

        left = height(node.left)
        right = height(node.right)

        result = max(result, left + right)

        return 1 + max(left, right)

    height(root)
    return result


def is_balanced(root):
    def height(node):
        if node is None:
            return 0

        left = height(node.left)
        if left == -1:
            return -1

        right = height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return height(root) != -1


def right_side_view(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result


def maximum_width(root):
    if root is None:
        return 0

    queue = deque([(root, 0)])
    max_width = 0

    while queue:
        level_size = len(queue)
        first = queue[0][1]
        last = 0

        for _ in range(level_size):
            node, index = queue.popleft()
            index -= first
            last = index

            if node.left:
                queue.append((node.left, 2 * index))

            if node.right:
                queue.append((node.right, 2 * index + 1))

        max_width = max(max_width, last + 1)

    return max_width


def is_complete(root):
    if root is None:
        return True

    queue = deque([root])
    seen_gap = False

    while queue:
        node = queue.popleft()

        for child in (node.left, node.right):
            if child:
                if seen_gap:
                    return False
                queue.append(child)
            else:
                seen_gap = True

    return True


# Build the first tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def print_report(root):
    print("Maximum Depth:", maximum_depth(root))
    print("Diameter:", diameter(root))
    print("Height Balanced:", is_balanced(root))
    print("Right Side View:", right_side_view(root))
    print("Maximum Width:", maximum_width(root))
    print("Complete:", is_complete(root))


print("FIRST TREE REPORT")
print_report(root)


# Move node 5 to the right of node 3
root.left.right = None
root.right.right = TreeNode(5)

print("\nSECOND TREE REPORT")
print_report(root)
