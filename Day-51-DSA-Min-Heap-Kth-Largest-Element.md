# Day 51 DSA: Binary Heap — Find the Kth Largest Element

Today we learn how to use a **Binary Heap** to find the Kth largest element and return the Top K largest values without sorting the entire input list.

Our main approach is:

- Use a **Min-Heap of size `k`**.
- Keep only the largest `k` values.
- Remove the weakest retained value when a better value arrives.
- Use the heap root to find the Kth largest value.

---

## 1. Understand the problem like a winners' club

Imagine a club with room for only three winners.

People arrive with scores:

```text
8, 3, 5, 12, 7, 12, 1
```

The club can retain only the three highest scores.

Whenever a new score arrives:

- If there is an empty place, add the score.
- If the club is full and a higher score arrives, remove the lowest score and add the new score.
- If the new score is lower than or equal to the lowest retained score, ignore it.

At the end:

```text
Retained values: [8, 12, 12]
```

The third-largest value is:

```text
8
```

**Key idea:**

> Keep the largest `k` values. The smallest value among those retained values is the Kth largest overall.

---

## 2. What is a Binary Heap?

A Binary Heap is a special complete binary tree that follows a heap-ordering rule.

It has two important properties.

### Shape property

A heap must be a complete binary tree.

This means:

- Every level is completely filled except possibly the last.
- The last level is filled from left to right.

### Ordering property

A heap must follow either the min-heap or max-heap ordering rule.

**Min-Heap:**

Every parent is smaller than or equal to its children.

Example:

```text
        2
       / \
      5   3
     / \
    9   7
```

The smallest value is at the root.

**Max-Heap:**

Every parent is greater than or equal to its children.

Example:

```text
        12
       /  \
      8    10
     / \
    3   5
```

The largest value is at the root.

### Heap representation using an array

A heap can be stored using a normal Python list.

For example:

```python
heap = [2, 5, 3, 9, 7]
```

For a zero-based array index `i`:

```python
left_child = 2 * i + 1
right_child = 2 * i + 2
parent = (i - 1) // 2
```

The parent formula is used when `i > 0`.

**Important:**

A heap is not a fully sorted array. It only guarantees the parent-child ordering rule.

---

## 3. Min-Heap versus Max-Heap

| Structure | Root contains |
|---|---|
| Min-Heap | Smallest value |
| Max-Heap | Largest value |

A common interview question is:

**Why do we use a Min-Heap to find the Kth largest element?**

Because we want to retain the largest `k` values.

Among those retained values, we need quick access to the smallest one.

That smallest retained value is the weakest candidate. When a better value arrives, we remove it.

For example:

```text
Retained values: [7, 8, 12]
k = 3
```

The smallest retained value is:

```text
7
```

If `10` arrives, we replace `7` with `10`.

**Remember:**

Think about which retained value needs to be removed, not just what the final answer is called.

---

## 4. Understand the problem precisely

We need to implement:

```python
def kth_largest(nums, k):
    ...
```

### Input

- `nums`: A list of integers.
- `k`: The required rank.

### Output

Return the Kth largest value.

### Conditions

- `1 <= k <= len(nums)`.
- Duplicate values count separately.
- Do not modify the original input list.
- Raise `ValueError` when `k` is invalid.

Example:

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

Descending order:

```text
[6, 5, 4, 3, 2, 1]
```

Answer:

```text
5
```

### What about duplicates?

```python
nums = [5, 5, 4]
k = 2
```

Descending order:

```text
[5, 5, 4]
```

Answer:

```text
5
```

Duplicates count separately.

**Kth largest does not mean Kth distinct largest.**

---

## 5. Start with the simple sorting solution

The easiest way to solve this problem is to sort the complete list.

```python
def kth_largest_by_sorting(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("Invalid k")

    return sorted(nums, reverse=True)[k - 1]
```

Example:

```python
nums = [8, 3, 5, 12, 7, 12, 1]

print(kth_largest_by_sorting(nums, 3))
```

Output:

```text
8
```

Time complexity:

```text
O(n log n)
```

The problem with sorting is that we order every value even though we only need the Kth largest value.

Can we keep only the largest `k` candidates?

Yes. We can use a bounded heap.

---

## 6. Derive the Kth Largest algorithm

We maintain a Min-Heap containing at most `k` values.

For every incoming value, there are three cases.

### Case 1: Heap contains fewer than k values

Insert the incoming value.

```python
heapq.heappush(heap, value)
```

Why?

We have not filled all available places.

### Case 2: Heap is full and incoming value is greater than the root

Replace the root.

```python
heapq.heapreplace(heap, value)
```

Why?

The incoming value is greater than the smallest retained value. Therefore, the smallest retained value no longer belongs in the top `k`.

### Case 3: Heap is full and incoming value is less than or equal to the root

Ignore the incoming value.

Why?

It cannot improve the current top `k` values.

### The invariant

> After processing each value, the heap contains the largest `min(k, processed_count)` values seen so far, counting duplicates.

This is the most important idea in the algorithm.

---

## 7. Complete runnable Python — Part A

File name:

```text
kth_largest.py
```

Code:

```python
import heapq


def kth_largest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("Invalid k")

    heap = []

    for value in nums:

        if len(heap) < k:
            heapq.heappush(heap, value)

        elif value > heap[0]:
            heapq.heapreplace(heap, value)

    return heap[0]


nums = [8, 3, 5, 12, 7, 12, 1]
k = 3

print(kth_largest(nums, k))
```

Output:

```text
8
```

### Understand the heap operations

**1. heappush()**

```python
heapq.heappush(heap, value)
```

Adds a value to the heap and restores heap ordering.

**2. heap[0]**

```python
heap[0]
```

Returns the smallest value in the Min-Heap without removing it.

**3. heapreplace()**

```python
heapq.heapreplace(heap, value)
```

Removes the smallest value and inserts the incoming value.

It restores heap ordering after replacement.

Important: `heapreplace()` always replaces the root. Therefore, we must check:

```python
value > heap[0]
```

before calling it.

### Understand the variables

| Variable | Meaning |
|---|---|
| `nums` | Original input list |
| `k` | Number of largest values to retain |
| `heap` | Min-Heap storing retained values |
| `value` | Current incoming element |
| `heap[0]` | Smallest retained value |

---

## 8. Part A — Dry Run

Input:

```python
nums = [8, 3, 5, 12, 7, 12, 1]
k = 3
```

We need to retain the three largest values.

| Incoming value | Action | Retained values (sorted for explanation) |
|---|---|---|
| 8 | Insert | [8] |
| 3 | Insert | [3, 8] |
| 5 | Insert | [3, 5, 8] |
| 12 | Replace 3 | [5, 8, 12] |
| 7 | Replace 5 | [7, 8, 12] |
| 12 | Replace 7 | [8, 12, 12] |
| 1 | Ignore | [8, 12, 12] |

Final retained values:

```text
[8, 12, 12]
```

The smallest retained value is:

```text
8
```

Therefore:

```text
Third largest = 8
```

Notice that the table shows retained values sorted only to make the explanation easy. The actual heap array is not necessarily sorted.

---

## 9. Part B — Return the Top K Largest Values

In Part A, we return only one value: the Kth largest.

In Part B, we return all the retained top `k` values in descending order.

Implement:

```python
def top_k_largest(nums, k):
    ...
```

### Output contract

- Input: A list of integers and an integer `k`.
- Output: The `k` largest values in descending order.
- Duplicates count separately.
- Do not modify the original list.
- Raise `ValueError` for invalid `k`.

### Algorithm

We use the same Min-Heap approach from Part A.

The only difference is the final return statement.

Part A:

```python
return heap[0]
```

Part B:

```python
return sorted(heap, reverse=True)
```

Why?

The heap contains the largest `k` values, but its internal array is not sorted.

Therefore, we sort only the retained `k` values in descending order.

### Complete runnable Python — Part B

File name:

```text
top_k_largest.py
```

Code:

```python
import heapq


def top_k_largest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("Invalid k")

    heap = []

    for value in nums:

        if len(heap) < k:
            heapq.heappush(heap, value)

        elif value > heap[0]:
            heapq.heapreplace(heap, value)

    return sorted(heap, reverse=True)


nums = [8, 3, 5, 12, 7, 12, 1]
k = 3

print(top_k_largest(nums, k))
```

Output:

```text
[12, 12, 8]
```

### Part B — Dry Run

Input:

```python
nums = [8, 3, 5, 12, 7, 12, 1]
k = 3
```

| Incoming value | Action | Retained values |
|---|---|---|
| 8 | Insert | [8] |
| 3 | Insert | [3, 8] |
| 5 | Insert | [3, 5, 8] |
| 12 | Replace 3 | [5, 8, 12] |
| 7 | Replace 5 | [7, 8, 12] |
| 12 | Replace 7 | [8, 12, 12] |
| 1 | Ignore | [8, 12, 12] |

Sort only the retained values:

```python
sorted([8, 12, 12], reverse=True)
```

Output:

```text
[12, 12, 8]
```

### Part A versus Part B

| Part A | Part B |
|---|---|
| `kth_largest()` | `top_k_largest()` |
| Returns one value | Returns k values |
| Returns `heap[0]` | Returns `sorted(heap, reverse=True)` |
| Finds the Kth largest | Finds the Top K largest |
| `O(n log(k+1))` | `O(n log(k+1) + k log k)` |

---

## 10. Part C — Explain a Decision

Part C is an explanation task. No additional code is required.

Suppose:

```text
Retained values: [7, 8, 12]
k = 3
```

The smallest retained value is:

```text
7
```

Consider each incoming value independently.

### Case 1: Incoming 6 → Ignore

Compare:

```text
6 < 7
```

The incoming value is smaller than the smallest retained value.

Therefore, it cannot enter the top three.

Retained values remain:

```text
[7, 8, 12]
```

The invariant is preserved because the three retained values are still the largest three values among those processed.

### Case 2: Incoming 7 → Ignore

Compare:

```text
7 == 7
```

The incoming value is equal to the smallest retained value.

Replacing the existing 7 with another 7 would not improve the retained values.

Therefore, we ignore it.

Retained values remain:

```text
[7, 8, 12]
```

The invariant is preserved.

Important: Duplicates count separately. Ignoring an equal value here is safe because the retained values already include an equal value.

### Case 3: Incoming 10 → Replace 7

Compare:

```text
10 > 7
```

The incoming value is greater than the smallest retained value.

Therefore, remove 7 and insert 10.

New retained values:

```text
[8, 10, 12]
```

The invariant is preserved because these are now the three largest values.

### Final comparison

| Incoming value | Decision | Reason |
|---|---|---|
| 6 | Ignore | Smaller than 7 |
| 7 | Ignore | Equal to 7 |
| 10 | Replace 7 | Greater than 7 |

### Interview-ready answer

A Min-Heap of size `k` stores the largest `k` values encountered so far. Its root contains the smallest retained value.

If an incoming value is smaller than or equal to the root, we ignore it because it cannot improve the top `k` values.

If an incoming value is greater than the root, we replace the root because the incoming value deserves a place among the largest `k` values.

This maintains the invariant.

---

## 11. Why the Algorithm Is Correct

Initially, the heap is empty.

While fewer than `k` values have been processed, we insert every incoming value.

Once the heap is full, let:

```text
m = smallest retained value
x = incoming value
```

There are two possibilities.

**Case 1: x <= m**

There are already `k` retained values that are greater than or equal to `x`.

The incoming value cannot improve the top `k`, so ignoring it is safe.

**Case 2: x > m**

The incoming value is stronger than the weakest retained value.

Remove `m` and insert `x`.

The heap now contains the largest `k` values among all processed values.

Therefore, the invariant remains true after every operation.

At the end:

- The heap contains the largest `k` values.
- Its root is the smallest among those values.
- That root is exactly the Kth largest value.

For Part B, sorting the retained values in descending order returns the complete top `k` list.

---

## 12. Complexity Analysis

Let:

```text
n = Number of input values
k = Number of values to retain
```

### Part A — Kth Largest

| Operation | Time complexity |
|---|---|
| Read heap root | O(1) |
| Insert into heap | O(log k) |
| Replace root | O(log k) |
| Process all values | O(n log(k+1)) |
| Extra space | O(k) |

Total:

```text
Time:  O(n log(k+1))
Space: O(k)
```

For `k >= 2`, time is commonly written as `O(n log k)`.

When `k = 1`, the algorithm effectively tracks the maximum in linear time.

### Part B — Top K Largest

Part B has one additional operation: sorting the retained values.

Sorting `k` values requires:

```text
O(k log k)
```

Total:

```text
Time:  O(n log(k+1) + k log k)
Space: O(k)
```

The heap itself never stores more than `k` values.

---

## 13. Mistakes to Avoid

### Mistake 1: Thinking the heap is completely sorted

```python
heap = [8, 12, 12]
```

Only the root is guaranteed to be the smallest value.

Other positions are not guaranteed to be in sorted order.

### Mistake 2: Replacing the root for every incoming value

Incorrect:

```python
heapq.heapreplace(heap, value)
```

This could remove a stronger retained value.

Correct:

```python
elif value > heap[0]:
    heapq.heapreplace(heap, value)
```

### Mistake 3: Using a set

Incorrect:

```python
nums = list(set(nums))
```

This removes duplicates and changes the meaning of Kth largest.

### Mistake 4: Forgetting input validation

Always check:

```python
if not 1 <= k <= len(nums):
    raise ValueError("Invalid k")
```

### Mistake 5: Keeping every value in the heap

If we keep all values, we lose the `O(k)` space advantage.

The heap must contain at most `k` elements.

### Mistake 6: Confusing Min-Heap with Max-Heap

For K largest, use a Min-Heap.

For K smallest, use a Max-Heap.

---

## 14. Tests to Run

### Part A — Test `kth_largest()`

```python
assert kth_largest([8, 3, 5, 12, 7, 12, 1], 3) == 8

assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

# Duplicates
assert kth_largest([5, 5, 4], 2) == 5

# Negative values
assert kth_largest([-5, -1, -3], 2) == -3

# One element
assert kth_largest([8], 1) == 8

# First rank
assert kth_largest([4, 1, 9], 1) == 9

# Last rank
assert kth_largest([4, 1, 9], 3) == 1

# All equal
assert kth_largest([7, 7, 7], 2) == 7

print("Part A: All test cases passed!")
```

### Part B — Test `top_k_largest()`

```python
assert top_k_largest([8, 3, 5, 12, 7, 12, 1], 3) == [12, 12, 8]

assert top_k_largest([3, 2, 1, 5, 6, 4], 2) == [6, 5]

# Duplicates
assert top_k_largest([5, 5, 4], 2) == [5, 5]

# Negative values
assert top_k_largest([-5, -1, -3], 2) == [-1, -3]

# One element
assert top_k_largest([10], 1) == [10]

# All equal
assert top_k_largest([7, 7, 7], 2) == [7, 7]

print("Part B: All test cases passed!")
```

### Input preservation test

Both functions must leave the original input unchanged.

```python
nums = [8, 3, 5, 12, 7, 12, 1]

before = nums.copy()

kth_largest(nums, 3)
assert nums == before

top_k_largest(nums, 3)
assert nums == before

print("Input preservation test passed!")
```

### Invalid input tests

```python
invalid_cases = [
    ([], 1),
    ([1, 2], 0),
    ([1, 2], 3),
    ([1, 2], -1)
]

for nums, k in invalid_cases:
    try:
        kth_largest(nums, k)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")

print("Invalid input tests passed!")
```

---

## 15. Institute, Corporate, and Client-Level Thinking

Different environments focus on different aspects of this problem.

| Setting | What to focus on |
|---|---|
| Institute / Interview | Explain why Kth largest uses a Min-Heap, state the invariant, analyze O(k) memory |
| Corporate | Test invalid ranks, duplicates, negative values, tie-breaking, and input preservation |
| Client | Clarify whether Top K means values, distinct values, records, or everyone tied at the boundary |

### A. Institute / Interview preparation

Prepare these questions:

**Question 1: Why use a Min-Heap for Kth largest?**

Answer:

We use a Min-Heap because we need quick access to the smallest value among the largest `k` retained values. When a larger value arrives, we can replace the root.

**Question 2: What is the invariant?**

Answer:

After processing each element, the heap contains the largest `min(k, processed_count)` values seen so far.

**Question 3: What is the space complexity?**

Answer:

The heap stores at most `k` elements. Therefore, auxiliary space complexity is `O(k)`.

**Question 4: Why not sort the entire list?**

Answer:

Sorting requires `O(n log n)` time. A bounded heap allows us to process the input while retaining only `k` values.

### B. Corporate preparation

Prepare test cases for:

1. Invalid `k` values.
2. Duplicate values.
3. Negative numbers.
4. All values being equal.
5. A single-element list.
6. Input preservation.
7. Equal values and tie-breaking requirements.

Remember that tie-breaking rules become important when working with records rather than plain numbers.

### C. Client-level thinking

Suppose a client asks:

> Show me the top three transactions.

Before implementing, clarify:

- Does the client want three transaction records or three distinct amounts?
- How should transactions with equal amounts be ordered?
- Should we consider all-time transactions or a rolling time window?
- Can transactions be corrected or deleted?

A bounded heap works well for retaining top-K values from append-only data.

**Important: Rolling windows are different.**

Old winners can expire from a rolling window. A simple bounded heap does not automatically remove expired values or maintain the correct top K.

The requirements may require a different or more advanced data structure.

---

## 16. Remember This

> To keep the strongest `k` candidates, make the weakest retained candidate easy to remove.

That is why we use a Min-Heap for K largest.

### K largest versus K smallest

| Problem | Heap | Root contains |
|---|---|---|
| K largest | Min-Heap | Smallest retained value |
| K smallest | Max-Heap | Largest retained value |

### Explain-back checkpoint

**Question:**

If you wanted the K smallest values instead, which retained value would you need quick access to, and why?

**Answer:**

I would need quick access to the largest retained value. Therefore, I would use a Max-Heap.

The root contains the largest among the retained K smallest values. When a smaller incoming value arrives, I replace the root.

This ensures that the heap always retains the K smallest values encountered so far.



### GitHub filename

```text
Day-51-DSA-Min-Heap-Kth-Largest-Element.md
```

**Day 51 takeaway:**

A heap helps us avoid sorting the entire input when we only need the strongest or weakest `k` candidates. The important skill is choosing the heap whose root gives quick access to the candidate we need to remove.