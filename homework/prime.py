down = int(input("请输入一个最小数:"))
up = int(input("请输入一个最大数:"))

li = []

for num in range(down, up + 1):

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            li.append(num)
print(li)

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("%d 不是质数" % num)
#             break
#     else:
#         print("%d 是质数" % num)
# else:
#     print("%d 不是质数" % num)
