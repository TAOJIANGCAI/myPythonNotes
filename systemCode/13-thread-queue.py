import threading, time
from queue import Queue


class Producer(threading.Thread):
    def run(self):
        global q
        for i in range(100):
            q.put(i)


        print(q.qsize())


class Consumer(threading.Thread):
    def run(self):
        global q
        time.sleep(1)
        for i in range(100):
            print(q.get())


if __name__ == "__main__":
    q = Queue()
    p = Producer()
    c = Consumer()
    p.start()
    # time.sleep(3)
    c.start()
