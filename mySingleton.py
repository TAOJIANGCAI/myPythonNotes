import time
import random
import threading


# 1,装饰器 方式
def Singleton(cls):
    _instance = {}

    def singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return singleton


@Singleton
class A(object):
    def __init__(self):
        pass


# 2,自己编写实例类
class MySingleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(random.randint(1, 3))

    # @classmethod
    # def instance(cls, *args, **kwargs):
    #     if not hasattr(MySingleton, '_instance'):
    #         with MySingleton._instance_lock:
    #             MySingleton._instance = MySingleton(*args, **kwargs)
    #     return MySingleton._instance

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_instance'):
    #         cls._instance = super().__new__(cls, *args, **kwargs)
    #     return cls._instance


def test():
    print(MySingleton().instance())


for i in range(5):
    threading.Thread(target=test).start()
