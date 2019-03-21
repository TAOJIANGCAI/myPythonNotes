from multiprocessing import Queue, Process, Manager, Pool
import os, time, random


def write(q):
    for i in ['a', 'b', 'c']:
        print('Put	%s	to	queue...' % i)
        q.put(i)
        time.sleep(random.random())


def read(q):
    while True:
        if not q.empty():
            print('Get	%s	from	queue.' % q.get())
            time.sleep(random.random())
        else:
            break


if __name__ == "__main__":
    # q = Queue()
    # p1 = Process(target=write, args=(q,))
    # p2 = Process(target=read, args=(q,))
    # p1.start()
    # p1.join()
    #
    # p2.start()
    #
    # p2.join()
    #
    # print("end---")
    q = Manager().Queue()

    p = Pool(2)
    p.apply(write, (q,))
    p.apply(read, (q,))
    p.close()
    p.join()
    print("end-----")
