def pre(func):
    def wrapper(*args, **kwargs):
        print("*********************")
        n = func(*args, **kwargs)
        return n

    return wrapper


def middle(func):
    def wrapper(*args, **kwargs):
        print("---------------------")
        n = func(*args, **kwargs)
        return n

    return wrapper


@pre
def login():
    print("welcome to my website ")


print(login())


def test(func):
    def wrapper(num):
        print("------------")
        n = func(num)
        return n

    return wrapper


@test
def test2(num):
    return num
