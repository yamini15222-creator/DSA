# Day 42 DSA: Root-to-Leaf Path Sum

## 1. Problem Statement

Given the root of a binary tree and a target sum, determine whether any path from the root to a leaf adds up exactly to the target.

A **leaf** is a node that has no left child and no right child.

The function returns `True` if at least one valid root-to-leaf path matches the target. Otherwise, it returns `False`.

Assumptions:
- The tree is a valid binary tree.
- Node values are integers.
- Negative values and duplicate values are allowed.
- An empty tree returns `False`, even when the target is zero.

## 2. Original Lesson Example

```text
           5
          / \
         4   8
        /   / \
       11  13  4
      / \      \
     7   2      1
```

For target `22`, the answer is `True`.

Matching path: `5 → 4 → 11 → 2`

Sum: `5 + 4 + 11 + 2 = 22`

For target `9`, the answer is `False`. Although `5 + 4 = 9`, node `4` is not a leaf, so the path cannot stop there.

| Target | Result | Explanation |
|---:|:---|---|
| 22 | `True` | Path: 5 → 4 → 11 → 2 |
| 26 | `True` | Path: 5 → 8 → 13 |
| 9 | `False` | The matching prefix ends at an internal node |
| 18 | `True` | Path: 5 → 8 → 4 → 1 |

## 3. Implementation Code

Save the Python implementation separately as `day42_path_sum.py`.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def has_path_sum(root, target):
    if root is None:
        return False

    remaining = target - root.value

    # A path is complete only when the current node is a leaf.
    if root.left is None and root.right is None:
        return remaining == 0

    return (
        has_path_sum(root.left, remaining)
        or has_path_sum(root.right, remaining)
    )


# Build the original lesson tree.
root = TreeNode(
    5,
    TreeNode(
        4,
        left=TreeNode(11, TreeNode(7), TreeNode(2))
    ),
    TreeNode(
        8,
        TreeNode(13),
        TreeNode(4, right=TreeNode(1))
    )
)

# Original lesson tests.
assert has_path_sum(root, 22) is True
assert has_path_sum(root, 26) is True
assert has_path_sum(root, 9) is False
assert has_path_sum(root, 18) is True

print("All original lesson tests passed!")
```

## 4. How the Recursive Algorithm Works

The algorithm carries the remaining target down the tree.

1. If the node is `None`, return `False`.
2. Subtract the current node's value from the target.
3. If the current node is a leaf, return `True` only when the remaining target is zero.
4. Otherwise, recursively check the left and right subtrees.
5. Return `True` if either subtree contains a matching path.

The recursive calls use `or` because only one matching path is required.

A leaf must have both children missing. A node with only one missing child is not a leaf.

## 5. Dry Run for Target 22

The algorithm explores the left subtree first.

| Node | Target received | Remaining after subtraction | Decision |
|---:|---:|---:|---|
| 5 | 22 | 17 | Continue |
| 4 | 17 | 13 | Continue |
| 11 | 13 | 2 | Continue |
| 7 | 2 | -5 | Leaf: return `False` |
| 2 | 2 | 0 | Leaf: return `True` |

The successful result travels back through nodes `11`, `4`, and `5`.

Each recursive call maintains its own remaining target. Exploring one branch does not modify the state of its sibling.

## 6. Negative Values and Zero Remaining

Negative values are allowed. Therefore, a negative remaining target does not automatically mean that a matching path is impossible.

Consider:

```text
    5
   /
 -3
```

For target `2`, the path `5 → -3` sums to `2`, so the result is `True`.

Do not reject a path simply because its remaining target is negative.

Zero remaining is not sufficient by itself. Success is confirmed only at a leaf after subtracting that leaf's value.

For example:

```text
    5
   /
   0
```

For target `5`, the result is `True` because the complete path `5 → 0` ends at a leaf and sums to `5`.

## 7. Tests to Run

Run these tests after defining `TreeNode`, `has_path_sum`, and the original lesson tree named `root`.

```python
assert has_path_sum(None, 0) is False

assert has_path_sum(TreeNode(7), 7) is True
assert has_path_sum(TreeNode(7), 0) is False

assert has_path_sum(root, 22) is True
assert has_path_sum(root, 26) is True
assert has_path_sum(root, 9) is False

# Negative remainder can still lead to success.
negative_path = TreeNode(5, left=TreeNode(-3))
assert has_path_sum(negative_path, 2) is True

# Matching an internal node is insufficient.
internal_match = TreeNode(5, left=TreeNode(2))
assert has_path_sum(internal_match, 5) is False

# Zero-valued nodes are allowed.
zero_path = TreeNode(5, left=TreeNode(0))
assert has_path_sum(zero_path, 5) is True

# A single zero node is a valid nonempty path.
assert has_path_sum(TreeNode(0), 0) is True
```

## 8. Assignment: Find a Matching Route

Build the following binary tree:

```text
           10
          /  \
         5   -3
        / \    \
       3   2    11
      /     \
    -2       1
```

Its root-to-leaf paths are:

```text
10 → 5 → 3 → -2 = 16
10 → 5 → 2 → 1  = 18
10 → -3 → 11    = 18
```

Implement `has_path_sum()` independently using the same function contract.

### Expected Results

| Target | Result |
|---:|:---|
| 16 | `True` |
| 18 | `True` |
| 15 | `False` |
| 7 | `False` |
| 100 | `False` |

Targets `15` and `7` do not have a complete root-to-leaf path with that sum.

### Assignment Tree Construction and Tests

```python
assignment_root = TreeNode(10)
assignment_root.left = TreeNode(5)
assignment_root.right = TreeNode(-3)

assignment_root.left.left = TreeNode(3)
assignment_root.left.right = TreeNode(2)
assignment_root.right.right = TreeNode(11)

assignment_root.left.left.left = TreeNode(-2)
assignment_root.left.right.right = TreeNode(1)

assert has_path_sum(assignment_root, 16) is True
assert has_path_sum(assignment_root, 18) is True
assert has_path_sum(assignment_root, 15) is False
assert has_path_sum(assignment_root, 7) is False
assert has_path_sum(assignment_root, 100) is False
```

## 9. Trace for Target 16

The matching path is `10 → 5 → 3 → -2`.

| Node | Remaining target calculation | Remaining |
|---:|---|---:|
| 10 | 16 − 10 | 6 |
| 5 | 6 − 5 | 1 |
| 3 | 1 − 3 | -2 |
| -2 | -2 − (-2) | 0 |

The remaining target becomes zero at leaf `-2`. Therefore, the result is `True`.

## 10. Why Target 7 Returns False

A valid path must begin at the root and finish at a leaf.

In the assignment tree, the path `10 → -3` sums to `7`, but node `-3` is not a leaf because it has a right child, `11`.

The complete path `10 → -3 → 11` sums to `18`, not `7`.

Therefore, `has_path_sum(assignment_root, 7)` returns `False`.

## 11. Warm-Up Question

Consider this tree:

```text
    4
   /
 -4
```

For target `0`, the result is `True`.

Success is confirmed at leaf `-4`, because `4 + (-4) = 0`.

## 12. Function Contract

**Input:** A binary-tree root and an integer target sum.

**Output:** A boolean indicating whether a root-to-leaf path equals the target.

- An empty tree returns `False`, even when the target is zero.
- Negative values and duplicate values are supported.
- A matching sum at an internal node does not count.
- A single-node tree is valid when its value equals the target.
- The function does not modify the tree.

## 13. Iterative DFS Extension

Recursive DFS is concise, but a very deep tree may exceed Python's recursion limit. An iterative implementation uses a stack instead.

The stack stores pairs:

`(node, remaining_target)`

The `remaining_target` represents the amount needed **before processing that node**.

For each popped pair:

1. Subtract the node's value from the remaining target.
2. If the node is a leaf, check whether the new remainder is zero.
3. Otherwise, push its existing children with the updated remainder.
4. Return `False` if the stack becomes empty without finding a matching path.

```python
def has_path_sum_iterative(root, target):
    if root is None:
        return False

    stack = [(root, target)]

    while stack:
        node, remaining_target = stack.pop()
        remaining = remaining_target - node.value

        if node.left is None and node.right is None:
            if remaining == 0:
                return True
            continue

        if node.right is not None:
            stack.append((node.right, remaining))

        if node.left is not None:
            stack.append((node.left, remaining))

    return False
```

### Iterative DFS Tests

Run these tests after defining the iterative function and both trees.

```python
assert has_path_sum_iterative(root, 22) is True
assert has_path_sum_iterative(root, 26) is True
assert has_path_sum_iterative(root, 9) is False

assert has_path_sum_iterative(assignment_root, 16) is True
assert has_path_sum_iterative(assignment_root, 18) is True
assert has_path_sum_iterative(assignment_root, 15) is False
assert has_path_sum_iterative(assignment_root, 7) is False
assert has_path_sum_iterative(assignment_root, 100) is False
assert has_path_sum_iterative(None, 0) is False

print("All recursive and iterative tests passed!")
```

## 14. Institute-Level Discussion

The function contract defines the input, output, and valid path rules.

The leaf check is necessary because the path must end at a leaf. Reaching the target at an internal node is not enough.

**Day 41 — Maximum Path Sum:** A path may start and end anywhere in the tree. The objective is to find the largest possible sum.

**Day 42 — Root-to-Leaf Path Sum:** A path must start at the root and end at a leaf. The objective is to check whether its sum exactly matches the target.

Day 41 returns a maximum sum, whereas Day 42 returns a boolean.

Do not use Day 41's `max(0, gain)` rule in this problem. Negative values may be necessary to complete the target sum.

## 15. Corporate-Level Discussion

Recursive DFS is concise and suitable for trees of ordinary depth. Iterative DFS is useful when a tree may be extremely deep because it avoids Python's recursive call-stack limit.

Keep each path's remaining target separate so that processing one branch does not affect another.

Clarify the required output before designing the algorithm:

- **Boolean:** Whether any matching path exists.
- **One path:** Return one matching route.
- **All paths:** Return every matching route.
- **Count:** Return the number of matching routes.

These requirements need different output handling.

## 16. Client-Level Discussion

Define what counts as a completed route.

In this problem, completion means reaching a structural leaf. In another application, a designated terminal state may not be the same as a structural leaf.

For monetary values, use an exact representation such as integer minor units, for example paise, instead of relying on approximate floating-point equality.

## 17. Complexity Analysis

Let `n` be the number of nodes and `h` be the height of the tree.

- **Worst-case time:** `O(n)`, because every node may need to be visited.
- **Recursive auxiliary space:** `O(h)` for the call stack.
- **Iterative auxiliary space:** Up to `O(n)` in the worst case.
- A successful path may allow the algorithm to stop early.

## 18. Common Mistakes

| Mistake | Why it fails |
|---|---|
| Return `True` whenever the remainder reaches zero | The current node may not be a leaf |
| Treat one missing child as a leaf | Both children must be missing |
| Return `target == 0` for a missing node | A missing child is not a valid path endpoint |
| Use `and` between child results | Only one matching path is required |
| Reject every negative remainder | Negative node values can restore the target |
| Use Day 41's maximum-path logic | Day 42 requires a root-to-leaf path |