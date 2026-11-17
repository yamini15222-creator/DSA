
def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result


# Test cases
print(daily_temperatures(
    [73, 74, 75, 71, 69, 72, 76, 73]
))
# [1, 1, 4, 2, 1, 1, 0, 0]

print(daily_temperatures([30, 40, 50, 60]))
# [1, 1, 1, 0]

print(daily_temperatures([30, 20, 10]))
# [0, 0, 0]

print(daily_temperatures([]))
# []
