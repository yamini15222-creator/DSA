DAY 52 – DSA
Kth Largest Element in a Stream
1. Problem Statement
Design a class that continuously receives integer values from a stream and returns the kth-largest element after every new value is added.

The stream contains initial values and new incoming values.

If fewer than k elements are available, return None.

Important: Duplicate values are counted separately.

Example:

Input:
- k = 3
- Initial values = [4, 5, 8, 2]
- Incoming values = [3, 5, 10, 9, 4]
Output:

- [4, 5, 5, 8, 8]
2. Objective
- Understand the Kth Largest Element in a Stream problem.
- Learn Min Heap data structure.
- Maintain the largest k elements efficiently.
- Implement add() and peek() operations.
- Understand time and space complexity.
- Practice heap-based problem solving.
3. Concepts Used
1. Stream

A stream is a continuous sequence of incoming values.

Example: 10 → 20 → 30 → 40 → 50.

2. Heap

A heap is a tree-based data structure used to efficiently access the smallest or largest element.

Types:
- Min Heap
- Max Heap
3. Min Heap

In a Min Heap, the smallest element is always at the root.

For this problem, we maintain only the largest k elements. The smallest element among those k values represents the kth-largest element in the complete stream.

4. Python heapq Module

Python provides the built-in heapq module to implement Min Heap operations.

Important functions:
- heapq.heappush() – Inserts an element.
- heapq.heapreplace() – Replaces the smallest element.
- heap[0] – Accesses the smallest element.
4. Approach
We use a Min Heap to store only the largest k values.

Steps:
1. Read the value of k.
2. Create an empty Min Heap.
3. Insert the initial values.
4. If the heap contains fewer than k elements, insert the new value.
5. If the heap already contains k elements, compare the new value with the root.
6. If the new value is greater than the root, replace the root.
7. Otherwise, ignore the new value.
8. Return the root if the heap contains k elements.
9. If fewer than k elements exist, return None.
5. Main Operations
add(value)

Adds a new value to the stream and returns the current kth-largest element.

peek()

Returns the current kth-largest element without modifying the heap.
6. Dry Run – Step-by-Step Execution
Given:
- k = 3
- Initial values = [6, 2]
- Incoming values = [4, 8, 1, 10, 8]
Step	Added value	Largest 3 values	Answer
Initial	-	[2, 6]	None
1	4	[2, 4, 6]	2
2	8	[4, 6, 8]	4
3	1	[4, 6, 8]	4
4	10	[6, 8, 10]	6
5	8	[8, 8, 10]	8

Final output: [2, 4, 4, 6, 8]
7. Python Implementation
The implementation uses:
- KthLargest class
- Min Heap
- add() method
- peek() method
- Input validation
8. Time and Space Complexity
Operation	Complexity
add()	O(log k)
peek()	O(1)
Space	O(k)

- O(log k): Insertion or replacement in the heap.
- O(1): Accessing the root element.
- O(k): Storing at most k elements.
9. Testing
The following test cases are included:
1. Standard example.
2. Assignment example.
3. Fewer than k values.
4. Peek operation.
5. Duplicate values.
6. Negative values.
7. k = 1.
8. Independent instances.
9. Original input list preservation.
10. Invalid input validation.
11. Sorting-based reference comparison.
10. Common Mistakes
- Using the wrong heap type.
- Returning the root before k values are available.
- Forgetting that duplicates count separately.
- Replacing the root with a smaller value.
- Sorting the complete stream unnecessarily.
- Modifying the original input list.
- Changing the heap during peek().
11. Real-Time Applications
1. Leaderboard systems – Maintaining top-ranked players.
2. Online gaming – Tracking highest scores.
3. E-commerce – Finding popular products.
4. Financial systems – Tracking large transactions.
5. Data analytics – Maintaining top values from incoming data.
12. Advantages
- Efficient insertion.
- Requires less memory.
- Avoids sorting the entire stream repeatedly.
- Supports duplicate values.
- Provides quick access to the kth-largest element.
13. Limitations
- Designed for an append-only stream.
- Does not support deletion of old values.
- Does not directly support rolling time windows.
- Stores only the largest k values.
14. Assignment Tasks
Part A – Basic Implementation

Implement the KthLargest class with constructor and add() method.

Part B – Peek Operation

Implement peek() to return the kth-largest element without modifying the heap.

Part C – Reference Testing

Compare the heap-based answer with a sorting-based answer after every insertion.
15. How to Run
Run the implementation and tests:
python day_52_kth_largest.py


Run the assignment separately:
python day_52_assignment.py


16. Expected Results
For the assignment example:
- k = 3
- Initial values = [6, 2]
- Incoming values = [4, 8, 1, 10, 8]
Expected output:
[2, 4, 4, 6, 8]


All automated tests should pass.
17. Key Learning Outcomes
After completing this problem, I learned:
1. How Min Heap works.
2. How to use Python heapq.
3. How to maintain the largest k elements.
4. How to implement add() and peek().
5. How to solve streaming problems.
6. How to compare heap and sorting approaches.
7. How to test different input conditions.
18. Conclusion
The Kth Largest Element in a Stream problem can be efficiently solved using a Min Heap.

Instead of storing and sorting every incoming value, we maintain only the largest k values.

The root of the Min Heap gives the kth-largest element.

This approach provides O(log k) time for adding a value, O(1) time for retrieving the answer, and O(k) space complexity.