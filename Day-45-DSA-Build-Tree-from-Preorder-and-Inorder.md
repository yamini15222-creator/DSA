# Day 45 – Construct Binary Tree from Preorder and Inorder Traversal

## 1. Introduction

A Binary Tree is a hierarchical data structure in which each node can have at most two children:

- Left child
- Right child

In this problem, we are given two traversal arrays of a binary tree:

1. Preorder Traversal
2. Inorder Traversal

Our task is to reconstruct the original binary tree using these two arrays.

This problem demonstrates how traversal sequences can be used to rebuild a tree structure. It also helps us understand recursion, tree relationships, hashmap optimization, and depth-first search.

**Topic:** Construct Binary Tree from Preorder and Inorder Traversal

**Data Structure:** Binary Tree

**Main Techniques:** Recursion, Hashmap, Depth-First Search

**Difficulty:** Medium

---

## 2. Problem Statement

Given two integer arrays:

- `preorder`, representing the preorder traversal of a binary tree.
- `inorder`, representing the inorder traversal of the same binary tree.

Construct and return the original binary tree.

Assume that all node values are unique.

### Function Definition

```python
def build_tree(preorder, inorder):
    pass
```

### Input

Two arrays containing the preorder and inorder traversals.

### Output

The root node of the reconstructed binary tree.

### Conditions

- Both arrays must have the same length.
- Both arrays must contain the same values.
- All node values must be unique.
- An empty input should return `None`.
- Inconsistent traversal sequences should raise a `ValueError`.

---

## 3. Understanding Tree Traversals

### 3.1 Preorder Traversal

Preorder follows:

**Root → Left → Right**

Example:

```text
          10
         /  \
        5    15
       / \     \
      3   7     18
```

Preorder output:

```python
[10, 5, 3, 7, 15, 18]
```

Explanation:

1. Visit root 10.
2. Visit left child 5.
3. Visit 5's left child 3.
4. Visit 5's right child 7.
5. Visit right child 15.
6. Visit 15's right child 18.

### 3.2 Inorder Traversal

Inorder follows:

**Left → Root → Right**

For the same tree:

```text
          10
         /  \
        5    15
       / \     \
      3   7     18
```

Inorder output:

```python
[3, 5, 7, 10, 15, 18]
```

Explanation:

1. Visit the leftmost node 3.
2. Visit node 5.
3. Visit node 7.
4. Visit root 10.
5. Visit node 15.
6. Visit node 18.

---

## 4. Main Observation

The most important observation is:

- Preorder always gives us the root of the current subtree first.
- Inorder tells us which nodes belong to the left subtree and which belong to the right subtree.

For example:

```python
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
```

The first preorder element is `3`. Therefore, `3` is the root.

In inorder:

```python
[9, 3, 15, 20, 7]
```

The root divides the array into:

Left subtree:

```python
[9]
```

Right subtree:

```python
[15, 20, 7]
```

This allows us to construct the left and right subtrees recursively.

---

## 5. Example 1 – Main Problem Example

### Input

```python
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
```

### Step 1: Find the Root

The first element in preorder is `3`.

```text
Root = 3
```

### Step 2: Divide Inorder

```text
Inorder = [9, 3, 15, 20, 7]
```

Left of root:

```python
[9]
```

Right of root:

```python
[15, 20, 7]
```

### Step 3: Construct Left Subtree

The next preorder element is `9`.

Since it belongs to the left subtree, it becomes the left child of 3.

### Step 4: Construct Right Subtree

The next preorder element is `20`.

In the right subtree's inorder section:

```python
[15, 20, 7]
```

The value 20 becomes the right child of 3.

Its left subtree contains 15, and its right subtree contains 7.

### Final Tree

```text
          3
         / \
        9   20
           /  \
          15   7
```

### Expected Output

```text
Root: 3
Left child: 9
Right child: 20
```

Generated preorder:

```python
[3, 9, 20, 15, 7]
```

Generated inorder:

```python
[9, 3, 15, 20, 7]
```

Both traversals match the original input.

---

## 6. Algorithm Explanation

We use recursion and a hashmap to construct the tree efficiently.

### Step 1: Validate Input

Check whether both arrays have equal lengths.

If the lengths are different, raise a `ValueError`.

### Step 2: Handle Empty Input

If both arrays are empty, return `None`.

### Step 3: Check Unique Values

Since the algorithm uses values as hashmap keys, duplicate values are not supported.

### Step 4: Check Matching Values

Both arrays must contain exactly the same values.

### Step 5: Create a Hashmap

Store each inorder value and its index.

Example:

```python
inorder = [9, 3, 15, 20, 7]
```

Hashmap:

```python
{
    9: 0,
    3: 1,
    15: 2,
    20: 3,
    7: 4
}
```

This helps us find the root position in O(1) average time.

### Step 6: Initialize Preorder Index

```python
pre_index = 0
```

This variable identifies the next root to process.

### Step 7: Recursive Function

Create a recursive function:

```python
def build(left, right):
```

The parameters represent the current valid inorder index range.

If:

```python
left > right
```

there are no nodes in that section, so return `None`.

### Step 8: Select the Root

Get the next value from preorder:

```python
value = preorder[pre_index]
```

Find its inorder position:

```python
middle = positions[value]
```

### Step 9: Validate the Root Position

The root must belong to the current inorder range.

If it does not, the traversal order is inconsistent.

### Step 10: Create the Node

```python
node = TreeNode(value)
```

### Step 11: Build Left and Right Subtrees

```python
node.left = build(left, middle - 1)
node.right = build(middle + 1, right)
```

The left subtree must be built first because the preorder traversal visits the left subtree before the right subtree.

### Step 12: Return the Root

After both recursive calls finish:

```python
return node
```

The completed tree is returned to the caller.

---

## 7. Dry Run – Recursive Execution

Input:

```python
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
```

Initial state:

```text
pre_index = 0
```

Hashmap:

```python
{
    9: 0,
    3: 1,
    15: 2,
    20: 3,
    7: 4
}
```

### Recursive Calls

| Call | Inorder Range | Root | Root Index |
|---|---|---|---|
| 1 | 0 to 4 | 3 | 1 |
| 2 | 0 to 0 | 9 | 0 |
| 3 | 2 to 4 | 20 | 3 |
| 4 | 2 to 2 | 15 | 2 |
| 5 | 4 to 4 | 7 | 4 |

### Execution Order

1. Select 3 as root.
2. Construct its left subtree using 9.
3. Construct its right subtree using 20.
4. Construct 20's left subtree using 15.
5. Construct 20's right subtree using 7.

At the end:

```text
pre_index = 5
```

All five preorder values have been consumed.

### Final Structure

```text
          3
         / \
        9   20
           /  \
          15   7
```

---

## 8. Why Do We Build the Left Subtree First?

This is a very important concept.

Preorder traversal follows:

```text
Root → Left → Right
```

The preorder array stores values in exactly this order.

For example:

```python
preorder = [3, 9, 20, 15, 7]
```

After selecting root 3, the next preorder value is 9.

Therefore, we must construct the left subtree before attempting to construct the right subtree.

If we construct the right subtree first, we may consume the wrong preorder values.

**Remember:** The order of recursive calls must follow the order of the traversal being consumed.

---

## 9. Why Use a Hashmap?

Without a hashmap, we may repeatedly search the inorder array to find the root position.

This can require O(n) time for each search.

With a hashmap:

```python
positions = {
    value: index
    for index, value in enumerate(inorder)
}
```

We can retrieve the root position in O(1) average time.

This reduces the overall construction time to O(n) average time.

---

## 10. Implementation Code Structure

The implementation contains the following functions:

| Function | Responsibility |
|---|---|
| `TreeNode()` | Creates a binary tree node. |
| `build_tree()` | Constructs the binary tree. |
| `preorder_values()` | Generates preorder traversal. |
| `inorder_values()` | Generates inorder traversal. |
| `print_tree_details()` | Displays root and immediate children. |
| `run_tests()` | Executes test cases. |

The main construction logic is implemented using a recursive helper function inside `build_tree()`.

---

## 11. Additional Practice Examples

### Example 2 – Balanced Binary Tree

Input:

```python
preorder = [10, 5, 3, 7, 15, 12, 18]
inorder = [3, 5, 7, 10, 12, 15, 18]
```

Expected tree:

```text
          10
         /  \
        5    15
       / \   / \
      3   7 12 18
```

### Example 3 – Non-BST Binary Tree

Input:

```python
preorder = [1, 9, 2]
inorder = [9, 1, 2]
```

Expected tree:

```text
       1
      / \
     9   2
```

This example confirms that the algorithm does not depend on BST ordering.

### Example 4 – Left-Skewed Tree

Input:

```python
preorder = [4, 3, 2, 1]
inorder = [1, 2, 3, 4]
```

Expected tree:

```text
        4
       /
      3
     /
    2
   /
  1
```

### Example 5 – Right-Skewed Tree

Input:

```python
preorder = [1, 2, 3, 4]
inorder = [1, 2, 3, 4]
```

Expected tree:

```text
    1
     \
      2
       \
        3
         \
          4
```

---

## 12. Input Validation and Edge Cases

A reliable implementation must handle invalid input correctly.

| Case | Input | Expected Behavior |
|---|---|---|
| Empty tree | `[], []` | Return `None` |
| Single node | `[7], [7]` | Construct one node |
| Unequal lengths | `[1, 2], [1]` | Raise `ValueError` |
| Different values | `[1, 2], [1, 3]` | Raise `ValueError` |
| Duplicate values | `[1, 1], [1, 1]` | Raise `ValueError` |
| Inconsistent order | `[1, 2, 3], [3, 1, 2]` | Raise `ValueError` |

### Why Is the Inconsistent Order Invalid?

Consider:

```python
preorder = [1, 2, 3]
inorder = [3, 1, 2]
```

Preorder identifies 1 as the root.

Inorder says 3 belongs to the left subtree of 1.

However, the next preorder value is 2, which belongs to the right subtree according to inorder.

The recursive boundary check detects this inconsistency and raises a `ValueError`.

---

## 13. Time and Space Complexity

Let `n` represent the number of nodes.

### Time Complexity

| Operation | Complexity |
|---|---|
| Validate traversal lengths | O(1) |
| Validate unique values | O(n) |
| Validate matching values | O(n) average |
| Build hashmap | O(n) |
| Find each root position | O(1) average |
| Construct all nodes | O(n) |
| **Overall** | **O(n) average** |

Each node is created exactly once, and each preorder value is consumed once.

### Space Complexity

| Component | Complexity |
|---|---|
| Hashmap | O(n) |
| Validation sets | O(n) |
| Recursion stack | O(h) |
| Constructed tree | O(n) |

Here, `h` is the height of the tree.

The auxiliary space is O(n), including the hashmap and validation sets.

The output tree itself requires O(n) space.

**Important:** A highly skewed tree can create recursion depth O(n). For very large trees, Python may reach its recursion limit; an iterative construction can be considered.

---

## 14. Common Mistakes

### Mistake 1: Selecting the Wrong Root

The first unprocessed preorder value must be selected as the current root.

### Mistake 2: Building the Right Subtree First

Preorder visits the left subtree before the right subtree.

Therefore, the left recursive call must come first.

### Mistake 3: Forgetting to Update the Index

The shared preorder index must advance after selecting a root.

Otherwise, the same value may be reused.

### Mistake 4: Using Incorrect Inorder Boundaries

For a root at index `middle`:

- Left subtree: `left` to `middle - 1`
- Right subtree: `middle + 1` to `right`

### Mistake 5: Using Values to Decide Left and Right

The algorithm must use the root's inorder position, not numeric comparisons.

An ordinary binary tree does not have to follow BST ordering.

### Mistake 6: Ignoring Duplicate Values

The hashmap approach assumes unique values. Duplicate values make the position lookup ambiguous.

### Mistake 7: Forgetting Empty Subtrees

When `left > right`, return `None`.

This is the base case that stops recursion.

---

## 15. Testing and Verification

After constructing a tree, we should verify that the generated traversals match the original arrays.

### Preorder Verification

```python
assert preorder_values(root) == preorder
```

### Inorder Verification

```python
assert inorder_values(root) == inorder
```

If both conditions are true, the constructed tree reproduces the supplied traversals.

The implementation also tests:

- Balanced tree construction.
- Empty tree.
- Single-node tree.
- Left-skewed tree.
- Invalid traversal order.
- Different input values.
- Duplicate values.
- Unequal traversal lengths.

---

## 16. Real-World Applications

Tree reconstruction techniques are useful in several areas:

1. **Compiler Design:** Tree structures are used to represent expressions and program syntax.
2. **Expression Processing:** Expression trees represent mathematical operations and their relationships.
3. **Data Serialization:** Tree traversal sequences can help store and reconstruct tree structures when sufficient information is available.
4. **Database Systems:** Tree structures are used in indexing and hierarchical data representation.
5. **File Systems:** Directories and files naturally form hierarchical tree structures.
6. **Software Engineering:** Abstract Syntax Trees represent source-code structure.

---

## 17. Possible Improvements

The current solution can be extended in several ways:

- Implement iterative tree construction to avoid recursion-depth limitations.
- Support duplicate values by using additional stable node identifiers or other disambiguating information.
- Implement tree construction from inorder and postorder traversals.
- Add level-order traversal to display the completed tree.
- Add visual tree representation.

---

## 18. Key Takeaways

- Preorder traversal identifies the root node.
- Inorder traversal identifies the left and right subtrees.
- A hashmap makes root-position lookup efficient.
- Recursion constructs each subtree.
- A shared preorder index tracks the next root.
- Left subtree construction must happen before right subtree construction.
- Unique node values are required by this implementation.
- The average time complexity is O(n).

**Day 45 Completed – Construct Binary Tree from Preorder and Inorder Traversal.**