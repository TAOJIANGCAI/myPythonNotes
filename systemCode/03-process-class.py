from multiprocessing import Process
import time
import os


# 继承Process类
class Process_class(Process):

    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print("⼦进程({})开始执⾏，⽗进程({})".format(os.getpid(), os.getppid()))
        start = time.time()
        time.sleep(self.interval)
        end = time.time()
        print("({})执⾏结束，耗时{}秒".format(os.getpid(), end - start))


if __name__ == "__main__":
    t_start = time.time()
    print("当前程序进程(%s)" % os.getpid())
    p1 = Process_class(2)
    # 对⼀个不包含target属性的Process类执⾏start()⽅法，就会运⾏这个类中的run()⽅法
    p1.start()
    p1.join()
    t_stop = time.time()
    print("(%s)执⾏结束，耗时%0.2f" % (os.getpid(), t_stop - t_start))
