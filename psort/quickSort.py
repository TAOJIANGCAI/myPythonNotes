def quick_sort(items, start, end):
    low = start
    high = end

    if start >= end:
        return

    mid_value = items[start]

    while low < high:

        while low < high and items[high] >= mid_value:
            high -= 1

        items[low] = items[high]

        while low < high and items[low] < mid_value:
            low += 1

        items[high] = items[low]

    items[low] = mid_value

    quick_sort(items, start, low - 1)

    quick_sort(items, low + 1, end)


if __name__ == "__main__":
    li = [5, 10, 8, 6, 13, 9]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
