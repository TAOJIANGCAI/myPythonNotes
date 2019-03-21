from threading import Thread, Lock
import time

# 多线程，使用共享全局变量时，应使用互斥锁，以免造成数据的破坏
num = 0


def test1():
    global num
    for i in range(1000000):
        flag = mu.acquire(True)
        if flag:
            num += 1
            mu.release()

    print("---test1---g_num=%d" % num)


def test2():
    global num
    for i in range(1000000):
        flag = mu.acquire(True)
        if flag:
            num += 1
            mu.release()

    print("---test1---g_num=%d" % num)


mu = Lock()
t1 = Thread(target=test1)
t1.start()
# time.sleep(3)
t2 = Thread(target=test1)
t2.start()
# print(num)
