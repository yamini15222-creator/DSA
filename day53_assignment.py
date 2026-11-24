
import heapq

# Part B: Implement Top K Frequent Elements

def top_k_frequent(nums, k):

    if type(k) is not int:
        raise TypeError("k must be an integer")

    if k < 0:
        raise ValueError("k must be nonnegative")

    counts = {}

    for value in nums:
        if type(value) is not int:
            raise TypeError("values must be integers")

        counts[value] = counts.get(value, 0) + 1

    if k > len(counts):
        raise ValueError("k exceeds distinct values")

    if k == 0:
        return []

    heap = []

    for value, frequency in counts.items():

        candidate = (frequency, -value)

        if len(heap) < k:
            heapq.heappush(heap, candidate)

        elif candidate > heap[0]:
            heapq.heapreplace(heap, candidate)

    ranked = sorted(heap, reverse=True)

    return [-value for frequency, value in ranked]


# Part A: Predict before running

nums = [6, 6, 2, 2, 2, 9, 9, 4, 4]
k = 3

print("Part A:")
print(top_k_frequent(nums, k))


# Part B: Test implementation

print("\nPart B:")
print(top_k_frequent([4, 4, 4, 7, 7, 9], 2))


# Part C: Verify against sorting

nums = [4, 4, 4, 7, 7, 9]
k = 2

counts = {}

for value in nums:
    counts[value] = counts.get(value, 0) + 1

expected = sorted(
    counts,
    key=lambda value: (-counts[value], value)
)[:k]

actual = top_k_frequent(nums, k)

print("\nPart C:")
print("Expected:", expected)
print("Actual:", actual)

assert actual == expected

print("Verification successful!")


# Additional test cases

assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert top_k_frequent([8, 8, 3, 3, 5], 1) == [3]
assert top_k_frequent([-1, -1, -2, -2, 5], 2) == [-2, -1]
assert top_k_frequent([9, 1, 5], 2) == [1, 5]
assert top_k_frequent([7, 7, 7], 1) == [7]
assert top_k_frequent([], 0) == []

print("\nAll tests passed!")


# Part D: Invalid input tests

try:
    top_k_frequent([1, 2], 1.5)
except TypeError:
    print("Invalid k type handled")

try:
    top_k_frequent([1, 2], -1)
except ValueError:
    print("Negative k handled")

try:
    top_k_frequent([1, "hello"], 1)
except TypeError:
    print("Invalid values handled")

try:
    top_k_frequent([7, 7], 2)
except ValueError:
    print("Invalid k range handled")


# Part E: Input mutation test

values = [3, 3, 1, 2]
before = values.copy()

top_k_frequent(values, 2)

assert values == before

print("Input unchanged!")


# Part F: Explain-back checkpoint

# (frequency, -value) works because:
# 1. Lower frequency is weaker.
# 2. If frequencies tie, larger value is weaker.
# 3. Negative value makes the larger number smaller
#    in heap ordering.
# 4. Therefore, the correct weakest candidate
#    stays at the root of the min-heap.