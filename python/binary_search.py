import math

a = [2, 4, 5, 8]


def binary_search(array, value):
    lo = 0
    hi = len(array)

    while lo < hi:
        m = math.floor(lo + (hi - lo) / 2)

        print(m)

        if array[m] == value:
            return True
        elif array[m] > value:
            hi = m
        elif array[m] < value:
            lo = m + 1

    return False


print(binary_search(a, 5))
print(binary_search(a, 6))
