def quick_sort(l, left, right):
    if left >= right:
        return l
    key = l[left]
    low = left
    high = right

    while left < right:
        while left < right and l[right] >= key:
            right -= 1
        l[left] = l[right]
        while left < right and l[left] <= key:
            left += 1
        l[right] = l[left]
    l[right] = key
    quick_sort(l, low, right - 1)
    quick_sort(l, right + 1, high)
    return l

l = [8, 3, 2, 9, 4, 6, 1]
print(quick_sort(l, 0, len(l) - 1))
