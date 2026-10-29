\# Day 42 DSA: Root-to-Leaf Path Sum



\## 1. Problem Statement



Given the root of a binary tree and a target sum, determine whether the tree contains a root-to-leaf path whose node values add up to the target.



A leaf is a node with no left or right child.



The function returns `True` if a matching root-to-leaf path exists; otherwise, it returns `False`.



Negative values and duplicate values are allowed.



\## 2. Original Lesson Example



```text

&#x20;          5

&#x20;         / \\

&#x20;        4   8

&#x20;       /   / \\

&#x20;      11  13  4

&#x20;     / \\      \\

&#x20;    7   2      1





For target 22, the answer is True.



Path: 5 → 4 → 11 → 2



Sum: 5 + 4 + 11 + 2 = 22



For target 9, the answer is False. Although 5 + 4 = 9, node 4 is not a leaf.



Other results:

\- Target 22: True

\- Target 26: True (5 → 8 → 13)

\- Target 9: False

\- Target 18: True (5 → 8 → 4 → 1)

3\. Implementation Code

Save the Python implementation separately as day42\_path\_sum.py.

class TreeNode:    def \_\_init\_\_(self, value, left=None, right=None):        self.value = value        self.left = left        self.right = rightdef has\_path\_sum(root, target):    if root is None:        return False    remaining = target - root.value    if root.left is None and root.right is None:        return remaining == 0    return (        has\_path\_sum(root.left, remaining)        or has\_path\_sum(root.right, remaining)    )# Original lesson treeroot = TreeNode(    5,    TreeNode(        4,        left=TreeNode(11, TreeNode(7), TreeNode(2)),    ),    TreeNode(        8,        TreeNode(13),        TreeNode(4, right=TreeNode(1)),    ),)print(has\_path\_sum(root, 22))  # Trueprint(has\_path\_sum(root, 26))  # Trueprint(has\_path\_sum(root, 9))   # Falseprint(has\_path\_sum(root, 18))  # True







4\. How the Algorithm Works

At each node, subtract its value from the remaining target.

1\. If the node is missing, return False.

2\. If the node is a leaf, return whether the remaining target is zero.

3\. Otherwise, check the left and right subtrees using or.

A leaf must have both children missing. A missing child is not a valid endpoint.

5\. Trace for Target 22

Node	Target received	Remaining after subtraction	Decision

5	22	17	Explore children

4	17	13	Explore children

11	13	2	Explore children

7	2	-5	Leaf: False

2	2	0	Leaf: True



The successful result travels back through nodes 11, 4, and 5.



Each recursive call has its own remaining target, so exploring one branch does not change the state of its sibling.

6\. Negative Values and Zero Remaining

Negative values are allowed, so a negative remaining target does not automatically mean failure.



Example:

&#x20;   5

&#x20;  /

&#x20;-3





For target 2, the path 5 → -3 sums to 2, so the result is True.



Do not reject a path merely because its remaining target is negative.



Zero remaining is not enough by itself. Success is confirmed only at a leaf after processing that leaf's value.

7\. Tests to Run

Run these tests with the TreeNode, has\_path\_sum, and original lesson root defined.

assert has\_path\_sum(None, 0) is Falseassert has\_path\_sum(TreeNode(7), 7) is Trueassert has\_path\_sum(TreeNode(7), 0) is Falseassert has\_path\_sum(root, 22) is Trueassert has\_path\_sum(root, 26) is Trueassert has\_path\_sum(root, 9) is False# Negative remainder can still lead to success.negative\_path = TreeNode(5, left=TreeNode(-3))assert has\_path\_sum(negative\_path, 2) is True# Matching an internal node is insufficient.internal\_match = TreeNode(5, left=TreeNode(2))assert has\_path\_sum(internal\_match, 5) is False# Zero-valued nodes are allowed.zero\_path = TreeNode(5, left=TreeNode(0))assert has\_path\_sum(zero\_path, 5) is True# A single zero node is a valid nonempty path.assert has\_path\_sum(TreeNode(0), 0) is True







8\. Assignment: Find a Matching Route

Build this tree:

&#x20;          10

&#x20;         /  \\

&#x20;        5   -3

&#x20;       / \\    \\

&#x20;      3   2    11

&#x20;     /     \\

&#x20;   -2       1





Its root-to-leaf paths are:

10 → 5 → 3 → -2 = 16

10 → 5 → 2 → 1  = 18

10 → -3 → 11    = 18





Implement has\_path\_sum() independently.

Expected Results

Target	Result

16	True

18	True

15	False

7	False

100	False



Assignment Tree Construction and Tests

assignment\_root = TreeNode(10)assignment\_root.left = TreeNode(5)assignment\_root.right = TreeNode(-3)assignment\_root.left.left = TreeNode(3)assignment\_root.left.right = TreeNode(2)assignment\_root.right.right = TreeNode(11)assignment\_root.left.left.left = TreeNode(-2)assignment\_root.left.right.right = TreeNode(1)assert has\_path\_sum(assignment\_root, 16) is Trueassert has\_path\_sum(assignment\_root, 18) is Trueassert has\_path\_sum(assignment\_root, 15) is Falseassert has\_path\_sum(assignment\_root, 7) is Falseassert has\_path\_sum(assignment\_root, 100) is False







9\. Trace for Target 16

The matching path is 10 → 5 → 3 → -2.

Node	Remaining target calculation	Remaining

10	16 - 10	6

5	6 - 5	1

3	1 - 3	-2

\-2	-2 - (-2)	0



The remaining target becomes zero at leaf -2. Therefore, the result is True.

10\. Why Target 7 Returns False

A valid path must begin at the root and end at a leaf.



No complete root-to-leaf path in the assignment tree sums to 7, so the function returns False.



A matching sum at an internal node is not enough.

11\. Warm-Up Question

Consider this tree:

&#x20;   4

&#x20;  /

&#x20;-4





For target 0, the result is True.



Success is confirmed at leaf -4, because 4 + (-4) = 0.

12\. Function Contract

Input: A binary-tree root and an integer target sum.



Output: A boolean indicating whether a root-to-leaf path equals the target.

\- An empty tree returns False, even when the target is zero.

\- Negative values and duplicate values are supported.

\- A matching sum at an internal node does not count.

\- A single-node tree is valid when its value equals the target.

\- The tree is not modified.

13\. Iterative DFS Extension

The iterative version uses a stack of (node, remaining\_target) pairs.



The remaining target represents the amount needed before processing that node. Pop the pair, subtract the node's value, check for a leaf, and then push children with the updated remainder.

def has\_path\_sum\_iterative(root, target):    if root is None:        return False    stack = \[(root, target)]    while stack:        node, remaining\_target = stack.pop()        remaining = remaining\_target - node.value        if node.left is None and node.right is None:            if remaining == 0:                return True            continue        if node.right is not None:            stack.append((node.right, remaining))        if node.left is not None:            stack.append((node.left, remaining))    return False







Example tests:

assert has\_path\_sum\_iterative(root, 22) is Trueassert has\_path\_sum\_iterative(root, 26) is Trueassert has\_path\_sum\_iterative(root, 9) is Falseassert has\_path\_sum\_iterative(assignment\_root, 16) is Trueassert has\_path\_sum\_iterative(assignment\_root, 18) is Trueassert has\_path\_sum\_iterative(assignment\_root, 15) is Falseassert has\_path\_sum\_iterative(None, 0) is False







14\. Institute-Level Discussion

The function contract defines the input, output, and path rules. The leaf check is necessary because the path must end at a leaf. Reaching the target at an internal node is not enough.



Day 41 — Maximum Path Sum: A path may start and end anywhere in the tree, and the goal is to find the largest sum.



Day 42 — Root-to-Leaf Path Sum: A path must start at the root and end at a leaf, and the goal is to check for an exact target. The output is a boolean.



Do not use Day 41's max(0, gain) rule here, because negative values may be necessary to complete the target sum.

15\. Corporate-Level Discussion

Recursive DFS is concise and suitable for trees of ordinary depth. A very deep tree may exceed Python's recursion limit, in which case iterative DFS avoids relying on recursive calls.



Keep each path's remaining target separate.



Also clarify the required output: a boolean, one matching path, all matching paths, or a count. These requirements need different output handling.

16\. Client-Level Discussion

Define what counts as a completed route. In this problem, completion means reaching a structural leaf. In another application, a designated terminal state may not be the same as a structural leaf.



For monetary values, use an exact representation such as integer minor units (for example, paise) instead of relying on approximate floating-point equality.

17\. Complexity Analysis

Let n be the number of nodes and h the tree height.

\- Time: O(n) in the worst case.

\- Recursive auxiliary space: O(h) for the call stack.

\- Iterative auxiliary space: Up to O(n) in the worst case.

18\. Common Mistakes

Mistake	Why it fails

Return True whenever the remainder reaches zero	The current node may not be a leaf

Treat one missing child as a leaf	Both children must be missing

Return target == 0 for a missing node	A missing child is not a valid path endpoint

Use and between child results	Only one matching path is required

Reject every negative remainder	Negative node values can restore the target

Use Day 41's maximum-path logic	Day 42 requires a root-to-leaf path

