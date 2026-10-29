# Day 43 DSA: Path Sum II — All Root-to-Leaf Paths

## 1. Problem Statement

Yesterday, we solved the following problem:

> Does at least one matching root-to-leaf path exist?

Today, we will solve a slightly different problem:

**Return every root-to-leaf path whose sum equals the target.**

This problem uses a backtracking pattern:

**Choose → Explore → Undo**

Imagine exploring routes through rooms. You carry a notebook containing the rooms on your current route. When you reach a valid exit, take a photograph of that page. When you return to a junction, erase the room you just left before trying another route.

- The notebook is the working `path`.
- The photographs are copies saved in `results`.

## 2. Original Lesson Example

Consider the following binary tree:

```text
           5
          / \
         4   8
        /   / \
       11  13  4
      / \     / \
     7   2   5   1
```

For target `22`, there are two matching root-to-leaf paths:

```text
5 → 4 → 11 → 2 = 22
5 → 8 → 4 → 5  = 22
```

Expected output:

```python
[
    [5, 4, 11, 2],
    [5, 8, 4, 5]
]
```

Notice that the right-side node `4` has a left child `5`, which creates the second matching path.

## 3. What Changes from Day 42?

| Decision | Day 42: Path Sum | Day 43: Path Sum II |
|---|---|---|
| Output | `True` or `False` | List of matching paths |
| Stop after the first match? | Yes | No |
| Remember the current route? | Not necessary | Yes |
| Empty tree | `False` | `[]` |
| Explore both branches? | May stop early | Yes |

The path rules remain the same:

- Start at the root.
- End at a leaf.
- Follow actual tree connections.
- Match the target exactly.
- Negative values and duplicate values are allowed.

We assume a valid tree structure and return paths as lists of values in left-first DFS order.

## 4. The 80/20 Idea

At every node, perform five steps.

1. **Choose:** Append its value to the working path.
2. Subtract its value from the remaining target.
3. If it is a matching leaf, save a copy of the path.
4. Otherwise, explore its children.
5. **Undo:** Remove its value before returning.

The basic code pattern is:

```python
path.append(node.value)       # Choose

# Explore or save a result.

path.pop()                    # Undo
```

Each recursive call must leave the shared path exactly as it found it.

## 5. Define the State Before Coding

| Variable | Meaning |
|---|---|
| `node` | Current node being explored |
| `remaining` | Sum still needed before processing this node |
| `path` | Values along the current route |
| `results` | Copies of completed matching paths |

Our helper function follows this rule:

> On entry, `path` contains the route to the current node's parent. On exit, that same path is restored.

For example, when entering node `11`:

```python
path = [5, 4]
```

After choosing node `11`:

```python
path = [5, 4, 11]
```

After finishing both children and undoing node `11`:

```python
path = [5, 4]
```

This restoration keeps sibling routes separate.

## 6. Why Saving a Copy Matters

The correct approach is:

```python
results.append(path.copy())
```

This approach is usually wrong for this backtracking algorithm:

```python
results.append(path)
```

The second version stores a reference to the same working list. Later `append()` and `pop()` operations change that list, including what the saved results appear to contain.

Think of the difference as:

```text
path         → The notebook you keep editing
path.copy()  → A photograph of the notebook at that moment
```

With proper backtracking, the working path is empty when traversal finishes. If every result references the same list, the answers may incorrectly end up looking like:

```python
[[], []]
```

Using `path.copy()` preserves each matching path independently.

## 7. Complete Runnable Python Implementation

Create a file named `day43_path_sum_ii.py`.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def path_sum(root, target):
    results = []
    path = []

    def dfs(node, remaining):
        if node is None:
            return

        # Choose: add the current node.
        path.append(node.value)
        remaining -= node.value

        is_leaf = node.left is None and node.right is None

        if is_leaf:
            if remaining == 0:
                # Save an independent copy of the path.
                results.append(path.copy())
        else:
            # Explore both branches in left-first order.
            dfs(node.left, remaining)
            dfs(node.right, remaining)

        # Undo: restore the working path.
        path.pop()

    dfs(root, target)
    return results


# Build the original lesson tree.
root = TreeNode(
    5,
    left=TreeNode(
        4,
        left=TreeNode(
            11,
            left=TreeNode(7),
            right=TreeNode(2)
        )
    ),
    right=TreeNode(
        8,
        left=TreeNode(13),
        right=TreeNode(
            4,
            left=TreeNode(5),
            right=TreeNode(1)
        )
    )
)


# Print matching paths.
print("Target 22:", path_sum(root, 22))
print("Target 26:", path_sum(root, 26))
print("Target 9:", path_sum(root, 9))
print("Target 18:", path_sum(root, 18))
```

Expected output:

```text
Target 22: [[5, 4, 11, 2], [5, 8, 4, 5]]
Target 26: [[5, 8, 13]]
Target 9: []
Target 18: [[5, 8, 4, 1]]
```

The function changes its working list but does not modify the tree.

The variables `results` and `path` are created inside each public function call, so separate calls do not share saved answers.

## 8. Dry Run: Save, Undo, Continue

For target `22`, follow the first matching route.

| Action | Working path | Remaining |
|---|---|---:|
| Enter `5` | `[5]` | 17 |
| Enter left `4` | `[5, 4]` | 13 |
| Enter `11` | `[5, 4, 11]` | 2 |
| Enter `7` | `[5, 4, 11, 7]` | -5 |
| Leaf fails; pop `7` | `[5, 4, 11]` | Parent still has 2 |
| Enter `2` | `[5, 4, 11, 2]` | 0 |
| Save a copy; pop `2` | `[5, 4, 11]` | Parent still has 2 |

After finishing the left subtree, the working path returns to:

```python
[5]
```

Then the right subtree begins:

```python
[5, 8]
```

The route through `13` matches target `26`, not target `22`, so it does not get saved for target `22`.

Later, we reach:

```python
[5, 8, 4, 5]
```

Its sum is `22`, so we save another copy.

At the end:

```text
Working path: []
Saved results: [[5, 4, 11, 2], [5, 8, 4, 5]]
```

The working path can become empty without damaging the saved copies.

## 9. Why Do We Undo the List but Not the Remaining Target?

`path` is one mutable list shared by recursive calls. Appending changes that same object, so we must remove the appended value.

`remaining` is an integer parameter local to each call. This statement:

```python
remaining -= node.value
```

rebinds the local variable. It does not change the parent's integer variable.

Therefore:

```text
Shared list change     → Explicitly undo with pop().
Local integer change  → No explicit undo needed.
```

This distinction appears in many backtracking problems.

## 10. Do Not Stop After the First Result

Day 42 used logic such as:

```python
left_succeeds or right_succeeds
```

That was appropriate because only one successful path was needed.

Today, both branches must be explored.

Also, avoid returning immediately after saving a result if that return skips cleanup:

```python
# Bug: skips path.pop()
if is_leaf and remaining == 0:
    results.append(path.copy())
    return
```

Our implementation reaches `path.pop()` for every existing node, whether the path matched or failed.

## 11. Negative Values and Duplicate Routes

The negative-value rule from Day 42 still applies.

For example:

```text
5 → -3
Target = 2
```

The matching output is:

```python
[[5, -3]]
```

A negative remainder is not enough to reject a branch because negative values may later bring the sum back to the target.

Distinct node paths can also have identical value sequences.

Consider:

```text
    1
   / \
  2   2
```

For target `3`, the function returns:

```python
[[1, 2], [1, 2]]
```

These are two different root-to-leaf routes. We do not silently deduplicate them.

If a client needs to distinguish them, return node IDs alongside or instead of values.

## 12. Tests to Run

Add these tests to the implementation file after defining `path_sum()` and constructing the original lesson tree.

```python
def run_tests():
    # Empty tree
    assert path_sum(None, 0) == []

    # Single-node tree
    assert path_sum(TreeNode(7), 7) == [[7]]
    assert path_sum(TreeNode(7), 8) == []

    # Original lesson: two matching paths
    assert path_sum(root, 22) == [
        [5, 4, 11, 2],
        [5, 8, 4, 5]
    ]

    # A single matching path
    assert path_sum(root, 26) == [[5, 8, 13]]

    # No matching path
    assert path_sum(root, 9) == []

    # Negative values
    negative_tree = TreeNode(
        5,
        left=TreeNode(-3)
    )
    assert path_sum(negative_tree, 2) == [[5, -3]]

    # Zero-valued leaf
    assert path_sum(TreeNode(0), 0) == [[0]]

    # Distinct routes with identical values
    duplicate_tree = TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(2)
    )
    assert path_sum(duplicate_tree, 3) == [
        [1, 2],
        [1, 2]
    ]

    # Calls must not share results
    assert path_sum(TreeNode(0), 0) == [[0]]
    assert path_sum(None, 0) == []

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
```

Expected output:

```text
All tests passed!
```

Run the implementation and tests with:

```powershell
python day43_path_sum_ii.py
```

## 13. Assignment: Find All Matching Routes

Build the following tree from Day 42:

```text
           10
          /  \
         5   -3
        / \    \
       3   2    11
      /     \
    -2       1
```

Implement `path_sum()` independently.

### Expected outputs

For target `18`:

```python
[[10, 5, 2, 1], [10, -3, 11]]
```

For target `16`:

```python
[[10, 5, 3, -2]]
```

For target `15`:

```python
[]
```

For target `100`:

```python
[]
```

### Assignment requirements

1. Write the tree construction and function.
2. Trace every `append()` and `pop()` for target `18`.
3. Explain why `path.copy()` is required.
4. Include a test with two matching routes that share the same prefix.
5. State the complexity using the total output size.

## 14. Extension: Count Matching Paths

Implement this additional function:

```python
def count_path_sums(root, target) -> int:
    ...
```

Count matching root-to-leaf paths without storing their value lists.

For this version, sum the child counts. You can achieve `O(n)` time and `O(h)` recursive space because no output paths need copying.

Example:

```python
print(count_path_sums(root, 18))
```

Expected output for the assignment tree:

```text
2
```

## 15. Complexity Analysis

Let:

- `n` be the number of nodes.
- `h` be the tree height.
- `S` be the total number of values across all returned paths.

The complexity of `path_sum()` is:

- **Time:** `O(n + S)`
- **Auxiliary space excluding results:** `O(h)`
- **Output space:** `O(S)`

Traversal processes each node once. Every saved path must also be copied, and those copies account for `S`.

For example, returning 100 matching paths of length 20 requires storing 2,000 values. That work cannot be ignored.

In the worst case, `S` can be `O(n²)`, so a blanket claim of `O(n)` total time would be incorrect.

For `count_path_sums()`, the time complexity is `O(n)` and recursive auxiliary space is `O(h)` because it does not store the paths.

## 16. Institute-Level Discussion

Connect this problem to subsets and combinations.

The shared pattern is:

**Choose → Explore → Undo**

Explain exactly which state is shared and which state is local.

- `path` is shared and mutable.
- `results` stores independent copies.
- `remaining` is local to each recursive call.
- `node` identifies the current position in the tree.

Understanding this state management is essential for solving backtracking problems correctly.

## 17. Corporate-Level Discussion

Consider output size before promising to return every route in one response.

If a limit is introduced, report clearly whether results are truncated.

A generator can stream paths, but each yielded mutable path still needs an independent snapshot if the caller must retain it.

## 18. Client-Level Discussion

Clarify whether “all paths” means:

- Distinct node routes, or
- Distinct sequences of values.

Agree on ordering, identifiers, and whether the client actually needs the paths or only their count.

For this assignment, the function returns every valid node route as a list of values, in left-first DFS order.

### GitHub Filename

```text
Day-43-DSA-Path-Sum-II-All-Root-to-Leaf-Paths.md
```

### Final Understanding Question

Before coding, answer this:

> After saving `[5, 4, 11, 2]`, we remove `2` from the working path. Why does the saved answer still contain `2`?

**Answer:** Because `results.append(path.copy())` creates an independent copy of the list at the time it matches. Removing `2` from the working path does not modify that saved copy.
