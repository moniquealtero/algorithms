def insertion_sort_reversed(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while(j >= 0 and a[j] < key):
            a[j+1] = a[j]
            j = j - 1

        a[j+1] = key

a = [22, 41, 16,104, 35, 123, 24678, 120, 1]

print('unordered array', a)

insertion_sort_reversed(a)

print('descending ordered array', a)


# O(n^2)
