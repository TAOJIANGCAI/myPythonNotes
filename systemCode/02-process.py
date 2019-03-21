from multiprocessing import Process
import os
import time

s = 5


def w1(interval):
    global s
    s += 3
    print("worker_1,⽗进程(%s),当前进程(%s)" % (os.getppid(), os.getpid()))
    start = time.time()
    time.sleep(interval)
    end = time.time()
    print("worker_1,执⾏时间为'%0.2f'秒" % (end - start))
    print(s)


def w2(interval):
    global s
    s += 5
    print("worker_2,⽗进程(%s),当前进程(%s)" % (os.getppid(), os.getpid()))
    start = time.time()
    time.sleep(interval)
    end = time.time()
    print("worker_2,执⾏时间为'%0.2f'秒" % (end - start))
    print(s)


def run():
    print("父进程ID：%s" % os.getpid())
    p1 = Process(target=w1, args=(1,))
    p2 = Process(target=w2, args=(2,))

    # 输出p1和p2进程的别名和pid
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)

    p2.start()
    p1.start()
    # p2.join()
    # 只是阻塞当前主线程，不阻塞子线程p2,jion中带参数表示阻塞当前主线程几秒
    p1.join(10)

    print("p2.is_alive=%s" % p2.is_alive())
    print("p1.is_alive=%s" % p1.is_alive())


if __name__ == "__main__":
    run()
