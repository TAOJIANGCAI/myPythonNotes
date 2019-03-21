def shell_sort(items):
    n = len(items)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            for i in range(j, 0, -gap):
                if items[i] < items[i - gap]:
                    items[i - gap], items[i] = items[i], items[i - gap]

        gap //= 2


if __name__ == "__main__":
    li = [5, 10, 8, 6, 13, 9]
    print(li)
    shell_sort(li)
    print(li)
