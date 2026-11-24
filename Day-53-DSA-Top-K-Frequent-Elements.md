Day 53 DSA: Top K Frequent Elements
Day 51 ranked values by size.
Day 52 maintained that ranking as values arrived.

Today, we rank values by how often they appear.
Given a list of integers, return the k most frequent distinct values.

We’ll combine two familiar tools: a frequency map and a bounded min-heap.
1. Understand it like voting for snacks
Children vote for their favourite snacks:
Apple, Banana, Apple, Mango, Banana, Apple


Count the votes:
Apple  → 3
Banana → 2
Mango  → 1


The two most popular snacks are Apple and Banana.

With numbers:
nums = [4, 4, 4, 7, 7, 9]k = 2



Answer:
[4, 7]



Main idea:
Count first. Then keep the k strongest frequency candidates.

2. Clarify ties before coding
What if two values appear equally often?
nums = [8, 8, 3, 3, 5]k = 1



For this lesson, we use this rule:
- Higher frequency wins.
- If frequencies tie, the smaller number wins.
Therefore:
[3]



3. Our contract
Implement:
def top_k_frequent(nums, k):    ...



Rules:
- nums contains integers.
- k is an integer.
- Return exactly k distinct values.
- Valid range: 0 <= k <= number_of_distinct_values.
- For k = 0, return [].
- Raise ValueError for an invalid range.
- Do not modify the input.
- Follow the frequency and tie rules.
4. Start with the straightforward solution
First count occurrences:
counts = {}for value in nums:    counts[value] = counts.get(value, 0) + 1



Then sort the distinct values:
ranked = sorted(    counts,    key=lambda value: (-counts[value], value))print(ranked[:k])



Complexity:
O(n + u log u) time
O(u) extra space


5. How to think about the heap
Ask:
Which retained candidate should be easiest to remove?

The weakest one:
- Lowest frequency.
- If frequencies tie, largest numeric value.
Use this tuple:
(frequency, -value)



Example:
Value 3, frequency 2 → (2, -3)
Value 8, frequency 2 → (2, -8)


Because:
(2, -8) < (2, -3)



Value 8 becomes the weaker candidate.

Remember:
Design the heap key around the candidate you want to evict.

6. Two phases – not one
Phase 1: Count everything

Build the frequency map.

Phase 2: Rank distinct values

For each candidate:
Heap has room?
    Push the candidate.

Candidate is stronger than the root?
    Replace the root.

Otherwise?
    Ignore the candidate.


7. Complete runnable Python
import heapqdef top_k_frequent(nums, k):    if type(k) is not int:        raise TypeError("k must be an integer")    if k < 0:        raise ValueError("k must be nonnegative")    counts = {}    for value in nums:        if type(value) is not int:            raise TypeError("values must be integers")        counts[value] = counts.get(value, 0) + 1    if k > len(counts):        raise ValueError("k exceeds the number of distinct values")    if k == 0:        return []    heap = []    for value, frequency in counts.items():        candidate = (frequency, -value)        if len(heap) < k:            heapq.heappush(heap, candidate)        elif candidate > heap[0]:            heapq.heapreplace(heap, candidate)



8. Dry run
Input:
nums = [8, 8, 3, 3, 5, 5, 5, 9]k = 2



Frequency map:
8 → 2
3 → 2
5 → 3
9 → 1


Value	Candidate key	Decision
8	(2, -8)	Push
3	(2, -3)	Push
5	(3, -5)	Replace weakest: 8
9	(1, -9)	Ignore

Final output:
[5, 3]



9. The invariant and why it works
During the second phase:
The heap contains the best min(k, candidates_processed) distinct values.

When full:
- A candidate no stronger than the root cannot improve the retained top k.
- A candidate stronger than the root replaces the weakest candidate.
Finally, sorting the retained entries produces the correct order.
10. Complexity
Let:
n = number of input elements
u = number of distinct values
k = number of results requested


Step	Cost
Build frequency map	Expected O(n)
Process distinct candidates	O(u log(k+1))
Sort retained results	O(k log(k+1))
Frequency-map storage	O(u)
Heap storage	O(k)

Total expected time for k >= 1:
O(n + u log(k+1))


Total auxiliary space:
O(u)


11. Common mistakes
Ranking by numeric value

Largest value does not mean most frequent value.

Using (frequency, value)

This gives the wrong tie-breaking behaviour.

Returning the heap directly

A heap is not completely sorted.

Validating k against len(nums)

Compare k with:
len(counts)



Claiming O(k) total space

The frequency map also requires memory.

Updating heap priorities directly

Changing priorities without restoring heap order can break the heap.
12. Tests to run
assert top_k_frequent(    [1, 1, 1, 2, 2, 3], 2) == [1, 2]assert top_k_frequent(    [8, 8, 3, 3, 5], 1) == [3]assert top_k_frequent(    [-1, -1, -2, -2, 5], 2) == [-2, -1]assert top_k_frequent(    [9, 1, 5], 2) == [1, 5]assert top_k_frequent(    [7, 7, 7], 1) == [7]assert top_k_frequent([], 0) == []assert top_k_frequent([1, 2], 0) == []values = [3, 3, 1, 2]before = values.copy()top_k_frequent(values, 2)assert values == beforetry:    top_k_frequent([7, 7, 7], 2)except ValueError:    passelse:



13. Assignment
Part A – Predict before running
nums = [6, 6, 2, 2, 2, 9, 9, 4, 4]k = 3



Write:
1. The frequency map.
2. The tuple key for each distinct value.
3. Which candidate is weakest?
4. The final ordered result.
Expected:
[2, 4, 6]



Part B – Implement without copying
Implement top_k_frequent() with:
- The same tie rule.
- A heap of at most k candidates.
- Input validation.
- No input mutation.
Part C – Verify against sorting
expected = sorted(    counts,    key=lambda value: (-counts[value], value))[:k]



Try cases with many ties.
14. Institute, corporate, and client-level thinking
Setting	What to focus on
Institute/interview	Explain the count-map + heap combination
Corporate	Define deterministic ties, validate inputs and test results
Client	Clarify what counts as an occurrence and how ties should be handled

Real-world example: Most common error codes
Suppose logs contain error-code events.

The client asks:

"Show the top five errors."

Clarify:
- Top five by event count or affected users?
- All-time or during a specific time window?
- Count repeated log delivery once or multiple times?
- Return exactly five codes or include all codes tied at fifth?
Each choice changes the result.
Sudden requirement change: Make it live
Here, an existing candidate's frequency changes whenever another occurrence arrives.

That requires maintained counts and a strategy for changing heap priorities or recomputing the ranking.

Today's implementation deliberately counts first, then ranks.
15. Remember this
Top K by size: Rank values.

Top K by frequency: Count first, then rank distinct values.

GitHub filename:
Day-53-Notes.md


Explain-back checkpoint: Why does (frequency, -value) put the correct candidate at the root when smaller values must win frequency ties?