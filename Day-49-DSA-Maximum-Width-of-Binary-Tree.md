# Day 49 – Maximum Width of a Binary Tree

## 1. Introduction

A binary tree is a hierarchical data structure in which each node can have at most two children: a left child and a right child.

In this problem, we calculate the **maximum width of a binary tree**.

The width of a level is determined by the positions of its leftmost and rightmost existing nodes, including the positions occupied by missing nodes between them.

The maximum width is the largest width among all levels of the tree.

This problem is important because it tests our understanding of:

- Binary tree traversal.
- Breadth-First Search (BFS).
- Queue operations.
- Complete binary tree indexing.
- Handling missing nodes.
- Efficient position tracking.

## 2. Problem Statement

Given the root of a binary tree, find the maximum width of the tree.

The width of one level is calculated as:

**Width = Position of the rightmost node − Position of the leftmost node + 1**

Missing positions between the leftmost and rightmost nodes must also be included.

If the tree is empty, return `0`.

### Example

Consider the following binary tree:

```text
        1
       / \
      3   2
     / \   \
    5   3   9
```

At level 1:

- Nodes: `[1]`
- Width: `1`

At level 2:

- Nodes: `[3, 2]`
- Width: `2`

At level 3:

- Existing nodes: `[5, 3, 9]`
- Positions: `[0, 1, 3]`
- Width: `3 - 0 + 1 = 4`

Therefore:

```text
Maximum Width = 4
```

Notice that level 3 contains only three actual nodes, but its width is four because one position between the first and last nodes is missing.

## 3. Understanding Maximum Width

It is important to distinguish between the number of existing nodes and the width of a level.

Consider:

```text
        1
       / \
      2   3
     /     \
    4       5
```

At the third level:

- Existing nodes: `2`
- First position: `0`
- Last position: `3`
- Width: `3 - 0 + 1 = 4`

The missing positions are included in the calculation.

Therefore, maximum width does not simply mean the maximum number of nodes present at any level.

It means the maximum positional distance between the first and last existing nodes at a level.

## 4. Difference Between Node Count and Width

| Property | Meaning |
|---|---|
| Node count | Number of actual nodes present at a level |
| Positional width | Number of positions from the first existing node to the last existing node, including gaps |
| Maximum width | Largest positional width among all levels |

Example:

```text
Level positions: [0, 1, 3]
```

- Actual node count = `3`
- First position = `0`
- Last position = `3`
- Width = `3 - 0 + 1`
- Width = `4`

This distinction is the main idea behind the problem.

## 5. Complete Binary Tree Indexing

To calculate the width, we assign a position index to every node.

We use the same indexing approach as a complete binary tree.

For a node at position `p`:

- Left child position = `2 * p + 1`
- Right child position = `2 * p + 2`

The root starts at position `0`.

### Example

```text
             1 (0)
            /     \
        2 (1)     3 (2)
        /  \       /  \
    4 (3) 5 (4) 6 (5) 7 (6)
```

The position values are:

| Node | Position |
|---|---:|
| Root | 0 |
| Left child | 1 |
| Right child | 2 |
| Left-left child | 3 |
| Left-right child | 4 |
| Right-left child | 5 |
| Right-right child | 6 |

These indexes allow us to calculate the width even when some nodes are missing.

## 6. Why Breadth-First Search Is Used

Breadth-First Search visits a binary tree level by level.

This makes BFS suitable because the maximum width must be calculated separately for every level.

For each level, we need to:

1. Identify the number of nodes currently waiting in the queue.
2. Obtain the position of the first node.
3. Process every node belonging to that level.
4. Track the position of the last node.
5. Calculate the level width.
6. Update the maximum width.
7. Continue to the next level.

A queue helps us maintain the correct level order.

## 7. Queue Structure

The queue stores two values for every node:

```python
(node, position)
```

Here:

- `node` represents the current tree node.
- `position` represents its calculated position.

Example:

```python
queue = deque([(root, 0)])
```

Initially, the root is inserted with position `0`.

When processing a node, its children are inserted using the indexing formulas:

```python
left_position = 2 * position + 1
right_position = 2 * position + 2
```

Only existing children are inserted into the queue.

We do not create additional nodes for missing positions.

## 8. Position Normalization

Position normalization is an important optimization.

Suppose the positions at a level are:

```text
[100, 101, 103]
```

The width is:

```text
103 - 100 + 1 = 4
```

Instead of continuing with large position values, subtract the first position from every position:

```text
[100 - 100, 101 - 100, 103 - 100]
```

The normalized positions become:

```text
[0, 1, 3]
```

The width remains:

```text
3 - 0 + 1 = 4
```

### Why Normalization Is Useful

Normalization:

- Reduces unnecessarily large common position offsets.
- Makes position values easier to understand.
- Helps control the growth of position values.
- Preserves the relative distance between nodes.
- Keeps the width calculation unchanged.

The first position of every level is used as the base.

```python
base = queue[0][1]
```

Every position is normalized using:

```python
position = raw_position - base
```

The normalized position is then used to calculate the next level's child positions.

## 9. Algorithm Design

The algorithm uses BFS with a queue.

### Step 1: Handle an Empty Tree

If the root is `None`, return `0`.

### Step 2: Initialize the Queue

Insert the root with position `0`.

```python
queue = deque([(root, 0)])
```

### Step 3: Initialize Maximum Width

```python
best = 0
```

This variable stores the largest width found so far.

### Step 4: Process Each Level

Find the number of nodes belonging to the current level:

```python
level_size = len(queue)
```

This value must remain fixed while processing the current level.

### Step 5: Normalize Positions

Obtain the first position:

```python
base = queue[0][1]
```

Subtract this base from every current position.

### Step 6: Process Every Node

Remove nodes from the queue one at a time.

Calculate the normalized position and update the last position.

### Step 7: Insert Existing Children

For a left child:

```python
queue.append((node.left, 2 * position + 1))
```

For a right child:

```python
queue.append((node.right, 2 * position + 2))
```

Only existing children are inserted.

### Step 8: Calculate Width

After processing the current level:

```python
width = last_position + 1
```

Because normalized positions begin at zero, the width is the last position plus one.

### Step 9: Update Maximum Width

```python
best = max(best, width)
```

After all levels have been processed, return `best`.

## 10. Complete Python Implementation

**Filename:** `day49_maximum_width_binary_tree.py`

```python
from collections import deque


class TreeNode:
    def __init__(
        self,
        value: int,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None
    ):
        self.value = value
        self.left = left
        self.right = right


def maximum_width(root: TreeNode | None) -> int:

    if root is None:
        return 0

    queue = deque([(root, 0)])

    best = 0

    while queue:

        level_size = len(queue)

        base = queue[0][1]

        last_position = 0

        for _ in range(level_size):

            node, raw_position = queue.popleft()

            position = raw_position - base

            last_position = position

            if node.left is not None:

                queue.append(
                    (node.left, 2 * position + 1)
                )

            if node.right is not None:

                queue.append(
                    (node.right, 2 * position + 2)
                )

        width = last_position + 1

        best = max(best, width)

    return best


def build_example_tree():

    root = TreeNode(1)

    root.left = TreeNode(3)
    root.right = TreeNode(2)

    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)

    root.right.right = TreeNode(9)

    return root


if __name__ == "__main__":

    print("DAY 49: MAXIMUM WIDTH OF A BINARY TREE")
    print("--------------------------------------")

    root = build_example_tree()

    result = maximum_width(root)

    print("Maximum width:", result)

    assert result == 4

    assert maximum_width(None) == 0

    assert maximum_width(TreeNode(10)) == 1

    print("All Day 49 main tests passed!")
```

## 11. Line-by-Line Explanation

### Importing deque

```python
from collections import deque
```

`deque` provides efficient insertion and removal operations at both ends.

We use it as a queue for BFS traversal.

### Creating the TreeNode Class

```python
class TreeNode:
```

This class represents one node in the binary tree.

Every node contains:

- `value`: The value stored in the node.
- `left`: Reference to the left child.
- `right`: Reference to the right child.

### Handling an Empty Tree

```python
if root is None:
    return 0
```

An empty tree does not contain any levels or nodes.

Therefore, its maximum width is zero.

### Initializing the Queue

```python
queue = deque([(root, 0)])
```

The root is inserted with position zero.

### Initializing the Result

```python
best = 0
```

This variable stores the maximum width found during traversal.

### Processing Each Level

```python
while queue:
```

The loop continues until every existing node has been processed.

### Finding the Level Size

```python
level_size = len(queue)
```

This stores the number of nodes in the current level.

It prevents children added during the current iteration from being processed as part of the same level.

### Finding the Base Position

```python
base = queue[0][1]
```

The first node's position becomes the base for normalization.

### Removing a Node

```python
node, raw_position = queue.popleft()
```

The node and its position are removed from the front of the queue.

### Normalizing the Position

```python
position = raw_position - base
```

The common offset is removed from the current position.

### Tracking the Last Position

```python
last_position = position
```

Because BFS processes nodes from left to right, the last processed node provides the rightmost existing position at the current level.

### Adding the Left Child

```python
if node.left is not None:
    queue.append((node.left, 2 * position + 1))
```

The left child receives the position calculated using the complete binary tree indexing formula.

### Adding the Right Child

```python
if node.right is not None:
    queue.append((node.right, 2 * position + 2))
```

The right child receives its corresponding position.

### Calculating Width

```python
width = last_position + 1
```

The first normalized position is zero.

Therefore, the width is the final position plus one.

### Updating the Result

```python
best = max(best, width)
```

The largest width is retained.

### Returning the Result

```python
return best
```

After all levels have been processed, the function returns the maximum width.

## 12. Complete Dry Run

Consider the following tree:

```text
        1
       / \
      3   2
     / \   \
    5   3   9
```

### Initial State

```text
Queue: [(1, 0)]
Maximum width: 0
```

### Level 1

The root has position `0`.

```text
Raw positions: [0]
Base: 0
Normalized positions: [0]
Width: 0 + 1 = 1
```

Children inserted:

- Node 3 at position 1.
- Node 2 at position 2.

```text
Queue: [(3, 1), (2, 2)]
Maximum width: 1
```

### Level 2

The current positions are `[1, 2]`.

```text
Base: 1
Normalized positions: [0, 1]
Width: 1 + 1 = 2
```

Children inserted:

- Node 5 at position 1.
- Node 3 at position 2.
- Node 9 at position 4.

```text
Queue: [(5, 1), (3, 2), (9, 4)]
Maximum width: 2
```

### Level 3

The current positions are `[1, 2, 4]`.

```text
Base: 1
Normalized positions: [0, 1, 3]
Width: 3 + 1 = 4
```

No additional children exist.

```text
Queue: []
Maximum width: 4
```

### Final Result

```text
Maximum Width = 4
```

## 13. Why Queue Length Alone Is Incorrect

A common mistake is to calculate the width using:

```python
width = len(queue)
```

This only counts existing nodes.

Consider:

```text
        1
       / \
      2   3
     /     \
    4       5
```

The third level contains two existing nodes.

However, their positions are:

```text
[0, 3]
```

The correct width is:

```text
3 - 0 + 1 = 4
```

Using the queue length would return `2`, which is incorrect.

Therefore, position indexes are necessary.

## 14. Day 49 Practice Tree

The following tree is used in the separate practice file:

```text
          10
         /  \
        5    15
       /       \
      3         20
       \       /
        4     18
```

### Original Complete-Tree Positions

The original positions are calculated without normalization.

| Level | Existing node positions | Width |
|---|---|---:|
| 1 | `[0]` | 1 |
| 2 | `[1, 2]` | 2 |
| 3 | `[3, 6]` | 4 |
| 4 | `[8, 13]` | 6 |

At level 4:

```text
Width = 13 - 8 + 1
Width = 6
```

Therefore:

```text
Maximum Width = 6
```

### Positions Used by the Normalized Algorithm

The implementation normalizes positions at each level.

| Level | Queued positions before current-level normalization | Base | Normalized positions | Width |
|---|---|---:|---|---:|
| 1 | `[0]` | 0 | `[0]` | 1 |
| 2 | `[1, 2]` | 1 | `[0, 1]` | 2 |
| 3 | `[1, 4]` | 1 | `[0, 3]` | 4 |
| 4 | `[2, 7]` | 2 | `[0, 5]` | 6 |

Both approaches calculate the same width.

The original positions describe the tree's complete-tree indexing. The queued positions describe the values maintained by the normalized implementation.

## 15. Edge Cases

A good implementation must handle different tree structures.

### Case 1: Empty Tree

```python
root = None
```

Expected result:

```text
0
```

### Case 2: Single Node

```text
    10
```

Expected result:

```text
1
```

### Case 3: Left-Skewed Tree

```text
    1
   /
  2
 /
3
```

Every level contains one node.

Expected result:

```text
1
```

### Case 4: Right-Skewed Tree

```text
1
 \
  2
   \
    3
```

Every level contains one node.

Expected result:

```text
1
```

### Case 5: Sparse Tree

```text
        1
       / \
      2   3
     /     \
    4       5
```

The last level has two existing nodes but a positional width of four.

Expected result:

```text
4
```

### Case 6: Duplicate Values

```text
        5
       / \
      5   5
     /     \
    5       5
```

Duplicate values do not affect the algorithm because node positions, not node values, determine width.

Expected result:

```text
4
```

## 16. Time and Space Complexity

### Time Complexity: O(n)

Every existing node is:

- Inserted into the queue once.
- Removed from the queue once.
- Processed once.

Therefore, the traversal takes O(n) time, where `n` is the total number of nodes.

### Space Complexity: O(w)

The queue stores nodes from the current and next levels.

The auxiliary queue space is O(w), where `w` represents the maximum number of existing nodes at any level.

The positional width can be much larger than the number of existing nodes because of missing positions.

Python integers can grow to accommodate large position values. Normalization reduces common offsets, although very large genuine gaps can still produce large integer positions.

## 17. Algorithm Correctness

The algorithm correctly calculates the maximum width because it maintains the positional relationship between nodes at every level.

### First: Correct Position Assignment

The root receives position zero.

Every existing left and right child receives its position using:

```text
Left child  = 2 * parent position + 1
Right child = 2 * parent position + 2
```

These formulas preserve the relative positions that would exist in a complete binary tree.

### Second: Correct Level Processing

BFS processes nodes level by level.

The fixed `level_size` ensures that nodes belonging to the next level are not processed prematurely.

### Third: Correct Normalization

Subtracting the same base from every position at a level does not change the difference between the first and last positions.

Therefore, normalization does not change the width.

### Fourth: Correct Width Calculation

After normalization, the first position is zero.

The last position plus one gives the number of positions between the first and last nodes, including gaps.

### Fifth: Correct Maximum Selection

The algorithm compares each level's width with the current maximum.

After every level has been processed, the stored result is the maximum width of the entire tree.

## 18. Common Mistakes

### Mistake 1: Counting Only Existing Nodes

Using the number of nodes in the queue gives the actual node count, not the positional width.

**Solution:** Track node positions.

### Mistake 2: Forgetting the Plus One

Incorrect:

```python
width = last_position - first_position
```

Correct:

```python
width = last_position - first_position + 1
```

The additional one includes both endpoint positions.

### Mistake 3: Processing the Entire Queue as One Level

If the queue size is not fixed before processing a level, newly inserted children may be processed too early.

**Solution:**

```python
level_size = len(queue)
```

Use this value in the current level's loop.

### Mistake 4: Enqueuing Missing Nodes

Creating placeholder nodes for every missing position wastes memory and can cause excessive processing.

**Solution:** Insert only existing children and preserve their calculated positions.

### Mistake 5: Incorrect Normalization

The base must be taken from the first node of the current level.

**Solution:**

```python
base = queue[0][1]
```

Then subtract it from every position at that level.

### Mistake 6: Using the Wrong Child Position Formula

The correct formulas are:

```python
left_position = 2 * position + 1
right_position = 2 * position + 2
```

Using an incorrect formula produces incorrect widths at deeper levels.

## 19. Practical Applications

The concept of positional width can help explain the structure and distribution of nodes in hierarchical systems.

Examples include:

- Analysing sparse binary tree structures.
- Understanding gaps in hierarchical layouts.
- Evaluating the shape of a tree.
- Studying tree traversal algorithms.
- Representing hierarchical positions.
- Understanding complete binary tree indexing.

The important lesson is that the number of existing elements does not always represent the full positional span of a structure.

## 20. Understanding Width Through Institute, Corporate, and Client Examples

The same idea can be understood using a hierarchical arrangement.

### Institute Example

Imagine an institute where students are arranged across different branches of a hierarchy.

Some branches may contain students while other positions remain empty.

Counting only the students would not show the full distance between the first and last occupied positions.

### Corporate Example

Imagine a company hierarchy with departments arranged under managers.

Some departments may be missing, but their positions still affect the overall span of the hierarchy.

### Client Example

Imagine a service system where clients are assigned positions under different service groups.

If the first and last clients are separated by unoccupied positions, counting only the actual clients does not represent the complete positional width.

These examples illustrate why positional width and actual element count are different measurements.

## 21. Conclusion

The Maximum Width of a Binary Tree problem demonstrates how position tracking can solve a problem that cannot be handled by simply counting nodes.

By combining Breadth-First Search, queue operations, complete binary tree indexing, and position normalization, we can calculate the correct width efficiently.

The most important concept in Day 49 is understanding that **the width of a level includes missing positions between its leftmost and rightmost existing nodes**.

The implementation processes only actual nodes while using their positions to account for gaps. This makes the solution efficient and suitable for sparse binary trees.

**Day 49 completed: Maximum Width of a Binary Tree.**