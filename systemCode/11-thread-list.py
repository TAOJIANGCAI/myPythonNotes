import threading


# 多进程不能共享全局变量，多线程可以共享全局变量（共享内存）

def w1(nums):
    nums.append(44)
    print("----in	work1---", nums)


def w2(nums):
    nums.append(55)
    print("----in	work1---", nums)


nums = [11, 22, 33]
t1 = threading.Thread(target=w1, args=(nums,))
t1.start()
t2 = threading.Thread(target=w2, args=(nums,))
t2.start()
