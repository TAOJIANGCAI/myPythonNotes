import threading, time
from threading import Lock


def sing():
    for i in range(3):
        print("sing...%d" % i)
        time.sleep(1)


def dance():
    for i in range(3):
        print("dance...%d" % i)
        time.sleep(1)


if __name__ == "__main__":
    print('---开始---:%s' % time.ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        print('当前运⾏的线程数为：%d' % length)
        if length <= 1:
            break
        time.sleep(0.5)

    print('结束:%s' % time.ctime())
