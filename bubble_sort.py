def bubble_sort(l):
    for i in range(0, len(l)):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
    return l

print(bubble_sort([5, 1, 2, 1, 3]))
                
