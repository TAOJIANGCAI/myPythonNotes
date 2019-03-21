import time


# 冒泡排序
def bubble_sort(items):
    length = len(items)
    for x in range(length - 1):
        for y in range(x, length):
            if items[x] >= items[y]:
                items[x], items[y] = items[y], items[x]


# 选择排序
def selection_sort(items):
    length = len(items)

    for x in range(length):
        min_index = x
        for y in range(x + 1, length):
            if items[min_index] >= items[y]:
                min_index = y
        if min_index != x:
            items[x], items[min_index] = items[min_index], items[x]


start = time.time()
li = [4, 6, 5, 8, 7]
selection_sort(li)
end = time.time()
print(end-start,li)
# print("选择排序耗时:%d" % t)
