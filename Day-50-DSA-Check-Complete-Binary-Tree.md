# Day 50 – Check Whether a Binary Tree Is Complete

## 1. Introduction

A binary tree is a hierarchical data structure in which every node can have at most two children:

- Left child
- Right child

In Day 49, we calculated the maximum width of a binary tree by counting the positions between the first and last existing nodes at each level.

In Day 50, we solve a different problem:

**How can we determine whether a binary tree is complete?**

A complete binary tree follows a specific arrangement:

1. Every level except possibly the last level must be completely filled.
2. The last level must be filled from left to right.
3. There must not be an empty position before an existing node.

We use Breadth-First Search (BFS), a queue, and a Boolean variable called `seen_gap` to solve this problem.

## 2. Problem Statement

Given the root of a binary tree, determine whether the tree is complete.

Return:

- `True` if the binary tree is complete.
- `False` if the binary tree is not complete.

### Example 1: Complete Binary Tree

```text
        1
       / \
      2   3
     / \  /
    4   5 6
```

Explanation:

- Level 1 contains one node.
- Level 2 contains two nodes.
- The last level contains nodes from left to right.
- The remaining empty position appears at the end.

Therefore, this tree is complete.

Output:

```python
True
```

### Example 2: Incomplete Binary Tree

```text
        1
       / \
      2   3
     /   / \
    4   6   7
```

Explanation:

- Node 2 has a left child but no right child.
- Node 3 has children after that missing position.
- An empty position occurs before an existing node.

Therefore, this tree is not complete.

Output:

```python
False
```

**Important:** Missing positions at the end of the last level are allowed. Missing positions before another existing node are not allowed.

## 3. Understanding Completeness Through Classroom Seating

Imagine a classroom in which students must sit according to the following rules:

1. Fill the front row before using the next row.
2. Students must sit from left to right.
3. An empty seat cannot appear before another occupied seat.

A complete binary tree follows the same arrangement.

### Valid Arrangement

```text
        1
       / \
      2   3
     / \  /
    4   5 6
```

All available positions are filled from left to right.

The final position is empty, which is allowed.

### Invalid Arrangement

```text
        1
       / \
      2   3
     /     \
    4       5
```

There is an empty position where the right child of node 2 should be, but node 3 has a right child.

This breaks the left-to-right arrangement.

The main concept is:

**Once an empty position is found, every position after it must also be empty.**

## 4. Clarifying the Problem Before Coding

Before writing the implementation, understand the input, output, and conditions.

### Input

The root node of a valid binary tree.

### Output

A Boolean value:

- `True` for a complete binary tree.
- `False` for an incomplete binary tree.

### Conditions

- An empty tree is considered complete.
- A single-node tree is complete.
- Node values can be repeated.
- Values do not need to follow Binary Search Tree ordering.
- The original tree must not be modified.
- The input is assumed to be a valid tree without cycles or shared child nodes.

This problem checks the arrangement of nodes, not their values.

## 5. Main Concepts Required

Only three important components are required.

| Component       | Purpose                                                  |
| --------------- | -------------------------------------------------------- |
| BFS queue       | Visits positions level by level, from left to right      |
| `None` entries  | Make missing positions visible                           |
| `seen_gap` flag | Remembers whether an empty position has already appeared |

The entire algorithm depends on one condition:

> Once BFS encounters an empty position, every remaining position must also be empty.

If a real node appears after an empty position, the tree is incomplete.

## 6. Why Breadth-First Search Is Used

Breadth-First Search is a tree traversal technique that visits nodes level by level.

For example:

```text
        1
       / \
      2   3
     / \  /
    4   5 6
```

The BFS traversal order is:

```text
1 → 2 → 3 → 4 → 5 → 6
```

This order is important because completeness is defined from top to bottom and from left to right.

BFS allows us to identify the first missing position and check whether any real node appears afterward.

### Why Not Use DFS?

Depth-First Search explores one branch deeply before moving to another branch.

However, completeness depends on the order of positions across an entire level.

BFS is therefore a natural and straightforward choice for this problem.

## 7. Understanding the Queue

The queue stores the nodes in the order in which they must be checked.

Unlike Day 49, where we stored only existing nodes with their position indexes, Day 50 explicitly stores `None` entries.

Example:

```python
queue = deque([root])
```

For every real node, we insert both children:

```python
queue.append(node.left)
queue.append(node.right)
```

Even if a child is missing, its `None` value must be inserted.

This allows the algorithm to detect gaps.

### Why Do We Insert None?

Consider:

```text
        1
       / \
      2   3
     /     \
    4       5
```

If missing children are skipped, the queue will contain only real nodes.

The algorithm will not know that the right child of node 2 was missing before reaching node 5.

By inserting `None`, we preserve the missing position in the BFS order.

**Important:** We do not enqueue children for a `None` entry. An empty position has no children to explore.

## 8. Understanding the seen_gap Flag

The most important variable in this algorithm is:

```python
seen_gap = False
```

It records whether BFS has already encountered an empty position.

There are three possible situations.

### Situation 1: A Real Node Before Any Gap

If a real node is found while `seen_gap` is `False`, the position is valid.

The algorithm inserts both children into the queue.

### Situation 2: An Empty Position

If the current entry is `None`, the algorithm executes:

```python
seen_gap = True
```

This means an empty position has been encountered.

The traversal continues because missing positions at the end are allowed.

### Situation 3: A Real Node After a Gap

If a real node appears while `seen_gap` is `True`, the tree is not complete.

The algorithm immediately returns:

```python
return False
```

This is the main decision-making condition.

## 9. Algorithm Design

The solution follows these steps.

### Step 1: Handle an Empty Tree

```python
if root is None:
    return True
```

An empty tree is considered complete.

### Step 2: Initialize the Queue

```python
queue = deque([root])
```

Insert the root into the queue.

### Step 3: Initialize the Gap Flag

```python
seen_gap = False
```

Initially, no missing position has been found.

### Step 4: Process the Queue

```python
while queue:
    node = queue.popleft()
```

Remove the first entry from the queue.

### Step 5: Check for an Empty Position

```python
if node is None:
    seen_gap = True
    continue
```

If the current entry is missing:

- Mark that a gap has been found.
- Continue to the next queue entry.

### Step 6: Check for a Real Node After a Gap

```python
if seen_gap:
    return False
```

If an existing node appears after an earlier missing position, the tree is incomplete.

### Step 7: Insert Both Children

```python
queue.append(node.left)
queue.append(node.right)
```

Both children are inserted, even if one or both are `None`.

### Step 8: Return True

If the queue becomes empty without finding a real node after a gap:

```python
return True
```

The tree is complete.

## 10. Complete Python Implementation

**Filename:** `day50_check_complete_binary_tree.py`

```python
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_complete(root):

    if root is None:
        return True

    queue = deque([root])
    seen_gap = False

    while queue:

        node = queue.popleft()

        if node is None:
            seen_gap = True
            continue

        if seen_gap:
            return False

        queue.append(node.left)
        queue.append(node.right)

    return True


def build_complete_tree():

    root = Node(
        1,
        Node(2, Node(4), Node(5)),
        Node(3, Node(6))
    )

    return root


def build_incomplete_tree():

    root = Node(
        1,
        Node(2, Node(4)),
        Node(3, Node(6), Node(7))
    )

    return root


if __name__ == "__main__":

    print("DAY 50: CHECK WHETHER A BINARY TREE IS COMPLETE")
   
    complete_tree = build_complete_tree()
    incomplete_tree = build_incomplete_tree()

    print("Complete tree:", is_complete(complete_tree))
    print("Incomplete tree:", is_complete(incomplete_tree))

    assert is_complete(None) is True
    assert is_complete(Node(1)) is True

    assert is_complete(complete_tree) is True
    assert is_complete(incomplete_tree) is False

    assert is_complete(Node(1, Node(2))) is True

    assert is_complete(Node(1, right=Node(2))) is False

    print("\nAll Day 50 main tests passed!")
```

## 11. Line-by-Line Code Explanation

### Importing deque

```python
from collections import deque
```

The `deque` data structure is used as a queue.

It supports efficient insertion at the back and removal from the front.

### Creating the Node Class

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

Each node contains:

- `value`: The value stored in the node.
- `left`: Reference to the left child.
- `right`: Reference to the right child.

### Checking an Empty Tree

```python
if root is None:
    return True
```

An empty tree is considered complete because it does not violate any completeness condition.

### Creating the Queue

```python
queue = deque([root])
```

The root is inserted into the queue.

### Initializing the Flag

```python
seen_gap = False
```

This variable indicates whether an empty position has been encountered.

### Processing the Queue

```python
while queue:
    node = queue.popleft()
```

The loop continues until all queue entries have been processed.

### Detecting an Empty Position

```python
if node is None:
    seen_gap = True
    continue
```

When a missing position is found, the flag becomes `True`.

The `continue` statement skips the remaining operations for that queue entry.

### Detecting an Invalid Node

```python
if seen_gap:
    return False
```

A real node appearing after a missing position violates completeness.

Therefore, the function returns `False`.

### Adding Children

```python
queue.append(node.left)
queue.append(node.right)
```

Both child positions are inserted.

This is necessary to preserve the left-to-right position sequence.

### Returning the Final Result

```python
return True
```

If no invalid position is found, the tree is complete.

## 12. Complete Dry Run

Consider the following incomplete tree:

```text
        1
       / \
      2   3
     /     \
    4       6
```

The BFS queue begins with:

```text
Queue: [1]
seen_gap = False
```

### Processing Node 1

Node 1 is a real node.

Add its children:

```text
Queue: [2, 3]
seen_gap = False
```

### Processing Node 2

Node 2 is a real node.

Add its children:

```text
Queue: [3, 4, None]
seen_gap = False
```

### Processing Node 3

Node 3 is a real node.

Add its children:

```text
Queue: [4, None, None, 6]
seen_gap = False
```

### Processing Node 4

Node 4 is a real node.

Add its children:

```text
Queue: [None, None, 6, None, None]
seen_gap = False
```

### Processing None

An empty position is found.

```text
Queue: [None, 6, None, None]
seen_gap = True
```

The algorithm continues.

### Processing the Next None

Another empty position is found.

```text
Queue: [6, None, None]
seen_gap = True
```

### Processing Node 6

Node 6 is a real node, but `seen_gap` is already `True`.

The condition is satisfied:

```python
if seen_gap:
    return False
```

The algorithm returns:

```text
False
```

### Dry Run Summary

| Entry removed | `seen_gap` before | Action               |
| ------------- | ----------------- | -------------------- |
| 1             | False             | Add 2 and 3          |
| 2             | False             | Add 4 and None       |
| 3             | False             | Add None and 6       |
| 4             | False             | Add None and None    |
| None          | False             | Set gap flag to True |
| None          | True              | Continue             |
| 6             | True              | Return False         |

The important point is that the tree does not become invalid merely because a missing child is found.

It becomes invalid when a real node appears after that missing position.

## 13. Why the Algorithm Works

The algorithm works because BFS visits positions in exactly the order required by the definition of a complete binary tree.

### First: BFS Preserves Position Order

BFS visits nodes from top to bottom and from left to right.

Therefore, an empty position is discovered before any later position.

### Second: The Gap Flag Remembers Missing Positions

Once an empty position is found, `seen_gap` becomes `True`.

The flag is never reset.

This ensures that gaps found at earlier levels also affect later positions.

### Third: Real Nodes After Gaps Are Invalid

If an actual node appears after a gap, the occupied positions are not continuously filled from left to right.

Therefore, the tree is incomplete.

### Fourth: No Real Node After a Gap Means Complete

If the traversal finishes without finding a real node after the first gap, all occupied positions form a continuous sequence.

This is exactly the definition of a complete binary tree.

### Important Invariant

`seen_gap` is `True` exactly when an earlier processed position was empty.

## 14. Difference Between Complete, Full, Perfect, and Balanced Trees

These four concepts are different.

| Tree type       | Meaning                                                                            |
| --------------- | ---------------------------------------------------------------------------------- |
| Complete        | All levels are filled except possibly the last, which is filled from left to right |
| Full            | Every node has either zero or two children                                         |
| Perfect         | Every internal node has two children, and all leaves are at the same depth         |
| Height-balanced | At every node, the left and right subtree heights differ by at most one            |

### Example: Complete but Not Full

```text
    1
   /
  2
```

This tree is complete because the last level is filled from the left.

However, it is not full because node 1 has only one child.

It is also not perfect.

### Example: Balanced but Not Complete

```text
    1
     \
      2
```

The tree is height-balanced because the height difference between the left and right subtrees is at most one.

However, it is not complete because the left position is empty before an occupied right position.

### Important Point

An ordinary Binary Search Tree does not have to be complete.

Completeness describes the tree's shape, not the ordering of its values.

## 15. Time and Space Complexity

Let `n` represent the total number of actual nodes.

### Time Complexity: O(n)

Every real node is removed from the queue and processed once.

Each real node adds exactly two child entries.

Therefore, the total number of queue entries processed is at most `2n + 1`.

The overall time complexity is:

```text
O(n)
```

### Auxiliary Space Complexity: O(n)

The queue can store real and missing positions from the current and next levels.

In the worst case, its size is proportional to the number of nodes.

Therefore:

```text
O(n)
```

### Complexity Summary

| Complexity      | Result |
| --------------- | ------ |
| Time            | O(n)   |
| Auxiliary space | O(n)   |

## 16. Common Mistakes

### Mistake 1: Skipping Missing Children

Incorrect approach:

```python
if node.left is not None:
    queue.append(node.left)
```

This hides the missing positions required by this algorithm.

Correct approach:

```python
queue.append(node.left)
queue.append(node.right)
```

Both children must be inserted.

### Mistake 2: Returning False Immediately at the First None

Every finite binary tree eventually has missing child positions.

A missing position alone does not mean the tree is incomplete.

The algorithm must continue checking for a later real node.

### Mistake 3: Resetting the Gap Flag

Incorrect:

```python
seen_gap = False
```

Resetting the flag for each level can hide a gap found at an earlier level.

The flag must remain active throughout the traversal.

### Mistake 4: Using Node Values to Determine Completeness

Completeness does not depend on the values stored in the nodes.

Repeated values and unsorted values are allowed.

Only the arrangement of the nodes matters.

### Mistake 5: Reusing Day 49 Queue Logic Without Changes

Day 49 and Day 50 use different queue strategies.

| Day    | Queue strategy                                        |
| ------ | ----------------------------------------------------- |
| Day 49 | Stores existing nodes with their position indexes     |
| Day 50 | Stores actual nodes and `None` entries to detect gaps |

Day 49 calculates positional width. Day 50 checks whether the tree is left-packed.

## 17. Test Cases

A good implementation should handle different tree arrangements.

### Test 1: Empty Tree

```python
assert is_complete(None) is True
```

Expected:

```text
True
```

### Test 2: Single Node

```python
assert is_complete(Node(1)) is True
```

Expected:

```text
True
```

### Test 3: Left Child Only

```python
assert is_complete(Node(1, Node(2))) is True
```

Expected:

```text
True
```

The final level is filled from the left.

### Test 4: Right Child Only

```python
assert is_complete(Node(1, right=Node(2))) is False
```

Expected:

```text
False
```

The left position is empty before the right position.

### Test 5: Perfect Tree

```python
assert is_complete(
    Node(1, Node(2), Node(3))
) is True
```

Expected:

```text
True
```

### Test 6: Deeper Left-Only Tree

```python
assert is_complete(
    Node(1, Node(2, Node(3)))
) is False
```

Expected:

```text
False
```

Node 3 appears after an empty position.

### Test 7: Duplicate Values

```python
assert is_complete(
    Node(7, Node(7), Node(7))
) is True
```

Expected:

```text
True
```

Repeated values do not affect completeness.

## 18. Day 50 Practice Tasks

### Part A: Predict and Explain

For each tree:

1. Determine whether the tree is complete.
2. If it is incomplete, identify the first gap.
3. Identify the real node that appears after the gap.

### Tree A

```text
        10
       /  \
      5    15
     / \   /
    3   7 12
```

Expected:

```text
True
```

### Tree B

```text
        10
       /  \
      5    15
     / \     \
    3   7     20
```

Expected:

```text
False
```

### Tree C

```text
        10
       /
      5
     /
    3
```

Expected:

```text
False
```

### Part B: Implement the Function

Implement the following function independently:

```python
def is_complete(root):
    ...
```

Requirements:

- Use a queue.
- Do not modify the original tree.
- Handle an empty tree.
- Use a `seen_gap` flag.
- Pass all the test cases.
- Explain why `None` entries must remain visible.

### Part C: Implement a Diagnostic Function

Create another function:

```python
def completeness_report(root):
    ...
```

It should return:

For a complete tree:

```python
(True, None)
```

For an incomplete tree:

```python
(False, offending_node.value)
```

Expected results:

```text
Tree A → (True, None)
Tree B → (False, 20)
Tree C → (False, 3)
```

**Additional consideration:** If different nodes have duplicate values, returning only the value does not uniquely identify the offending node. A unique node ID or location would be more useful in that situation.

## 19. Institute, Corporate, and Client-Level Thinking

Understanding the algorithm is useful, but it is also important to know where this concept is applied.

### Institute and Interview Perspective

In an interview, you should be able to:

- Define a complete binary tree.
- Explain why BFS is used.
- Explain the purpose of `None` entries.
- Explain the `seen_gap` flag.
- Identify the first invalid position.
- Discuss time and space complexity.

### Corporate Implementation Perspective

In a software project, a completeness checker can be used to:

- Validate hierarchical data structures.
- Check whether a tree follows a required layout.
- Detect missing positions.
- Provide diagnostic information.
- Write automated validation tests.

### Client Perspective

Before implementing the solution for a client, understand:

- Whether missing positions are actually invalid.
- Whether incomplete structures should be rejected.
- Whether the system should report the first invalid node.
- Whether the system should attempt to repair the structure.

### Practical Connection: Binary Heaps

A binary heap requires a complete binary tree structure.

A min-heap also follows an ordering rule:

- Every parent must be less than or equal to its children.

Our `is_complete()` function checks only the shape of the tree.

It does not check heap ordering.

Therefore, checking completeness alone is not enough to establish that a tree is a valid min-heap.

Also, the implementation assumes a valid tree without cycles or shared child nodes. Those conditions would need separate validation if the input did not guarantee them.

## 20. Conclusion

The Check Whether a Binary Tree Is Complete problem teaches how to validate the arrangement of nodes in a binary tree.

The solution uses Breadth-First Search to visit positions from top to bottom and left to right.

A queue stores both real nodes and missing positions. The `seen_gap` flag remembers when the first missing position has appeared.

If another real node appears after that gap, the tree is incomplete.

The most important concept in Day 50 is:

**Once BFS encounters an empty position, every remaining position must also be empty.**

The algorithm takes O(n) time and O(n) auxiliary space.

**Day 50 completed: Check Whether a Binary Tree Is Complete.**
