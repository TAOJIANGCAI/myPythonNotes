import time


def test_generator():
    return1 = yield 1

    print(return1, "++++++")

    return2 = yield 2

    print(return2, "-----")

    return3 = yield 3

    print(return3, "******")


t = test_generator()
print(t.send(None))
print(t.send("test2"))
print(t.send("test3"))



def wrapper(func):
    def count_time():
        start = time.time()
        func()
        end = time.time()

        print(end-start)

    return count_time

@wrapper
def func():
    for i in range(10000):
        print(i)


