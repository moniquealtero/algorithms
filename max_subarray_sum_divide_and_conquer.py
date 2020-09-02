def max_crossing_sum(arr, low, mid, high):
    sums = 0
    left_sum = float('-inf')

    for i in range(mid, 0, -1):
        sums = sums + arr[i]

        if(sums > left_sum):
            left_sum = sums

    right_sum = float('-inf')
    sums = 0

    for j in range(mid + 1, high + 1):
        sums = sums + arr[j]

        if(sums > right_sum):
            right_sum = sums

    return max(left_sum + right_sum, left_sum, right_sum)


def max_subarray(arr, low, high):
    if(high == low):
        return(arr[high])

    mid = (low + high)/2

    return max(
        max_subarray(arr, low, mid),
        max_subarray(arr, mid +1, high),
        max_crossing_sum(arr, low, mid, high)
    )

a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

print(max_subarray(a, 0, len(a) - 1))


# O(n log n)
