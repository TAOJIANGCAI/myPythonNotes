m = int(input("请输入一个数:"))
n = int(input("请输入一个数:"))

if m < n:
    m, n = n, m

for i in range(2, n + 1):
    if (n % i == 0 and m % i == 0):
        hcf = i

# 最小公倍数
t = m * n // hcf

print(hcf, t)
