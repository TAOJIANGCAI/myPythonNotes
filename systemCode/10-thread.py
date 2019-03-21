import threading, time

num = 100


def w1():
    global num
    for i in range(3):
        num += 2

    print("----in	work1,	g_num	is	%d---" % num)


def w2():
    global num
    for i in range(3):
        num += 2

    print("----in	work2,	g_num	is	%d---" % num)


t1 = threading.Thread(target=w1)
t1.start()
time.sleep(2)
t2 = threading.Thread(target=w2)
t2.start()
