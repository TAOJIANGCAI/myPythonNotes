from multiprocessing import Process, Queue
import os


# 多进程的三种方式：
# 1.from multiprocessing import Process
# 2.创建一个类，继承Process类，重写run方法
# 3.使用from multiprocessing import Pool进程池创建进程

# 进程间的通信:
# 1,from multiprocessing import Process创建的进程，使用from multiprocessing import Queue，q = Queue()
# 2,通过进程池创建的进程，使用from multiprocessing import Manager,q = Manager.Queue()


def run_proc(name):
    print("子进程运行中,name = %s,pid = %d" % (name, os.getpid()))


def run():
    print("父进程id:%d" % os.getppid())
    p = Process(target=run_proc, args=("test",))
    p.start()
    p.join()
    print("子进程结束")


if __name__ == "__main__":
    run()
