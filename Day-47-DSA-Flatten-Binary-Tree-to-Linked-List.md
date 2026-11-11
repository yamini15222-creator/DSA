# Day 47 – Flatten a Binary Tree to a Linked List

## 1. Introduction

Day 47 focuses on transforming a binary tree into a single right-linked chain while preserving the original preorder traversal sequence.

A binary tree is a hierarchical data structure in which each node can have at most two children:
- Left child
- Right child

In this problem, the tree must be transformed into a linked-list-like structure using the existing nodes.

Preorder traversal visits nodes in the following order:

**Root → Left → Right**

The transformation must preserve this order while modifying the original node connections.

This problem introduces an important concept in data structures: **in-place pointer manipulation**. Instead of creating a new linked list, we rearrange the existing tree pointers.

## 2. Problem Statement

Given the root of a binary tree, flatten the tree into a single right-linked chain following preorder traversal.

The flattened tree must satisfy the following conditions:

1. Every node's `left` pointer must become `None`.
2. Every node's `right` pointer must point to the next node in preorder.
3. All original tree nodes must be reused.
4. Every original node must appear exactly once.
5. The relative order of nodes must remain the same as preorder traversal.
6. No additional tree nodes should be created.

The function modifies the original tree directly and returns `None`.

An empty tree should be handled without performing any operations.

## 3. Example

Consider the following binary tree:

```text
          10
         /  \
        5    15
       / \     \
      3   7     20
         /
        6
```

### Preorder Traversal

Preorder traversal follows:

**Root → Left → Right**

The traversal sequence is:

```text
10 → 5 → 3 → 7 → 6 → 15 → 20
```

### Expected Flattened Structure

After applying the flattening operation, the tree becomes:

```text
10
  \
   5
    \
     3
      \
       7
        \
         6
          \
           15
             \
              20
```

In the resulting structure:

- All left pointers are `None`.
- All nodes are connected using right pointers.
- The original preorder sequence is preserved.
- The original node objects are reused.

The resulting structure behaves like a singly linked list.

## 4. Function Contract

Before implementing the algorithm, it is important to define the expected behavior of the function.

### Input

The function accepts:

- The root node of a binary tree.
- `None` when the tree is empty.

### Output

The function returns `None`.

### Expected Behavior

The function must:

- Modify the original binary tree.
- Preserve every original node.
- Preserve the value stored in every node.
- Arrange nodes according to preorder traversal.
- Set every left pointer to `None`.
- Connect consecutive preorder nodes using right pointers.

### Important Note

The function does not create a new tree or return a new root.

It modifies the existing tree through the original root reference.

Correct function call:

```python
flatten(root)
```

Incorrect function call:

```python
root = flatten(root)
```

The second approach is incorrect because the function returns `None`. Assigning that return value to `root` would overwrite the original root reference.

The algorithm assumes a valid binary tree without cycles or shared child nodes.

## 5. Concepts Used

This problem combines several important concepts from binary trees and linked lists.

### 5.1 Binary Tree

A binary tree is a hierarchical structure where each node contains a value and references to its left and right children.

Example:

```text
        1
       / \
      2   3
```

### 5.2 Preorder Traversal

Preorder traversal processes nodes in this order:

1. Visit the root.
2. Traverse the left subtree.
3. Traverse the right subtree.

For example:

```text
        1
       / \
      2   3
     / \
    4   5
```

Preorder output:

```text
1 → 2 → 4 → 5 → 3
```

The flattened tree must follow exactly this sequence.

### 5.3 Pointer Manipulation

Pointer manipulation means changing the references between nodes without creating replacement nodes.

In this problem, the following references are modified:

- `current.left`
- `current.right`
- `tail.right`

These changes gradually transform the tree into a linked chain.

### 5.4 In-Place Algorithm

An in-place algorithm modifies the input data structure directly.

The flattening algorithm does not require a separate linked-list structure or an additional collection of tree nodes.

Its auxiliary space complexity is O(1).

## 6. Main Idea: Rewire the Pointers

The central idea is to place the original right subtree after the left subtree.

Consider a node with both left and right children:

```text
         current
         /     \
       LEFT    RIGHT
```

Preorder traversal requires:

```text
current → LEFT subtree → RIGHT subtree
```

Therefore, the original right subtree must be moved after the left subtree.

The algorithm performs the following operations:

1. Check whether the current node has a left child.
2. Find the rightmost node in the left subtree's right-pointer chain.
3. Preserve the original right subtree.
4. Attach the original right subtree to the identified node.
5. Move the left subtree to the current node's right pointer.
6. Set the current node's left pointer to `None`.
7. Continue processing the next node through the right pointer.

This process is repeated until all nodes are connected in preorder order.

## 7. Important Pointer Operations

The following code performs the main pointer-rewiring operation:

```python
tail = current.left

while tail.right is not None:
    tail = tail.right

tail.right = current.right

current.right = current.left

current.left = None
```

### Explanation of Each Statement

**Step 1: Start from the left child**

```python
tail = current.left
```

The left subtree must appear before the original right subtree in preorder.

Therefore, we begin searching from the left child.

**Step 2: Find the rightmost node**

```python
while tail.right is not None:
    tail = tail.right
```

This loop follows right pointers until it reaches a node whose right pointer is `None`.

This node becomes the attachment point for the original right subtree.

**Step 3: Attach the original right subtree**

```python
tail.right = current.right
```

The original right subtree is connected after the left subtree's right-pointer chain.

**Step 4: Move the left subtree**

```python
current.right = current.left
```

The left subtree becomes the right subtree of the current node.

**Step 5: Remove the left connection**

```python
current.left = None
```

This ensures that the current node no longer has a left child.

### Important Observation

The attachment node is not necessarily a leaf node.

It is the last node reached by following right pointers from the current node's left child.

It may still have a left child. That left child will be moved into the correct position when the algorithm processes that node later.

## 8. Detailed Dry Run of the Example

Consider the original tree:

```text
          10
         /  \
        5    15
       / \     \
      3   7     20
         /
        6
```

The expected preorder sequence is:

```text
10 → 5 → 3 → 7 → 6 → 15 → 20
```

### Step 1: Process Node 10

The current node is `10`.

Its left child is `5`, and its right child is `15`.

Find the rightmost node by following right pointers from node `5`:

```text
5 → 7
```

Node `7` has no right child.

Therefore:

```python
tail.right = current.right
```

becomes:

```python
7.right = 15
```

Next:

```python
current.right = current.left
current.left = None
```

Node `5` becomes the right child of node `10`.

Intermediate structure:

```text
10
  \
   5
  / \
 3   7
    / \
   6   15
         \
          20
```

### Step 2: Process Node 5

Move to node `5`.

Its left child is `3`, and its right subtree begins at `7`.

Node `3` has no right child.

Therefore:

```python
3.right = 7
```

Next, move node `3` to the right of node `5` and clear the left pointer.

Intermediate structure:

```text
10
  \
   5
    \
     3
      \
       7
      / \
     6   15
           \
            20
```

### Step 3: Process Node 3

Node `3` does not have a left child.

No pointer changes are necessary.

Move to node `7`.

### Step 4: Process Node 7

Node `7` has a left child `6`.

Its current right subtree begins at node `15`.

Node `6` has no right child.

Therefore:

```python
6.right = 15
```

Next, move node `6` to the right of node `7` and clear the left pointer.

Intermediate structure:

```text
10
  \
   5
    \
     3
      \
       7
        \
         6
          \
           15
             \
              20
```

### Step 5: Process Remaining Nodes

The remaining nodes are:

- 6
- 15
- 20

None of these nodes has a left child.

The algorithm simply moves through their right pointers.

### Final Result

```text
10 → 5 → 3 → 7 → 6 → 15 → 20
```

All left pointers are now `None`.

## 9. Attachment Point Analysis

The attachment point is the node where the original right subtree is connected.

For the Day 47 example:

| Current node | Left subtree starts at | Attachment point | Original right subtree |
|---|---:|---:|---:|
| 10 | 5 | 7 | 15 |
| 5 | 3 | 3 | 7 |
| 7 | 6 | 6 | 15 |

The attachment operations preserve the required preorder sequence.

The attachment point does not always have to be the final node in the left subtree's preorder traversal.

It only needs to be the rightmost node in the current left subtree's right-pointer chain. Any remaining left child at that node is processed later.

## 10. Why Preserve the Original Right Subtree?

Consider the following structure:

```text
        1
       / \
      2   5
```

Before modifying the tree:

```python
current.right = current.left
```

the current node's right pointer is the direct connection to node `5`.

If we overwrite this connection immediately, node `5` and its descendants may become unreachable from the root.

Therefore, the original right subtree must first be connected to a safe location.

The correct sequence is:

```python
tail.right = current.right

current.right = current.left

current.left = None
```

This is an important principle in pointer-based algorithms:

**Preserve the remaining structure before overwriting a pointer.**

The same principle is useful in linked-list reversal, node deletion, and other pointer-rewiring problems.

## 11. Loop Invariant

A loop invariant describes a condition that remains true during every iteration of an algorithm.

Before processing each `current` node:

1. All nodes already processed form the correct preorder prefix.
2. Every processed node has its left pointer set to `None`.
3. The unprocessed nodes remain reachable from the current node.
4. The remaining nodes will be placed after the processed prefix in preorder order.

When the current node has a left subtree, the algorithm places that subtree before the original right subtree.

This preserves the required preorder sequence.

The algorithm continues until `current` becomes `None`.

At that point, all nodes have been processed.

## 12. Complete Algorithm

The algorithm can be represented using the following pseudocode:

```text
FUNCTION flatten(root)

    current = root

    WHILE current is not None

        IF current.left is not None

            tail = current.left

            WHILE tail.right is not None
                tail = tail.right

            tail.right = current.right

            current.right = current.left

            current.left = None

        current = current.right

    RETURN None
```

### Algorithm Explanation

- Initialize the current pointer with the root.
- Check whether the current node has a left subtree.
- Find the attachment point in the left subtree.
- Attach the original right subtree at that point.
- Move the left subtree to the right.
- Clear the left pointer.
- Continue through the right chain.
- Stop when all nodes have been processed.

The algorithm modifies the original tree without creating additional tree nodes.

## 13. Stack-Based Alternative

Another approach uses a stack to store nodes in preorder order.

### Steps

1. Initialize an empty stack.
2. Push the root node if it is not `None`.
3. Pop the next node from the stack.
4. Save its original right and left children.
5. Push the right child first.
6. Push the left child second.
7. Connect the previously processed node to the current node using its right pointer.
8. Set the current node's left pointer to `None`.
9. Repeat until the stack is empty.

### Why Push Right Before Left?

A stack follows the Last In, First Out (LIFO) principle.

Therefore, the left child must be pushed after the right child so that it is processed first.

This produces preorder traversal:

```text
Root → Left → Right
```

### Complexity of the Stack Approach

- Time complexity: O(n).
- Auxiliary space complexity: O(n) in the worst case.

The pointer-rewiring method is preferable when constant auxiliary space is required.

## 14. Test Cases and Verification

Testing is important to ensure that the flattened tree satisfies all structural requirements.

### Test Case 1: Normal Binary Tree

Input:

```text
          10
         /  \
        5    15
       / \     \
      3   7     20
         /
        6
```

Expected:

```text
10 → 5 → 3 → 7 → 6 → 15 → 20
```

Expected result: Pass.

### Test Case 2: Empty Tree

Input:

```python
root = None
```

Expected behavior:

- No exception.
- No processing required.
- Function returns `None`.

Expected result: Pass.

### Test Case 3: Single Node

Input:

```text
    7
```

Expected flattened structure:

```text
7
```

The node has no left or right child.

Expected result: Pass.

### Test Case 4: Left-Only Tree

Input:

```text
        4
       /
      3
     /
    2
   /
  1
```

Expected flattened chain:

```text
4 → 3 → 2 → 1
```

Expected result: Pass.

### Test Case 5: Right-Only Tree

Input:

```text
1
 \
  2
   \
    3
```

Expected flattened chain:

```text
1 → 2 → 3
```

Since every node already has a `None` left pointer, no structural changes are needed.

Expected result: Pass.

### Test Case 6: Repeated Values

Input:

```text
       5
      / \
     5   5
```

Expected flattened chain:

```text
5 → 5 → 5
```

The test must verify node identity, not only node values, because repeated values cannot distinguish individual nodes.

Expected result: Pass.

### Test Case 7: Repeated Flattening

Flatten the same tree twice.

The second operation should not change the already flattened structure.

Expected result: Pass.

### Structural Verification

A correct test should verify:

- Every original node is present.
- No original node is missing.
- No node appears more than once.
- The order matches the original preorder traversal.
- Every left pointer is `None`.
- The chain ends when the final node's right pointer is `None`.

The implementation captures the original node objects before flattening and checks their identities after the transformation.

## 15. Complexity Analysis

Let `n` represent the total number of nodes in the binary tree.

### Time Complexity: O(n)

The outer loop processes nodes along the resulting right-linked structure.

The attachment-point searches follow right pointers within left subtrees.

Across the complete transformation, the total work performed by these searches is linear.

Therefore, the overall time complexity is:

**O(n)**

The nested loop does not automatically imply O(n²). Complexity must be evaluated across the complete execution rather than by simply multiplying the maximum lengths of the loops.

### Auxiliary Space Complexity: O(1)

The pointer-rewiring algorithm uses only a fixed number of additional variables:

- `current`
- `tail`
- `original_right`

No additional stack, queue, or collection is required by the flattening operation.

Therefore, the auxiliary space complexity is:

**O(1)**

### Additional Memory

The optional attachment log and testing helper functions may use additional memory.

However, these are not required by the actual flattening algorithm.

### Complexity Comparison

| Approach | Time Complexity | Auxiliary Space |
|---|---|---|
| Pointer Rewiring | O(n) | O(1) |
| Stack-Based | O(n) | O(n) |

The pointer-rewiring method is space-efficient because it modifies the existing tree directly.

## 16. Common Mistakes

| Mistake | Explanation |
|---|---|
| Overwriting `current.right` too early | The original right subtree can become unreachable. |
| Forgetting `current.left = None` | The result will not be a valid right-only chain. |
| Creating new nodes | The requirement is to reuse the original node objects. |
| Using inorder traversal | The resulting sequence will not match preorder. |
| Assuming the attachment point must be a leaf | The attachment node may still have a left child. |
| Assigning `root = flatten(root)` | The root reference becomes `None` because the function returns `None`. |
| Checking only node values | Repeated values can hide missing or duplicated node objects. |
| Forgetting to preserve the original right subtree | Some nodes may become disconnected from the root. |

## 17. Real-World Applications

The flattening operation demonstrates techniques that are useful in several software engineering applications.

### 17.1 Tree-to-List Conversion

Hierarchical data can be transformed into a sequential structure for processing or reporting.

### 17.2 Memory-Efficient Transformations

In-place operations can reduce the need for additional data structures when modifying existing objects.

### 17.3 Data Structure Manipulation

The problem develops practical skills in changing node references safely.

### 17.4 Serialization and Sequential Processing

A flattened representation can make certain sequential processing operations easier, although it does not preserve the original tree hierarchy in its modified form.

### 17.5 Destructive Data Transformations

The operation is destructive because the original tree connections are changed.

Any other part of a program holding references to these nodes will observe the modified structure.

If the original hierarchy must remain available, a separate representation should be created instead of modifying the original tree.

## 18. Key Takeaways

- Flattening transforms a binary tree into a right-linked chain.
- The required order is preorder: Root → Left → Right.
- Every node's left pointer must become `None`.
- Every original node must be reused exactly once.
- The original right subtree must be preserved before pointer rewiring.
- The attachment point is found by following right pointers from the left child.
- The attachment point does not necessarily have to be a leaf.
- The pointer-rewiring algorithm uses O(1) auxiliary space.
- The overall time complexity is O(n).
- The stack-based alternative uses O(n) worst-case auxiliary space.
- The operation modifies the original tree and is therefore destructive.

**Final Understanding:**

The most important lesson from Day 47 is learning how to rearrange existing node connections without losing access to unprocessed nodes. Preserving the original right subtree before changing the current node's right pointer is the key to maintaining the correct preorder sequence.