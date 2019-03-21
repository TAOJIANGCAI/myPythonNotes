from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("%s开始执⾏,进程号为%d" % (msg, os.getpid()))
    # random.random()随机⽣成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执⾏完毕，耗时%0.2f" % (t_stop - t_start))


if __name__ == "__main__":
    po = Pool(3)
    for i in range(10):
        # 非阻塞方式执行
        # po.apply_async(worker, (i,))
        #     阻塞方式执行
        po.apply(worker, (i,))
    print("----start----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有⼦进程执⾏完成，必须放在close语句之后
    print("-----end-----")
