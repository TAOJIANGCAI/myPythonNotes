def bin_search(items, item):
    n = len(items)
    start = 0
    end = n - 1

    while start < end:
        mid = (start + end) // 2

        if items[mid] == item:
            return True

        if item > items[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


def recursion_search(items, item):
    n = len(items)
    if n == 0:
        return False
    mid = n // 2
    if items[mid] == item:
        return True
    elif items[mid] < item:
        return recursion_search(items[mid + 1:], item)
    else:
        return recursion_search(items[:mid], item)


if __name__ == "__main__":
    li = [1, 2, 3, 4, 6, 7, 8, 9]
    print(recursion_search(li, 4))
    print(recursion_search(li, 5))
