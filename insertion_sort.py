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

print('ordered array', a)
