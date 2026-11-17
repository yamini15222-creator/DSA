
def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


# Test cases
print(contains_duplicate([4, 1, 4]))  # True
print(contains_duplicate([1, 2, 3]))  # False
print(contains_duplicate([]))         # False
print(contains_duplicate([5]))        # False
