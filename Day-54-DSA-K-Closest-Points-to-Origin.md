Day 54 DSA: K Closest Points to the Origin
Introduction
Today, we are learning K Closest Points to the Origin using a Heap (Priority Queue).

In this problem, we are given a list of points represented by (x, y) coordinates. Our task is to find exactly k points that are closest to the origin (0, 0).

We will use a Max-Heap approach using Python's Min-Heap (heapq) to efficiently maintain the closest points.

The main idea is to keep only the k closest points and remove the farthest point whenever we find a better candidate.
1. Problem Statement
Given a list of points where each point is represented as (x, y), return exactly k points closest to the origin (0, 0).

We calculate the distance using the squared Euclidean distance:
distance = x * x + y * y



We do not need to calculate the square root because squared distance gives the same ordering as normal distance.

Example:
points = [(3, 3), (1, 2), (-2, 1), (0, 1)]k = 2



Output:
[(0, 1), (-2, 1)]



Explanation:
- (3, 3) → Distance = 18
- (1, 2) → Distance = 5
- (-2, 1) → Distance = 5
- (0, 1) → Distance = 1
The two closest points are (0, 1) and (-2, 1).

When two points have the same distance, we compare their coordinates:
1. Smaller distance comes first.
2. If distances are equal, smaller x comes first.
3. If both distance and x are equal, smaller y comes first.
2. Understanding the Problem with a Real-Life Example
Imagine a delivery van that has space for only two delivery locations.

There are several delivery locations, but the van can visit only two locations closest to the warehouse.

What should we do?
1. Select the first two locations.
2. Find the farthest location among the selected two.
3. When a new location arrives, compare it with the farthest selected location.
4. If the new location is closer, remove the farthest location.
5. Add the new location to the selected list.
This process continues until all locations are checked.

Main concept:

We maintain only the k closest points instead of sorting all the points.
3. Understanding Squared Euclidean Distance
The distance between a point (x, y) and the origin (0, 0) is:
Distance = √(x² + y²)


But we can avoid calculating the square root.

We use:
Distance² = x² + y²


Example:

For point (1, 2):
Distance² = 1² + 2²
          = 1 + 4
          = 5


For point (3, 3):
Distance² = 3² + 3²
          = 9 + 9
          = 18


Since 5 < 18, point (1, 2) is closer.

Therefore, squared distance is enough to compare points.
4. Understanding Heap Concept
A heap is a special tree-based data structure used to efficiently find the smallest or largest element.

Python provides the heapq module, which implements a Min-Heap.

In a Min-Heap:
- The smallest element is always at the root.
- We can access the smallest element quickly.
- Insertion and removal take O(log n) time.
But in this problem, we need the farthest point at the root because we want to remove the farthest point whenever a closer point arrives.

So, we reverse the values using negative numbers.
key = (-distance_squared, -x, -y)



This makes the worst retained point appear at the root of Python's Min-Heap.

Why do we use negative values?

Because Python's Min-Heap always places the smallest key at the root.

By reversing the ranking values, the farthest point becomes the smallest heap key.
5. Understanding the Heap Key
We use the following heap key:
candidate = (-distance_squared, -x, -y)



Let's understand it with an example.
Point	Distance²	Heap Key
(3, 3)	18	(-18, -3, -3)
(1, 2)	5	(-5, -1, -2)
(-2, 1)	5	(-5, 2, -1)

Python compares tuples from left to right.

For equal distances, it compares the x values. If those are also equal, it compares the y values.

Important:
- A larger heap key represents a better point.
- A smaller heap key represents a worse point.
- The root contains the worst point among the retained points.
- We replace the root only when a better candidate arrives.
6. Algorithm / Approach
Follow these steps to solve the problem:
1. Check whether k is within the valid range.
2. If k == 0, return an empty list.
3. Create an empty heap.
4. Calculate the squared distance for every point.
5. Create a negative heap key using distance, x, and y.
6. If the heap contains fewer than k points, insert the new point.
7. If the heap is full, compare the new candidate with the root.
8. If the new candidate is better, replace the root.
9. After processing all points, sort the retained heap entries into the required order.
10. Convert the negative coordinates back into their original values.
11. Return the result.
7. Python Code Implementation
Filename: Day-54-Top-K-Closest-Points.py
import heapqdef k_closest(points, k):    if not 0 <= k <= len(points):        raise ValueError("k must be between 0 and len(points)")    if k == 0:        return []    heap = []    for x, y in points:        distance_squared = x * x + y * y        candidate = (-distance_squared, -x, -y)        if len(heap) < k:            heapq.heappush(heap, candidate)        elif candidate > heap[0]:            heapq.heapreplace(heap, candidate)    result = []    for _, neg_x, neg_y in sorted(heap, reverse=True):        result.append((-neg_x, -neg_y))    return result



Output:
Closest Points: [(0, 1), (-2, 1)]


8. Code Explanation
Let's understand the important parts of the code.

Step 1: Validate k
if not 0 <= k <= len(points):    raise ValueError("k must be between 0 and len(points)")



This checks whether k is valid.

If k is negative or greater than the number of points, it raises a ValueError.

Step 2: Handle k = 0
if k == 0:    return []



If we need zero points, we return an empty list.

Step 3: Create an empty heap
heap = []



This heap stores only the k closest points.

Step 4: Calculate squared distance
distance_squared = x * x + y * y



This calculates the distance of each point from the origin without using the square root.

Step 5: Create the heap key
candidate = (-distance_squared, -x, -y)



Negative values reverse the ordering so that the worst retained point stays at the root.

Step 6: Insert elements
if len(heap) < k:    heapq.heappush(heap, candidate)



If the heap has fewer than k points, we insert the new point.

Step 7: Replace the worst point
elif candidate > heap[0]:    heapq.heapreplace(heap, candidate)



If the new candidate is better than the root, we remove the root and insert the new candidate.

Step 8: Sort and return the result
result = []for _, neg_x, neg_y in sorted(heap, reverse=True):    result.append((-neg_x, -neg_y))return result



We sort the retained points according to the required ranking and convert the negative coordinates back to their original values.
9. Dry Run
Let's execute the program step by step.

Input:
points = [(3, 3), (1, 2), (-2, 1), (0, 1)]k = 2



Incoming Point	Distance²	Decision	Retained Points
(3, 3)	18	Insert	[(3, 3)]
(1, 2)	5	Insert	[(1, 2), (3, 3)]
(-2, 1)	5	Replace (3, 3)	[(-2, 1), (1, 2)]
(0, 1)	1	Replace (1, 2)	[(0, 1), (-2, 1)]

Final Output:
[(0, 1), (-2, 1)]



The heap contains only two points because k = 2.

Note: The heap itself is not sorted. We sort the retained elements before returning the result.
10. Time and Space Complexity
Let:
- n = Total number of points.
- k = Number of closest points required.
Operation	Time Complexity
Calculate distance	O(1)
Insert into heap	O(log k)
Replace root	O(log k)
Process all points	O(n log(k + 1))
Sort final k points	O(k log k)

Overall Time Complexity:
O(n log(k + 1))


This includes sorting the final k points.

Space Complexity:
O(k)


Because we maintain only k elements in the heap.
11. Test Cases
Let's check whether our implementation works correctly for different inputs.
# Test Case 1: Normal inputassert k_closest([(3, 3), (1, 2), (-2, 1), (0, 1)], 2) == [    (0, 1), (-2, 1)]# Test Case 2: Same distance, smaller x winsassert k_closest([(1, 2), (-2, 1)], 1) == [    (-2, 1)]# Test Case 3: Same distance and x, smaller y winsassert k_closest([(1, 2), (1, -2)], 1) == [    (1, -2)]# Test Case 4: Duplicate pointsassert k_closest([(2, 0), (0, 0), (0, 0)], 2) == [    (0, 0), (0, 0)]# Test Case 5: k = 0assert k_closest([], 0) == []# Test Case 6: k = nassert k_closest([(2, 0), (0, 0)], 2) == [    (0, 0), (2, 0)]# Test Case 7: Invalid ktry:



Expected Output:
Invalid k handled correctly
All test cases passed!


12. Common Mistakes
1. Using normal distance unnecessarily

Using sqrt() is not required. Squared distance is enough to compare points.

2. Using a normal Min-Heap directly

If we store positive distances, the closest point will be at the root. But we want the farthest retained point at the root.

3. Forgetting negative tie-breakers

We must reverse all three values:
(-distance_squared, -x, -y)



Not just the distance.

4. Returning the heap without sorting

A heap is not a sorted list. We must sort the retained points before returning them.

5. Forgetting duplicate points

Duplicate points count separately. We should not remove them using a set.
13. Assignment
Now try implementing the problem yourself.

Task 1: Implement K Closest Points
points = [(2, 0), (-2, 0), (0, 2), (1, 1), (0, 0)]k = 3



Expected output:
[(0, 0), (1, 1), (-2, 0)]



Task 2: K Closest Points to Any Center

Create another function:
def k_closest_to(points, k, center):    pass



Instead of calculating distance from (0, 0), calculate distance from the given center.

Use this formula:
distance_squared = (x - cx) ** 2 + (y - cy) ** 2



Example:
points = [(0, 0), (3, 1), (2, 2)]k = 2center = (2, 1)



Expected output:
[(2, 2), (3, 1)]



Remember to use the same tie-breaking rule based on the original x and y coordinates.
14. Interview Questions
Q1. What is the K Closest Points to the Origin problem?

It is a problem where we find the k points closest to (0, 0) from a given list of coordinate points.

Q2. Why do we use squared distance?

Because square root does not change the ordering of nonnegative distances. Therefore, squared distance is sufficient.

Q3. Why do we use a heap?

A heap allows us to maintain only the required k closest points without sorting the entire input.

Q4. Why do we use negative values?

Python provides a Min-Heap. Negative values reverse the ordering and help us keep the farthest retained point at the root.

Q5. What is the time complexity?

O(n log(k + 1)), including sorting the final results.

Q6. What is the space complexity?

O(k) because the heap stores only k points.

Q7. What happens when k = 0?

The function returns an empty list.

Q8. What happens when two points have the same distance?

We compare their x coordinates first and then their y coordinates. Smaller coordinates win.
15. Real-World Applications
1. Finding the nearest hospitals to a location.
2. Finding nearby restaurants or shopping centers.
3. Finding the closest delivery destinations.
4. Location-based recommendation systems.
5. Finding nearby users in social networking applications.
6. Nearest-neighbor search in machine learning.
Note: Real-world road distance or travel time may differ from straight-line distance. The distance metric must match the actual requirement.
16. Day 54 Key Takeaways
- Learned the K Closest Points to the Origin problem.
- Understood squared Euclidean distance.
- Learned how Python Min-Heap works.
- Understood why negative values are used in heap keys.
- Learned how to maintain only k closest points.
- Practiced heapq.heappush() and heapq.heapreplace().
- Understood tie-breaking rules.
- Practiced dry runs and test cases.
- Learned time and space complexity.
Important concept to remember:

To find the k closest points, maintain a heap of size k and keep the farthest retained point at the root. Whenever a better point arrives, replace the root.

17. Explain-Back Checkpoint
Consider the following two points:
(1, 2)(1, -2)



Both have the same squared distance:
1² + 2² = 5
1² + (-2)² = 5


Their heap keys are:
(1, 2)  -> (-5, -1, -2)(1, -2) -> (-5, -1, 2)



Since (-5, -1, 2) is smaller than (-5, -1, -2), (1, -2) is considered worse in the reversed heap ranking.

Therefore, (1, -2) wins under our required ranking because its y coordinate is smaller.

Day 54 completed: K Closest Points to the Origin using Heap.