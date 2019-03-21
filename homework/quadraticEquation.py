a = float(input("请输入a:"))
b = float(input("请输入b:"))
c = float(input("请输入c:"))

d = b ** 2 - 4 * a * c

x1 = (-b + d ** 0.5) / (2 * a)
x2 = (b + d ** 0.5) / (2 * a)
print('{0},{1}'.format(x1, x2))
