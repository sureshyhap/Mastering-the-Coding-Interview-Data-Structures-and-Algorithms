lyst = [2, 5, 1, 2, 3, 5, 1, 2, 4]
lyst2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
lyst3 = [2, 3, 4, 5]

def first_recurring(lyst):
    seen_before = set()
    for num in lyst:
        if num in seen_before:
            return num
        else:
            seen_before.add(num)
    return None

print(first_recurring(lyst))
print(first_recurring(lyst2))
print(first_recurring(lyst3))
