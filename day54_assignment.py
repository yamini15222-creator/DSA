
import heapq

# Part A: Predict before running

points = [(2, 0), (-2, 0), (0, 2), (1, 1), (0, 0)]
k = 3

print("Part A:")
print("Input:", points)
print("K:", k)


# Part B: Implement K Closest Points to Origin

def k_closest(points, k):

    if type(k) is not int:
        raise TypeError("k must be an integer")

    if k < 0 or k > len(points):
        raise ValueError("Invalid k value")

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


print("\nPart B:")
print(k_closest(points, k))

# Expected: [(0, 0), (1, 1), (-2, 0)]


# Part C: K Closest Points to Any Center

def k_closest_to(points, k, center):

    if type(k) is not int:
        raise TypeError("k must be an integer")

    if k < 0 or k > len(points):
        raise ValueError("Invalid k value")

    if len(center) != 2:
        raise ValueError("Center must contain x and y")

    cx, cy = center

    if type(cx) is not int or type(cy) is not int:
        raise TypeError("Center coordinates must be integers")

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

        distance_squared = (x - cx) ** 2 + (y - cy) ** 2

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


print("\nPart C:")
print(k_closest_to(
    [(0, 0), (3, 1), (2, 2)],
    2,
    center=(2, 1)
))

# Expected: [(2, 2), (3, 1)]


# Part D: Verify against sorting

points = [(3, 3), (1, 2), (-2, 1), (0, 1)]
k = 2

expected = sorted(
    points,
    key=lambda point: (
        point[0] ** 2 + point[1] ** 2,
        point[0],
        point[1]
    )
)[:k]

actual = k_closest(points, k)

print("\nPart D:")
print("Expected:", expected)
print("Actual:", actual)

assert actual == expected

print("Sorting verification successful!")


# Part E: Test K Closest to Any Center against sorting

points = [(0, 0), (3, 1), (2, 2)]
center = (2, 1)
k = 2

cx, cy = center

expected = sorted(
    points,
    key=lambda point: (
        (point[0] - cx) ** 2 + (point[1] - cy) ** 2,
        point[0],
        point[1]
    )
)[:k]

actual = k_closest_to(points, k, center)

print("\nPart E:")
print("Expected:", expected)
print("Actual:", actual)

assert actual == expected

print("Center sorting verification successful!")


# Part F: Additional test cases

# Same distance: smaller x wins
assert k_closest([(1, 2), (-2, 1)], 1) == [(-2, 1)]

# Same distance and x: smaller y wins
assert k_closest([(1, 2), (1, -2)], 1) == [(1, -2)]

# Duplicate points count separately
assert k_closest(
    [(2, 0), (0, 0), (0, 0)], 2
) == [(0, 0), (0, 0)]

# K = 0
assert k_closest([], 0) == []

# K = number of points
assert k_closest(
    [(2, 0), (0, 0)], 2
) == [(0, 0), (2, 0)]

print("\nAll additional tests passed!")


# Part G: Invalid K tests

try:
    k_closest([(1, 2)], -1)
except ValueError:
    print("Negative k handled")

try:
    k_closest([(1, 2)], 2)
except ValueError:
    print("Invalid k range handled")

try:
    k_closest([(1, 2)], 1.5)
except TypeError:
    print("Invalid k type handled")


# Part H: Input mutation test

values = [(3, 3), (1, 2), (0, 1)]
before = values.copy()

k_closest(values, 2)

assert values == before

print("Input unchanged!")


# Part I: Explain-back checkpoint

# Points: (1, 2) and (1, -2)
#
# Distance squared for both points = 5
#
# (1, 2)  -> (-5, -1, -2)
# (1, -2) -> (-5, -1, 2)
#
# The second key is larger.
# Therefore, (1, -2) wins because smaller y wins.

print("\nExplain-back:")
print("(1, -2) wins because smaller y wins.")

print("\nAll Day 54 tests passed!")
