
def bubble(a):
    for i in range(0, len(a)):
        for j in range(len(a) - 1, i, -1):
            if(a[j] < a[j-1]):
                k = a[j]
                a[j] = a[j-1]
                a[j-1] = k

a = [12, 1, 4, 7, 20, 2, 5, 8]

print('unordered array', a)

bubble(a)

print('ordered array', a)

# O(n^2)
