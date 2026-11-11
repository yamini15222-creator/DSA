
# Day 48 – Binary Tree Right Side View

## 1. Problem Statement

Given the root of a binary tree, return the values of the nodes that are visible when the tree is viewed from its right side.

The right-side view contains the rightmost visible node at every level of the binary tree.

Each level contributes exactly one node to the result.

If the tree is empty, return an empty list.

## 2. Objective

The objective is to understand how to traverse a binary tree level by level and identify the rightmost node at each level.

This problem can be solved using two approaches:

1. Breadth-First Search (BFS) – Level Order Traversal.
2. Depth-First Search (DFS) – Right-First Preorder Traversal.

Both approaches produce the same right-side view.

## 3. Example 1 – Basic Binary Tree

### Input Tree

```text
        1
       / \
      2   3
       \   \
        5   4
```

### Level Order Traversal

```text
Level 0: [1]
Level 1: [2, 3]
Level 2: [5, 4]
```

### Right-Side View

```python
[1, 3, 4]
```

### Explanation

- At level 0, node 1 is visible.
- At level 1, node 3 is the rightmost node.
- At level 2, node 4 is the rightmost node.

Therefore, the output is `[1, 3, 4]`.

## 4. Example 2 – Deeper Left Subtree

The right-side view does not always consist of nodes reached by following only right-child pointers.

Sometimes, a node from the left subtree becomes visible because there is no node on the right at that depth.

### Input Tree

```text
        1
       / \
      2   3
       \
        5
         \
          6
```

### Level Order Traversal

```text
Level 0: [1]
Level 1: [2, 3]
Level 2: [5]
Level 3: [6]
```

### Right-Side View

```python
[1, 3, 5, 6]
```

### Explanation

- Level 0: Node 1 is visible.
- Level 1: Node 3 is visible.
- Level 2: Node 5 is the only node at that level.
- Level 3: Node 6 is the only node at that level.

This example shows why we must consider every level instead of simply following the right-child pointers.

## 5. Day 48 Practice Tree

### Input Tree

```text
          10
         /  \
        5    15
       / \   /
      3   7 12
           \
            8
```

### Level Order Traversal

```text
Level 0: [10]
Level 1: [5, 15]
Level 2: [3, 7, 12]
Level 3: [8]
```

### Right-Side View

```python
[10, 15, 12, 8]
```

### Left-Side View (Extension)

```python
[10, 5, 3, 8]
```

The left-side view is an extension exercise. The main problem for Day 48 is the right-side view.

## 6. Approach 1 – Breadth-First Search (BFS)

### Concept

Breadth-First Search visits nodes level by level.

We use a queue to process the nodes.

For every level:

1. Find the number of nodes currently present in the queue.
2. Process exactly that many nodes.
3. Add the left child to the queue if it exists.
4. Add the right child to the queue if it exists.
5. Store the last node processed at that level.

Since nodes are processed from left to right, the last node of each level is the rightmost node.

### Algorithm

```text
1. If root is None, return an empty list.

2. Create an empty result list.

3. Create a queue and insert the root node.

4. While the queue is not empty:

   a. Store the current queue size in level_size.

   b. Repeat level_size times:

      i. Remove the front node from the queue.

      ii. If it is the last node of this level,
          add its value to the result.

      iii. Add its left child if it exists.

      iv. Add its right child if it exists.

5. Return the result list.
```

### Important Point

We must store the queue size before processing the current level.

```python
level_size = len(queue)
```

This ensures that children added during the current level are processed only in the next level.

### Python Implementation

```python
from collections import deque

def right_side_view_bfs(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for index in range(level_size):
            node = queue.popleft()

            if index == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result
```

## 7. Approach 2 – Depth-First Search (DFS)

### Concept

Depth-First Search explores one branch deeply before exploring another branch.

For the right-side view, we visit:

1. Root node.
2. Right subtree.
3. Left subtree.

This is called right-first preorder traversal.

We maintain the current depth.

If the current depth equals the length of the result list, it means that we have reached this level for the first time.

Because we visit the right subtree first, the first node encountered at each depth is the rightmost visible node.

### Algorithm

```text
1. Create an empty result list.

2. Define a recursive DFS function with:
   - Current node
   - Current depth

3. If the current node is None, return.

4. If depth equals the length of the result:
   Add the current node value.

5. Visit the right child with depth + 1.

6. Visit the left child with depth + 1.

7. Return the result list.
```

### Python Implementation

```python
def right_side_view_dfs(root):
    result = []

    def dfs(node, depth):
        if node is None:
            return

        if depth == len(result):
            result.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)

    return result
```

## 8. BFS vs DFS Comparison

| Feature | BFS | DFS |
|---|---|---|
| Traversal | Level by level | Depth first |
| Data structure | Queue | Recursion |
| Visiting order | Left to right | Right to left |
| Selected node | Last node of level | First node at depth |
| Time complexity | O(n) | O(n) |
| Auxiliary space | O(w) | O(h) |
| Tree modification | No | No |

Where:

- n = number of nodes.
- w = maximum width of the tree.
- h = height of the tree.

## 9. Time Complexity Analysis

### BFS

Every node is inserted into the queue once and removed from the queue once.

Therefore:

```text
Time Complexity: O(n)
```

The queue stores nodes from the current and next levels.

```text
Auxiliary Space Complexity: O(w)
```

Here, w represents the maximum width of the tree.

### DFS

Every node is visited exactly once.

Therefore:

```text
Time Complexity: O(n)
```

The recursive call stack depends on the height of the tree.

```text
Auxiliary Space Complexity: O(h)
```

Here, h represents the height of the tree.

For a skewed tree, the recursion depth can reach n.

## 10. Edge Cases

The following cases should be tested:

| Test Case | Input | Expected Output |
|---|---|---|
| Empty tree | None | [] |
| Single node | 7 | [7] |
| Left-only chain | 1 → 2 → 3 | [1, 2, 3] |
| Right-only chain | 1 → 2 → 3 | [1, 2, 3] |
| Rightmost is not maximum | Root 1, left 100, right 2 | [1, 2] |
| Duplicate values | Root 5, right child 5 | [5, 5] |
| Complete example | Given example tree | [1, 3, 4] |
| Deeper left subtree | Given deeper example | [1, 3, 5, 6] |

## 11. Important Observations

1. The right-side view contains one visible node per level.
2. BFS selects the last node of every level.
3. DFS selects the first node encountered at every depth.
4. DFS must visit the right subtree before the left subtree.
5. BFS must process nodes from left to right.
6. The queue size must be stored before processing a level.
7. The right-side view is not necessarily the path formed by following right pointers.
8. Duplicate values must be preserved if they occur at different levels.
9. The original binary tree must remain unchanged.

## 12. Common Mistakes

### Mistake 1: Following Only Right Pointers

Incorrect approach:

```python
while root:
    result.append(root.val)
    root = root.right
```

This fails when a left-subtree node becomes visible at a deeper level.

### Mistake 2: Not Fixing the Level Size

Incorrect BFS logic may process newly inserted children as if they belong to the current level.

Correct approach:

```python
level_size = len(queue)
```

### Mistake 3: Using the Wrong DFS Order

For the right-side view, DFS should visit the right child before the left child.

Correct:

```python
dfs(node.right, depth + 1)
dfs(node.left, depth + 1)
```

### Mistake 4: Selecting the First BFS Node

BFS processes nodes from left to right, so the first node is the leftmost node, not the rightmost node.

Correct:

```python
if index == level_size - 1:
    result.append(node.val)
```

## 13. Testing Strategy

The implementation should be tested with:

- Empty binary tree.
- Single-node binary tree.
- Left-skewed binary tree.
- Right-skewed binary tree.
- Balanced binary tree.
- Tree with missing right children.
- Tree with duplicate values.
- Tree where a deeper left-subtree node is visible.

Both BFS and DFS implementations should return the same output for every test case.

The original tree should also be checked to ensure that traversal does not modify its structure.

## 14. Expected Output

For the main example:

```text
DAY 48: BINARY TREE RIGHT SIDE VIEW

BFS result: [1, 3, 4]
DFS result: [1, 3, 4]

All Day 48 tests passed!
```

For the Day 48 practice tree:

```text
BFS right-side view: [10, 15, 12, 8]
DFS right-side view: [10, 15, 12, 8]

Both approaches agree: Yes
```

## 15. Key Takeaways

- BFS uses a queue and selects the last node at each level.
- DFS uses recursion and visits right before left.
- Both approaches have O(n) time complexity.
- BFS uses O(w) auxiliary space.
- DFS uses O(h) auxiliary space.
- A left-subtree node can be visible from the right side.
- The tree structure remains unchanged.

## 16. Conclusion

In Day 48, we learned how to find the right-side view of a binary tree using BFS and DFS.

BFS identifies the last node at every level, while DFS identifies the first node at every depth by visiting the right subtree before the left subtree.

Both methods solve the problem efficiently in O(n) time.

This practice strengthens our understanding of binary tree traversal, level processing, recursion, queues, and tree visibility.
