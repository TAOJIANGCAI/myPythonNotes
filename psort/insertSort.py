def insert_sort(items):
    n = len(items)
    for j in range(1, n):
        for i in range(j, 0, -1):
            if items[i] < items[i - 1]:
                items[i - 1], items[i] = items[i], items[i - 1]

    # for j in range(1, n):
    # i = j
    # while i > 0:
    #     if items[i] < items[i - 1]:
    #         items[i - 1], items[i] = items[i], items[i - 1]
    #         i -= 1
    #     else:
    #         break


if __name__ == "__main__":
    li = [5, 10, 8, 6, 13, 9]
    print(li)
    insert_sort(li)
    print(li)
