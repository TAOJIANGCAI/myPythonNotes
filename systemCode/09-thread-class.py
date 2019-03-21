import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print("i am a " + self.name + "\n")


if __name__ == "__main__":
    print("start...")
    for i in range(5):
        t = MyThread()
        t.start()
    print("end...")
