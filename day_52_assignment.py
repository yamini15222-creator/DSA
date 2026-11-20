
from day_52_kth_largest import KthLargest


def part_a():
    print("PART A: Add values to the stream")

    k = 3
    initial_values = [6, 2]
    incoming_values = [4, 8, 1, 10, 8]

    tracker = KthLargest(k, initial_values)

    for value in incoming_values:
        answer = tracker.add(value)

        print(
            "Added:", value,
            "| Kth Largest:", answer,
            "| Heap:", sorted(tracker.heap)
        )


def part_b():
    print("\nPART B: Peek operation")

    tracker = KthLargest(2, [10])

    print("Before enough values:", tracker.peek())

    print("After adding 7:", tracker.add(7))

    print("Peek again:", tracker.peek())

    print("Peek once more:", tracker.peek())




def part_c():
    print("\nPART C: Reference comparison")

    k = 3
    history = [6, 2]

    tracker = KthLargest(k, history)

    for value in [4, 8, 1, 10, 8]:

        history.append(value)

        actual = tracker.add(value)

        expected = (
            sorted(history, reverse=True)[k - 1]
            if len(history) >= k
            else None
        )

        print(
            "Added:", value,
            "| Heap Answer:", actual,
            "| Expected:", expected
        )

        assert actual == expected

    print("Reference comparison passed!")


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
