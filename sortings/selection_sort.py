def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if(lst[j] > lst[min]):
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst
print(selection_sort([64, 25, 12, 22, 11]))  # [11, 12, 22, 25, 64]