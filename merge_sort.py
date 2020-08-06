def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(0, n1):
        L[i] = a[p + i]

    for j in range(0, n2):
        R[j] = a[q + 1 + j]

    L[n1] = float('inf')
    R[n2] = float('inf')

    i = 0
    j = 0

    for k in range(p, r+1):
        if(L[i] <= R[j]):
            a[k] = L[i]
            i = i +1
        else:
            a[k] = R[j]
            j = j + 1

def merge_sort(a, p, r):
    if(p < r and r > 0):
        q = (p + ( r-1 ))//2

        merge_sort(a, p, q)
        merge_sort(a, q +1, r)
        merge(a, p, q, r)

a = [2, 3, 5, 1, 5, 9, 7, 2, 8, 123214, 2421, 123214, 421454, 123, 124, 4]

merge_sort(a, 0, len(a) - 1)

print(a)
