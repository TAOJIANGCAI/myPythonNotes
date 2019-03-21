num = input("请输入一个数:")

n = len(num)
sum = 0
num = int(num)

while True:
    i = num % 10
    sum += i ** n
    num = num // 10
    if num == 0:
        break
print(sum)
