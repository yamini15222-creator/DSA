
def maximum_sum_window(nums, k):
    if k <= 0 or k > len(nums):
        return None

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]

        max_sum = max(max_sum, window_sum)

    return max_sum


# Test cases
print(maximum_sum_window([2, 1, 5, 1, 3, 2], 3))  # 9
print(maximum_sum_window([1, 2, 3, 4], 2))        # 7
print(maximum_sum_window([-2, -1, -5], 2))        # -3
print(maximum_sum_window([1, 2], 3))              # None
