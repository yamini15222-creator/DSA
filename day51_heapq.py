import heapq


def kth_largest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")

    heap = []

    for value in nums:
        if len(heap) < k:
            heapq.heappush(heap, value)

        elif value > heap[0]:
            heapq.heapreplace(heap, value)

    return heap[0]


nums = [3, 2, 1, 5, 6, 4]

print(kth_largest(nums, 2))  # 5
print(kth_largest(nums, 3))  # 4
print(nums)                 # Original list unchanged

assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
assert kth_largest([3, 2, 1, 5, 6, 4], 3) == 4

# Duplicates count separately
assert kth_largest([5, 5, 4], 2) == 5

# Negative values
assert kth_largest([-5, -1, -3], 2) == -3

# One value
assert kth_largest([8], 1) == 8

# Boundary ranks
assert kth_largest([4, 1, 9], 1) == 9
assert kth_largest([4, 1, 9], 3) == 1

# All equal
assert kth_largest([7, 7, 7], 2) == 7

# Input is not mutated
values = [3, 1, 2]
before = values.copy()
assert kth_largest(values, 2) == 2
assert values == before

# Invalid requests
for values, k in [([], 1), ([1, 2], 0), ([1, 2], 3)]:
    try:
        kth_largest(values, k)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")

print("All tests passed!")