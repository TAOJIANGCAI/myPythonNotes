a = float(input("请输入三角形的第一个边长:"))
b = float(input("请输入三角形的第二个边长:"))
c = float(input("请输入三角形的第三个边长:"))

s = (a + b + c) // 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("三角形的面积是:%0.2f" % area)
