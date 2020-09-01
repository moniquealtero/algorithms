def insertion_sort_ascending(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while(j >= 0 and a[j] > key):
            a[j+1] = a[j]
            j = j - 1

        a[j+1] = key


def insertion_sort_descending(a):
    for i in range(1, len(b)):
        key = b[i]
        j = i - 1

        while(j >= 0 and b[j] < key):
            b[j+1] = b[j]
            j = j - 1

        b[j+1] = key

a = [22, 41, 16,104, 35, 123, 24678, 120, 1]

print('unordered array', a)

insertion_sort_ascending(a)

print('ascending ordered array', a)

b = [22, 41, 16,104, 35, 123, 246, 120, 1]

insertion_sort_descending(b)

print('descending ordered array', b)


# O(n²)
