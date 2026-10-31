# Day 44 – Path Sum III: Count Downward Paths Using Prefix Sums

## 1. Introduction

Day 44 focuses on **Path Sum III**.

The objective is to count all downward paths in a binary tree whose sum equals a given target.

A path:
- Can start at any node.
- Can end at any node.
- Must move downward from parent to child.
- Does not need to reach a leaf node.

We use **Prefix Sum + Hash Map + DFS + Backtracking** to solve this efficiently.

## 2. Example Tree

```text
          10
         /  \
        5   -3
       / \    \
      3   2    11
     / \   \
    3  -2   1
```

Target = 8

Matching paths:

1. `5 → 3 = 8`
2. `5 → 2 → 1 = 8`
3. `-3 → 11 = 8`

Output:

```text
3
```

## 3. Difference Between Day 42, Day 43 and Day 44

| Day | Problem | Requirement |
|---|---|---|
| Day 42 | Path Sum | Check whether a root-to-leaf path matches |
| Day 43 | Path Sum II | Return all matching root-to-leaf paths |
| Day 44 | Path Sum III | Count all matching downward paths |

Day 44 is more flexible because a path can begin and end anywhere.

## 4. Basic Approach

One straightforward approach is to start a DFS from every node and count matching downward paths.

This approach can take O(n²) time in the worst case, especially for a tree that looks like a linked list.

To improve performance, we use prefix sums and a hash map.

## 5. Prefix Sum Concept

A prefix sum represents the sum from the root to the current node.

Suppose:

```text
Earlier prefix sum = 10
Current prefix sum = 18
```

The sum between those two positions is:

```text
18 - 10 = 8
```

Therefore:

```text
Earlier prefix = Current prefix - Target
```

This allows us to count matching paths using a dictionary.

## 6. Main Algorithm

The important sequence is:

**Count → Add → Explore → Undo**

1. Count matching earlier prefix sums.
2. Add the current prefix sum to the dictionary.
3. Explore the left and right children.
4. Remove the current prefix sum while backtracking.

The order matters. Counting before adding the current prefix prevents an empty path from being counted when the target is zero.

## 7. Initial Prefix Dictionary

We start with:

```python
prefix_count = {0: 1}
```

This represents the empty prefix before the root.

It allows paths that start at the root to be counted correctly.

## 8. Why Do We Use a Frequency Dictionary?

We use a dictionary containing prefix sums and their frequencies.

We cannot use a set because the same prefix sum may appear multiple times.

Example:

```text
0 → 0 → 0
```

For target 0, there are six nonempty downward paths.

Repeated prefix sums must therefore be counted separately.

## 9. Complete Implementation

File name:

`day44_path_sum_iii.py`

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_path_sum(root, target):
    prefix_count = {0: 1}

    def dfs(node, running):
        if node is None:
            return 0

        running += node.value

        needed = running - target
        total = prefix_count.get(needed, 0)

        prefix_count[running] = (
            prefix_count.get(running, 0) + 1
        )

        total += dfs(node.left, running)
        total += dfs(node.right, running)

        prefix_count[running] -= 1

        if prefix_count[running] == 0:
            del prefix_count[running]

        return total

    return dfs(root, 0)
```

## 10. Dry Run

For the example tree and target 8, the algorithm identifies:

```text
5 → 3       = 8
5 → 2 → 1   = 8
-3 → 11     = 8
```

Total matching paths:

```text
3
```

## 11. Why Backtracking Is Important

Backtracking removes the current prefix sum after exploring a node's children.

This ensures that prefix sums from one branch are not incorrectly used while exploring another branch.

For example, a path cannot move from a left child to a right child through their common parent.

Only downward parent-to-child paths are valid.

## 12. Connection With Day 43

In Day 43, we used:

```python
path.append(node.value)
path.pop()
```

In Day 44, we use a prefix frequency dictionary.

Both problems use DFS and backtracking.

The difference is that Day 43 stores actual paths, whereas Day 44 counts matching paths using prefix sums.

## 13. Correctness Explanation

The algorithm works because:

1. The current prefix sum represents the sum from the root to the current node.
2. Subtracting the target identifies the earlier prefix sum needed to form a matching path.
3. The dictionary frequency gives the number of matching starting positions.
4. DFS explores both child branches.
5. Backtracking removes the current prefix so it cannot affect unrelated branches.

Therefore, every valid downward path is counted, and invalid cross-branch paths are excluded.

## 14. Time and Space Complexity

| Complexity | Explanation |
|---|---|
| Time | O(n) average |
| Space | O(h) auxiliary space |

Where:

- `n` = number of nodes.
- `h` = height of the tree.

Each node is visited once. Dictionary operations take O(1) average time.

The recursion stack and active prefix dictionary use space proportional to the tree height.

A very deep tree may exceed Python's recursion limit.

## 15. Test Cases

| Test | Input | Expected |
|---|---|---:|
| 1 | Example tree, target 8 | 3 |
| 2 | Example tree, target 18 | 3 |
| 3 | Example tree, target 10 | 1 |
| 4 | Example tree, target 100 | 0 |
| 5 | Empty tree, target 0 | 0 |
| 6 | Single node 5, target 5 | 1 |
| 7 | Three zero-valued nodes, target 0 | 6 |

## 16. Assignment

Create a separate file:

`day44_assignment.py`

Assignment tree:

```text
       1
      / \
    -1   1
    /     \
   1      -1
```

Complete the `count_path_sum()` function using prefix sums and backtracking.

Expected results:

| Target | Expected count |
|---|---:|
| 1 | 3 |
| 0 | 3 |
| -1 | 1 |
| 5 | 0 |

## 17. Institute-Level Practice

1. Explain the prefix sum technique.
2. Why do we initialize the dictionary with `{0: 1}`?
3. Why is a frequency dictionary required instead of a set?
4. Explain the importance of backtracking.
5. Compare the brute-force and optimized approaches.

## 18. Corporate-Level Practice

1. Implement Path Sum III using DFS and a hash map.
2. Handle positive, negative and zero-valued nodes.
3. Test repeated prefix sums.
4. Explain time and space complexity.
5. Prevent prefix sums from one branch from affecting another branch.

## 19. Client-Level Understanding

A client wants to count how many continuous downward paths in a binary tree have a particular target sum.

The system should:
- Accept a binary tree and target value.
- Find all valid downward paths.
- Count matching paths.
- Handle negative and zero values.
- Return the total count.

The prefix sum and hash map approach provides an efficient solution.

## 20. GitHub File Name

`Day-44-DSA-Path-Sum-III-Prefix-Sums-and-Backtracking.md`

## 21. Final Understanding

Day 44 teaches how to combine prefix sums, hash maps, DFS and backtracking.

The key formula is:

```text
Earlier Prefix = Current Prefix - Target
```

The key algorithm sequence is:

```text
Count → Add → Explore → Undo
```

**Main takeaway:** Prefix sums help count matching downward paths efficiently without storing every possible path.
