
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
