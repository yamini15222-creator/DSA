# Day 41 DSA: Binary Tree Maximum Path Sum

## Problem statement

Find the largest sum of node values along any non-empty path in a binary tree. A path follows parent-child connections in either direction, may start and end at any nodes, and does not need to pass through the root.

## Assignment tree

```text
          10
         /  \
        2    10
       / \     \
      20  1    -25
               / \
              3   4
```

Expected maximum path:

```text
20 -> 2 -> 10 -> 10
Sum = 20 + 2 + 10 + 10 = 42
```

The two `10` values are different nodes, so both can be part of the path.

## Python implementation

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_path_sum(root):
    if root is None:
        raise ValueError("A nonempty tree is required")

    best = root.value

    def gain(node):
        nonlocal best

        if node is None:
            return 0

        left_gain = max(0, gain(node.left))
        right_gain = max(0, gain(node.right))

        # A complete path through this node may use both sides.
        candidate = node.value + left_gain + right_gain
        best = max(best, candidate)

        # A parent may extend through only one side.
        return node.value + max(left_gain, right_gain)

    gain(root)
    return best


if __name__ == "__main__":
    root = TreeNode(
        10,
        TreeNode(2, TreeNode(20), TreeNode(1)),
        TreeNode(10, right=TreeNode(-25, TreeNode(3), TreeNode(4))),
    )

    print("Maximum path sum:", max_path_sum(root))  # 42

    assert max_path_sum(TreeNode(-8)) == -8

    all_negative = TreeNode(-3, TreeNode(-5), TreeNode(-2))
    assert max_path_sum(all_negative) == -2

    print("All tests passed!")
```

Expected output:

```text
Maximum path sum: 42
All tests passed!
```

## Warm-up question

A node has value `5`, its left child returns gain `-3`, and its right child returns gain `8`.

- Clamp the left gain: `max(0, -3) = 0`
- Clamp the right gain: `max(0, 8) = 8`
- Complete candidate: `5 + 0 + 8 = 13`
- Gain returned to the parent: `5 + max(0, 8) = 13`

**Answer:** complete candidate = `13`; returned gain = `13`.

## Dry run

The traversal is postorder: children are processed before their parent. Gains in the table are child gains after negative values have been clamped to zero.

| Node | Left gain | Right gain | Complete candidate | Returned gain | Best so far |
|---:|---:|---:|---:|---:|---:|
| 20 | 0 | 0 | 20 | 20 | 20 |
| 1 | 0 | 0 | 1 | 1 | 20 |
| 2 | 20 | 1 | 23 | 22 | 23 |
| 3 | 0 | 0 | 3 | 3 | 23 |
| 4 | 0 | 0 | 4 | 4 | 23 |
| -25 | 3 | 4 | -18 | -21 | 23 |
| 10 (right child of root) | 0 | 0 | 10 | 10 | 23 |
| 10 (root) | 22 | 10 | **42** | 32 | **42** |

## Why the -25 branch is omitted

The best downward gain from `-25` is `-25 + max(3, 4) = -21`. Since this contribution is negative, its parent uses `max(0, -21) = 0` and does not include that branch in the maximum path.

We cannot skip `-25` and connect directly to `3` or `4`: any path that uses those descendants must include their connecting parent.

## Complete candidate versus returned gain

- **Complete candidate:** `node.value + left_gain + right_gain`. It can use both branches to form a path whose highest node is the current node.
- **Returned gain:** `node.value + max(left_gain, right_gain)`. It returns only one branch because a parent cannot extend a path that splits into two branches.

For node `2`, the complete candidate is `2 + 20 + 1 = 23`, while the returned gain is `2 + max(20, 1) = 22`.

Returning both branches to the parent would create an invalid fork instead of one simple path.

## Required edge cases

```python
assert max_path_sum(TreeNode(-8)) == -8

all_negative = TreeNode(-3, TreeNode(-5), TreeNode(-2))
assert max_path_sum(all_negative) == -2

try:
    max_path_sum(None)
except ValueError:
    pass
else:
    raise AssertionError("Expected ValueError")
```

The answer starts with `root.value`, not zero, so an all-negative tree returns its largest node value rather than an empty path.

## Complexity

- **Time:** `O(n)` because every node is processed once.
- **Auxiliary space:** `O(h)` for the recursive call stack, where `h` is tree height.
- A highly skewed tree may exceed Python's recursion limit. For very deep trees, an iterative postorder traversal is an alternative.

## Extension: return the actual path

To return the path as well as its sum, store parent/branch choices during postorder traversal and reconstruct the best left branch, center node, and right branch afterward. Avoid copying full path lists at every recursive call, because that can increase the time and space cost.

## Corporate-level considerations

Clarify whether empty input is allowed and whether the required output is the sum, endpoints, or full path. This implementation raises `ValueError` for an empty tree and returns only the sum.

## Client-level considerations

This problem permits the path to start and end anywhere. It is not the same as maximum root-to-leaf sum, where the path must start at the root and finish at a leaf. This problem sums node values, not edge costs.
