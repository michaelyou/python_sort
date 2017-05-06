def insert_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0:
            if l[j] > key:
                l[j + 1] = l[j]
                l[j] = key
            j -= 1
    return l


print(insert_sort([3, 5, 1, 3, 1]))
