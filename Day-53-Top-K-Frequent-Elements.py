
import heapq


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
        raise ValueError("k exceeds the number of distinct values")

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

    return [
        -negative_value
        for frequency, negative_value in ranked
    ]


print(top_k_frequent([4, 4, 4, 7, 7, 9], 2))
print(top_k_frequent([8, 8, 3, 3, 5], 1))
print(top_k_frequent([-1, -1, -2, -2, 5], 2))
