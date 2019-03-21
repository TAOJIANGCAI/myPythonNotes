def select_sort(items):
    n = len(items)
    for j in range(1, n):
        min_index = j - 1
        for i in range(j, n):
            if items[min_index] > items[i]:
                min_index = i
        if min_index != j-1:
            items[min_index], items[j - 1] = items[j - 1], items[min_index]


if __name__ == "__main__":
    li = [5, 10, 8, 6, 13, 9]
    print(li)
    select_sort(li)
    print(li)
