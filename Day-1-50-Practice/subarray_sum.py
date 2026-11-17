
def subarray_sum(nums, k):
    prefix_count = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        needed = current_sum - k

        count += prefix_count.get(needed, 0)

        prefix_count[current_sum] = (
            prefix_count.get(current_sum, 0) + 1
        )

    return count


# Test cases
print(subarray_sum([1, 1, 1], 2))       # 2
print(subarray_sum([1, 2, 3], 3))       # 2
print(subarray_sum([1, -1, 1], 1))      # 3
print(subarray_sum([], 2))              # 0
