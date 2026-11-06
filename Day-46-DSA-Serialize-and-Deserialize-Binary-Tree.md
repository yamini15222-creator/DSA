Day 46 – Serialize and Deserialize a Binary Tree
Detailed DSA Notes | Binary Trees | Preorder Traversal | Recursion
1. Introduction
A Binary Tree is a hierarchical data structure in which each node can have at most two children:
1. Left child
2. Right child
In this problem, we learn how to convert a binary tree into a string and reconstruct the original tree from that string.

This process involves two important operations:

Serialization

Serialization converts a binary tree into a string representation so that the tree can be stored, transmitted, or shared.

Deserialization

Deserialization converts the serialized string back into a binary tree with the same structure and node values.

The main objective is to ensure that the reconstructed tree is structurally identical to the original tree.
Example
Original binary tree:
          1
         / \
        2   3
           / \
          4   5


Serialized representation:
1,2,#,#,3,4,#,#,5,#,#


After deserialization, we should get the same binary tree.

2. Problem Statement
Design two functions to serialize and deserialize a binary tree.

Function 1: serialize(root)
- Accepts the root node of a binary tree.
- Converts the tree into a string.
- Uses preorder traversal.
- Represents missing children using #.
- Returns a comma-separated string.
Function 2: deserialize(data)
- Accepts a serialized string.
- Reconstructs the binary tree.
- Uses recursive tree construction.
- Returns the root of the reconstructed tree.
- Validates incomplete, invalid, and extra tokens.
Important requirements
1. Use preorder traversal.
2. Use # to represent missing children.
3. Separate tokens using commas.
4. Do not add a trailing comma.
5. Support negative integer values.
6. Support duplicate node values.
7. Reject malformed serialized input.

3. Concepts Used
The solution uses the following concepts:
Concept	Purpose
Binary Tree	Stores hierarchical node values
Recursion	Visits and reconstructs tree nodes
Preorder Traversal	Processes Root → Left → Right
Serialization	Converts tree into a string
Deserialization	Rebuilds tree from a string
List	Temporarily stores serialized tokens
String Join	Combines tokens into one string
String Split	Separates serialized tokens
nonlocal	Updates the shared token index
Exception Handling	Handles invalid input


4. Preorder Traversal
Preorder traversal is the main traversal technique used in this problem.

The order is:
1. Visit the Root.
2. Visit the Left subtree.
3. Visit the Right subtree.
It is represented as:
Root → Left → Right


Consider this tree:
          1
         / \
        2   3
           / \
          4   5


Traversal:
- First visit node 1.
- Move to the left child 2.
- Move to the right child 3.
- Visit the left child of 3, which is 4.
- Visit the right child of 3, which is 5.
Preorder output:
1, 2, 3, 4, 5


However, preorder values alone cannot identify the exact tree structure.

For that reason, we use # to represent missing children.

5. Why Do We Need the # Marker?
Consider two different binary trees.

Tree 1:
    1
   /
  2


Tree 2:
  1
   \
    2


Both trees have the same preorder traversal:
1, 2


Therefore, preorder traversal alone cannot distinguish between them.

To preserve the tree structure, we use # for every missing child.

Tree 1:
1,2,#,#,#


Tree 2:
1,#,2,#,#


Now the serialized strings are different.

This is why the missing-child marker is essential.

6. Serialization Format
The serialization format follows these rules:
Condition	Serialized Token
Node contains value 1	1
Node contains value 10	10
Negative node value	-2
Missing left child	#
Missing right child	#
Empty tree	#

All tokens are separated by commas.

For example:
1,2,#,#,3,4,#,#,5,#,#


There must not be a trailing comma.

7. Detailed Serialization Example
Consider the following binary tree:
          1
         / \
        2   3
           / \
          4   5


We apply preorder traversal.

Step 1: Visit root node 1.
1


Step 2: Move to the left child 2.
1,2


Step 3: Node 2 has no left child.

Append #.
1,2,#


Step 4: Node 2 has no right child.

Append another #.
1,2,#,#


Step 5: Move to the right child 3.
1,2,#,#,3


Step 6: Visit the left child 4.
1,2,#,#,3,4


Step 7: Node 4 has no left or right children.

Append two # markers.
1,2,#,#,3,4,#,#


Step 8: Visit the right child 5.
1,2,#,#,3,4,#,#,5


Step 9: Node 5 has no left or right children.

Append two more # markers.

Final serialized string:
1,2,#,#,3,4,#,#,5,#,#


Final result
The original binary tree has been successfully converted into a string.

8. Serialization Algorithm
The algorithm uses recursion and a list to store tokens.

Algorithm:
1. Create an empty list called tokens.
2. Define a recursive function named preorder.
3. If the current node is None, append # and return.
4. Otherwise, append the current node value as a string.
5. Recursively process the left child.
6. Recursively process the right child.
7. Join all tokens using commas.
8. Return the serialized string.
Pseudocode
FUNCTION serialize(root):

    CREATE empty tokens list

    FUNCTION preorder(node):

        IF node is NULL:
            APPEND "#" to tokens
            RETURN

        APPEND node.value to tokens

        preorder(node.left)

        preorder(node.right)

    preorder(root)

    RETURN JOIN tokens using commas



9. Deserialization
Deserialization is the reverse process of serialization.

It reconstructs a binary tree from the serialized string.

For example:
1,2,#,#,3,4,#,#,5,#,#


The deserializer reads each token and creates the corresponding node.
Important rules
- If the token is #, return None.
- Otherwise, convert the token into an integer.
- Create a new tree node.
- Rebuild its left child.
- Rebuild its right child.
- Continue until the complete tree is reconstructed.
The order must remain:
Root → Left → Right



10. Shared Cursor Using nonlocal
One important concept in this implementation is the shared index.

Consider:
index = 0def build_tree():    nonlocal index



The variable index tracks the current position in the serialized token list.

Every recursive call must access and update the same index.

For example:
Serialized tokens:

1,2,#,#,3,4,#,#,5,#,#


The index begins at zero.
Index	Token	Operation
0	1	Create root node
1	2	Create left child
2	#	Left child is empty
3	#	Right child is empty
4	3	Create right child
5	4	Create left child
6	#	Left child is empty
7	#	Right child is empty
8	5	Create right child
9	#	Left child is empty
10	#	Right child is empty

After processing all tokens, the tree is completely reconstructed.

The nonlocal keyword allows the nested function to modify the index defined in the enclosing function.

Without a shared cursor, tracking token consumption across recursive calls would require a different mechanism.

11. Detailed Deserialization Example
Serialized input:
1,2,#,#,3,4,#,#,5,#,#


Step 1: Read token 1.

Create the root node.
1


Step 2: Read token 2.

Create the left child of node 1.
    1
   /
  2


Step 3: Read #.

Node 2 has no left child.

Step 4: Read another #.

Node 2 has no right child.

Step 5: Read token 3.

Create the right child of node 1.
    1
   / \
  2   3


Step 6: Read token 4.

Create the left child of node 3.

Step 7: Read two # markers.

Node 4 has no children.

Step 8: Read token 5.

Create the right child of node 3.

Step 9: Read two # markers.

Node 5 has no children.

Final reconstructed tree:
          1
         / \
        2   3
           / \
          4   5


The reconstructed tree matches the original tree.

12. Complete Implementation
The main implementation contains:
- TreeNode class.
- serialize() function.
- deserialize() function.
- Preorder traversal.
- Inorder traversal.
- Test cases.
- Invalid input validation.
Main code structure
class TreeNode:    def __init__(self, value, left=None, right=None):        self.value = value        self.left = left        self.right = right



The TreeNode class represents each node in the binary tree.

Each node contains:
- A value.
- A reference to its left child.
- A reference to its right child.
Serialization function
def serialize(root):    tokens = []    def preorder(node):        if node is None:            tokens.append("#")            return        tokens.append(str(node.value))        preorder(node.left)        preorder(node.right)    preorder(root)    return ",".join(tokens)



Explanation
- tokens stores the serialized values.
- preorder() performs recursive traversal.
- None nodes are represented by #.
- Node values are converted into strings.
- join() combines the tokens with commas.
Deserialization function
def deserialize(data):    if not isinstance(data, str):        raise TypeError("Tree data must be a string")    if data == "":        raise ValueError("Use '#' for an empty tree")    tokens = data.split(",")    index = 0    def build_tree():        nonlocal index        if index >= len(tokens):            raise ValueError("Incomplete tree data")        token = tokens[index]        index += 1        if token == "#":            return None        try:            value = int(token)        except ValueError as exc:            raise ValueError(                f"Invalid integer token: {token!r}"            ) from exc        node = TreeNode(value)        node.left = build_tree()        node.right = build_tree()        return node



Explanation
1. Check whether the input is a string.
2. Reject an empty string.
3. Split the string into tokens.
4. Initialize the index to zero.
5. Define the recursive build_tree() function.
6. Use nonlocal to update the shared index.
7. Reject incomplete token sequences.
8. Return None when the token is #.
9. Convert valid integer tokens into node values.
10. Recursively rebuild left and right children.
11. Reject any extra tokens after the tree is complete.
12. Return the reconstructed root.

13. Input Validation and Error Handling
A reliable deserialization function must reject malformed input.
Input	Expected result	Reason
""	ValueError	Empty input
"1,#"	ValueError	Incomplete tree
"1,#,#,9"	ValueError	Extra token
"x,#,#"	ValueError	Invalid integer
"#,#"	ValueError	Extra token
"1,,#,#,#"	ValueError	Invalid empty token
"#"	Valid	Empty tree

Why incomplete input is rejected
For example:
1,#


The root node 1 is created, but the serialized data does not contain enough information to construct both children.

Therefore, the deserializer raises ValueError.
Why extra tokens are rejected
For example:
1,#,#,9


The first three tokens already describe a complete tree containing one node.

The additional token 9 does not belong to that tree.

Therefore, the deserializer raises ValueError.

14. Additional Test Examples
Test Case 1: Tree with negative and duplicate values
Tree:
          10
         /  \
       -2    10
         \   /
          4 0


Expected serialization:
10,-2,#,4,#,#,10,0,#,#,#


There are five actual nodes and eleven total tokens.
Test Case 2: Empty tree
Input:
root = None



Output:
#


Test Case 3: Single-node tree
Tree:
  0


Output:
0,#,#


Test Case 4: Left-skewed tree
Tree:
    1
   /
  2
 /
3


Output:
1,2,3,#,#,#,#


Test Case 5: Right-skewed tree
Tree:
1
 \
  2
   \
    3


Output:
1,#,2,#,3,#,#


Test Case 6: Duplicate values
Tree:
      5
     / \
    5   5


Output:
5,5,#,#,5,#,#


Duplicate values are valid because tree structure is represented by the missing-child markers.

15. Testing and Verification
The most important test is the round-trip test.

First, serialize the original tree.

Next, deserialize the resulting string.

Finally, serialize the reconstructed tree and compare both strings.
encoded = serialize(root)restored = deserialize(encoded)assert serialize(restored) == encoded



If the assertion passes, the reconstructed tree has the same serialized structure and values.

Additional verification can use preorder and inorder traversals:
print("Preorder:", preorder_values(restored))print("Inorder:", inorder_values(restored))



Expected output for the main example:
Preorder: [1, 2, 3, 4, 5]
Inorder: [2, 1, 4, 3, 5]


The reconstructed tree is a new object, so:
restored is root



returns False.

16. Complexity Analysis
Let:
- n = number of nodes.
- h = height of the binary tree.
Serialization
Every node is visited exactly once.

Every missing child is also recorded.

Time complexity:
O(n)


Space complexity:
O(n)


The token list contains 2n + 1 tokens, and the recursive traversal uses O(h) stack space.
Deserialization
Every serialized token is processed exactly once.

Time complexity:
O(n)


Auxiliary recursion stack:
O(h)


The reconstructed tree itself requires O(n) space, and the input token list also requires O(n) space.
Complexity summary
Operation	Time Complexity	Auxiliary Space
Serialization	O(n)	O(n)
Deserialization	O(n)	O(h) recursion stack

For a balanced binary tree, the height is approximately O(log n).

For a skewed binary tree, the height can become O(n).

Recursion limitation: A very deep skewed tree may exceed Python's recursion limit.

17. Important Mathematical Observation
A binary tree containing n nodes has exactly n + 1 missing-child pointers.

Each node has two child pointers, so there are 2n total child pointers.

Of these:
- n - 1 point to actual child nodes.
- n + 1 point to missing children.
Therefore:
Total serialized tokens
= Actual nodes + Missing-child markers
= n + (n + 1)
= 2n + 1


For example, if a tree contains five nodes:
Total tokens = 2(5) + 1 = 11


This matches the main example.

18. Common Mistakes
1. Forgetting to include # for missing children.
2. Using inorder or postorder instead of preorder.
3. Reconstructing the right subtree before the left subtree.
4. Forgetting to increment the shared index.
5. Not checking whether the token list has ended.
6. Not checking for extra tokens.
7. Failing to convert integer tokens correctly.
8. Adding a trailing comma to the serialized string.
9. Assuming duplicate values are invalid.
10. Forgetting that an empty tree must serialize as #.

19. Real-World Applications
Serialization and deserialization are useful in several areas of software development.

1. Data Storage

Tree structures can be converted into strings and saved for later reconstruction.

2. Data Transmission

Serialized trees can be transferred between different programs or systems.

3. Database Applications

Tree structures can be represented in a serializable format for storage and retrieval.

4. Testing and Debugging

Developers can serialize a tree to inspect its structure and reproduce test cases.

5. Distributed Systems

Structured data can be transmitted between services and reconstructed when needed.

20. Key Takeaways
- Serialization converts a binary tree into a string.
- Deserialization reconstructs a binary tree from a string.
- Preorder traversal follows Root → Left → Right.
- The # marker represents missing children.
- A shared index tracks token consumption.
- The nonlocal keyword allows recursive calls to update the index.
- Negative and duplicate node values are supported.
- Incomplete and extra tokens must be rejected.
- Serialization and deserialization both take O(n) time.
- The serialized representation contains exactly 2n + 1 tokens for a tree with n nodes.
Final conclusion: The combination of preorder traversal and explicit missing-child markers allows a binary tree to be serialized into a unique representation and reconstructed with the same structure and values.