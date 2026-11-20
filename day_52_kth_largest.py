
import heapq


class KthLargest:
    def __init__(self, k, initial_values=()):
        if isinstance(k, bool) or not isinstance(k, int):
            raise TypeError("k must be an integer")

        if k < 1:
            raise ValueError("k must be positive")

        self.k = k
        self.heap = []

        for value in initial_values:
            self.add(value)

    def add(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("score must be an integer")

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, value)

        elif value > self.heap[0]:
            heapq.heapreplace(self.heap, value)

        return self.peek()

    def peek(self):
        if len(self.heap) < self.k:
            return None

        return self.heap[0]


# ---------------- AUTOMATED TESTS ----------------

def test_standard_example():
    tracker = KthLargest(3, [4, 5, 8, 2])
    results = [tracker.add(x) for x in [3, 5, 10, 9, 4]]
    assert results == [4, 5, 5, 8, 8]


def test_assignment_example():
    tracker = KthLargest(3, [6, 2])
    results = [tracker.add(x) for x in [4, 8, 1, 10, 8]]
    assert results == [2, 4, 4, 6, 8]


def test_peek():
    tracker = KthLargest(2, [10])
    assert tracker.peek() is None
    assert tracker.add(7) == 7
    assert tracker.peek() == 7


def test_duplicates():
    tracker = KthLargest(2, [5, 5, 5])
    assert tracker.peek() == 5
    assert tracker.add(5) == 5


def test_negative_values():
    tracker = KthLargest(2, [-10, -3, -7])
    assert tracker.peek() == -7
    assert tracker.add(-1) == -3


def test_k_equals_one():
    tracker = KthLargest(1, [2, 8, 4])
    assert tracker.peek() == 8
    assert tracker.add(10) == 10


def test_independent_instances():
    first = KthLargest(2, [1, 5])
    second = KthLargest(2, [10, 20])

    first.add(7)

    assert first.peek() == 5
    assert second.peek() == 10


def test_input_not_modified():
    values = [4, 1, 9]
    original = values.copy()

    KthLargest(2, values)

    assert values == original


def test_sorting_reference():
    k = 3
    history = [6, 2]
    tracker = KthLargest(k, history)

    for value in [4, 8, 1, 10, 8, 12]:
        history.append(value)

        expected = (
            sorted(history, reverse=True)[k - 1]
            if len(history) >= k
            else None
        )

        assert tracker.add(value) == expected


def test_invalid_inputs():
    for invalid_k in [0, -1]:
        try:
            KthLargest(invalid_k)
        except ValueError:
            pass
        else:
            raise AssertionError("Expected ValueError")

    for invalid_k in [2.5, "3", True]:
        try:
            KthLargest(invalid_k)
        except TypeError:
            pass
        else:
            raise AssertionError("Expected TypeError")

    tracker = KthLargest(2)

    for invalid_score in ["hello", 3.5, True]:
        try:
            tracker.add(invalid_score)
        except TypeError:
            pass
        else:
            raise AssertionError("Expected TypeError")


def run_all_tests():
    tests = [
        test_standard_example,
        test_assignment_example,
        test_peek,
        test_duplicates,
        test_negative_values,
        test_k_equals_one,
        test_independent_instances,
        test_input_not_modified,
        test_sorting_reference,
        test_invalid_inputs
    ]

    for test in tests:
        test()
        print("PASS:", test.__name__)

    print("\nAll tests passed!")


if __name__ == "__main__":
    run_all_tests()
