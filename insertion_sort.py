a = [5, 2, 4, 6,1, 3]
#a = [22, 41, 16,104, 35, 123, 24678, 120, 1]

print('unordered array', a)

for i in range(1, len(a)):
    key = a[i]
    j = i - 1

    while(j >= 0 and a[j] > key):
        a[j+1] = a[j]
        j = j - 1

    a[j+1] = key

print('ascending ordered array', a)

b = [5, 2, 4, 6, 1, 3]

for i in range(1, len(b)):
    key = b[i]
    j = i - 1

    while(j >= 0 and b[j] < key):
        b[j+1] = b[j]
        j = j - 1

    b[j+1] = key

print('descending ordered array', b)
