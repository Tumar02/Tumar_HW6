def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def binary_search(lst, n):
    n = len(lst)
    first = 0
    last = n-1
    while first < last:
        middle = first+last//2
        if lst[middle] == n:
            return f'Element has found {middle}'
        elif lst[middle] < n:
            first = middle+1
        else:
            last = middle-1
            return f'Element not found'


lst = [1, 2, 10, 8]
print(bubble_sort(lst))
print(binary_search(lst, 10))
