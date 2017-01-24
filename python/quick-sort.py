def quickSort(a, left, right):
    if left >= right:
        return
    l, r = left, right
    k = a[left]
    while left != right:
        while left != right and a[right] >= k:
            right -= 1
        if left == right:
            break
        a[left] = a[right]

        while left != right and a[left] <= k:
            left += 1
        if left == right:
            break
        a[right] = a[left]

    # left equals right
    a[left] = k
    quickSort(array, l, left - 1)
    quickSort(array, left + 1, r)

def quickSort2(a, left, right):
    if left >= right:
        return
    l, r = left, right
    k = a[left]
    while left != right:
        while left != right and a[right] >= k:
            right -= 1
        if left == right:
            break

        while left != right and a[left] <= k:
            left += 1
        if left == right:
            break

        a[left], a[right] = a[right], a[left]

    # left equals right
    a[left], a[l] = a[l], a[left]
    quickSort(array, l, left - 1)
    quickSort(array, left + 1, r)


array = [4,9,8,6,7,2,1,6,7,2,9,3]
origin = array[:]
quickSort(array, 0, len(array) - 1)
print array
print array == sorted(origin)
