
import heapq


def k_closest(points, k):

    if type(k) is not int:
        raise TypeError("k must be an integer")

    if k < 0 or k > len(points):
        raise ValueError("k must be between 0 and len(points)")

    for point in points:
        if len(point) != 2:
            raise ValueError("Each point must contain x and y")

        x, y = point

        if type(x) is not int or type(y) is not int:
            raise TypeError("Coordinates must be integers")

    if k == 0:
        return []

    heap = []

    for x, y in points:

        distance_squared = x * x + y * y

        candidate = (-distance_squared, -x, -y)

        if len(heap) < k:
            heapq.heappush(heap, candidate)

        elif candidate > heap[0]:
            heapq.heapreplace(heap, candidate)

    ranked = sorted(heap, reverse=True)

    return [
        (-neg_x, -neg_y)
        for distance, neg_x, neg_y in ranked
    ]


# Example 1
points = [(3, 3), (1, 2), (-2, 1), (0, 1)]

print("K Closest Points:")
print(k_closest(points, 2))

# Expected: [(0, 1), (-2, 1)]


# Example 2
points = [(2, 0), (-2, 0), (0, 2), (1, 1), (0, 0)]

print("\n Example:")
print(k_closest(points, 3))

# Expected: [(0, 0), (1, 1), (-2, 0)]
