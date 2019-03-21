import threading, time


def saySorry():
    print("honey,my mistake--")
    time.sleep(1)


if __name__ == "__main__":
    print("start---")
    start = time.time()
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()
        # saySorry()
    end = time.time()

    print("%0.2f" % (end - start))
