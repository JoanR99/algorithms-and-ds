a = [31, 41, 59, 26, 41, 58]

for i in range(1, len(a)):
    print(i)
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1

    a[j + 1] = key


for value in a:
    print(value)
