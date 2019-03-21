def merge_sort(items):
    n = len(items)
    mid = n // 2

    if len(items) == 1:
        return items

    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    result = []

    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1

    result += left[l:]
    result += right[r:]

    return result


if __name__ == "__main__":
    li = [5, 10, 8, 6, 13, 9]
    print(li)
    print(merge_sort(li))
