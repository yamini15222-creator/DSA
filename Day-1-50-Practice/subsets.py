
def subsets(nums):
    result = []
    path = []

    def backtrack(start):
        # Save a copy of the current subset
        result.append(path.copy())

        for i in range(start, len(nums)):
            # Choose
            path.append(nums[i])

            # Explore
            backtrack(i + 1)

            # Undo
            path.pop()

    backtrack(0)
    return result


# Test cases
print(subsets([1, 2]))
# [[], [1], [1, 2], [2]]

print(subsets([1, 2, 3]))
# All 8 subsets

print(subsets([]))
# [[]]

print(subsets([5]))
# [[], [5]]
