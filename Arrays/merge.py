import random

lyst1 = [random.randint(1, 100) for _ in range(10)]
lyst2 = [random.randint(1, 100) for _ in range(10)]

def merge(lyst1, lyst2):
    lyst1.sort()
    lyst2.sort()
    result = []
    i = 0
    j = 0
    length1 = len(lyst1)
    length2 = len(lyst2)
    if not length1:
        return lyst2
    if not length2:
        return lyst1
    while i < length1 and j < length2:
        if lyst1[i] < lyst2[j]:
            result.append(lyst1[i])
            i += 1
        else:
            result.append(lyst2[j])
            j += 1
    if i < length1:
        result.extend(lyst1[i:])
    elif j < length2:
        result.extend(lyst2[j:])
    return result

print(merge(lyst1, lyst2))
