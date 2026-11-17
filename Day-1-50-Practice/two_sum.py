
def two_sum(nums, target):
    seen = {}

    for index, value in enumerate(nums):
        needed = target - value

        if needed in seen:
            return [seen[needed], index]

        seen[value] = index

    return None


# Test cases
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))      # [1, 2]
print(two_sum([3, 3], 6))         # [0, 1]
print(two_sum([1, 2, 3], 10))     # None
