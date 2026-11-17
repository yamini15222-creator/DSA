
def shipping_capacity(weights, days):
    if not weights or days <= 0 or days > len(weights):
        return None

    low = max(weights)
    high = sum(weights)

    def can_ship(capacity):
        required_days = 1
        current_load = 0

        for weight in weights:
            if current_load + weight > capacity:
                required_days += 1
                current_load = 0

            current_load += weight

        return required_days <= days

    while low < high:
        mid = (low + high) // 2

        if can_ship(mid):
            high = mid
        else:
            low = mid + 1

    return low


# Test cases
print(shipping_capacity([1, 2, 3, 1, 1], 4))  # 3
print(shipping_capacity([3, 2, 2, 4, 1, 4], 3))  # 6
print(shipping_capacity([1, 2, 3, 4, 5], 1))  # 15
print(shipping_capacity([1, 2, 3], 3))  # 3
