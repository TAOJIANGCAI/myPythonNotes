def bubble_sort(items):
    n = len(items)
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]


if __name__ == "__main__":
    li = [5, 10, 8, 6, 13, 9]
    print(li)
    bubble_sort(li)
    print(li)
