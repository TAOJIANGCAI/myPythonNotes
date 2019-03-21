nterms = int(input("你需要几项:"))

n1 = 0
n2 = 1
count = 2

if nterms == 1:
    print("fibonacci:%d" % n1)
elif nterms == 2:
    print("fibonacci:%d,%d" % (n1, n2))
elif nterms > 2:
    print(n1, ",", n2, end=",")
    while count < nterms:
        n3 = n1 + n2
        print(n3, end=",")
        count += 1
        n1 = n2
        n2 = n3

# if n == 1:
#     li = [0]
# elif n == 2:
#     li = [0, 1]
# elif n > 2:
#     li = [0, 1]
#     for i in range(2, n):
#         li.append(li[i - 1] + li[i - 2])
#
# print(li)
