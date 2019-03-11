import datetime
import random
import os
from collections import Counter
import time
import re
from multiprocessing import Process, Queue, Pool


# 输入日期， 判断这一天是这一年的第几天？
def day_of_year():
    year = input("请输入年份:")
    month = input("请输入月份:")
    day = input("请输入日:")

    end = datetime.date(year=int(year), month=int(month), day=int(day))
    start = datetime.date(year=int(year), month=1, day=1)

    return (end - start).days + 1


# 内存只有4G无法一次性读入10G的文件，需要分批读入。分批读入数据要记录每次读入数据的位置。要考虑每次读入数据的大小，太小就会在读取操作上花费过多的时间。
def get_lines():
    flag = True
    l = []
    with open("main.c", "r") as f:
        while flag:
            data = f.readlines(2000)
            if data:
                l.append(data)
                yield l
            else:
                flag = False


# 打乱一个排好序的list对象alist？
def test_shuffle():
    l = [1, 2, 3, 4, 5]
    random.shuffle(l)
    print(l)


# 现有字典 d={‘a’:24，‘g’:52，‘i’:12，‘k’:33}请按value值进行排序
def sort_dict_by_value():
    d = {"a": 24, "b": 52, "k": 12, "i": 33}

    # d2 = sorted(d.items(), key=sort_by_value)
    d2 = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return dict(d2)


def sort_by_value(t):
    return t[0]


# 请反转字符串“aStr”?
def reverse_str():
    a = "aStr"
    return a[-1::-1]


# 将字符串"k:1|k1:2|k2:3|k3:4"，处理成字典：{k:1， k1:2， ..
def str_to_dict():
    a = "k:1|k1:2|k2:3|k3:4"
    return {i.split(":")[0]: i.split(":")[1] for i in a.split("|")}


# 写一个列表生成式，产生一个公差为11的等差数列
def gen_list():
    return [11 * i - 10 for i in range(1, 10)]


# 给定两个列表，怎么找出他们相同的元素和不同的元素?
def test_list():
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]

    return (set(b) ^ set(a)), (set(b) & set(a))


# 手写单例模式
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def Singleton(cls):
    isinstance = {}

    def wrapper(*args, **kwargs):
        if cls not in isinstance:
            isinstance[cls] = cls(*args, **kwargs)

        return isinstance[cls]

    return wrapper


@Singleton
class Foo(object):
    pass


f1 = Foo()
f2 = Foo()


# print(f1 is f2)


# 反转一个整数，例如-123-->-321
def reverse_int(a):
    if a < 0:
        return -int(str(abs(a))[::-1])
    else:
        return int(str(abs(a))[::-1])


# E:\pythonProject\interviewPython\cjt
# 设计实现遍历目录与子目录，抓取.pyc文件
def traversal_file():
    # 路径    文件夹名    所有的文件列表
    for parentDir, dirname, filenames in os.walk("E:\pythonProject\interviewPython\cjt", followlinks=True):
        for filename in filenames:
            if filename.endswith(".txt"):
                print(parentDir, filename)
                print(os.path.join(parentDir, filename))


# print(sum([i for i in range(1, 101)]))
# 遍历列表时删除元素的正确做法
def remove_list():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    # remove元素时，后面的元素会向前推进，同时，i的值也会增大，即不能得到想要的值
    # for i in a:
    #     if i > 5:
    #         a.remove(i)
    #     else:
    #         pass
    # b = filter(lambda x: x > 5, a)
    # b = [i for i in a if i > 5]
    # 倒序删除
    for i in range(len(a) - 1, -1, -1):
        if a[i] > 5:
            a.remove(a[i])
    print(a)


# 字符串”123″转换成123，不使用内置api，例如int（）
def str_to_int():
    a = "12345"
    num = 0
    for index, value in enumerate(a[::-1]):
        # eval(str) 将str当成有效的表达式来求值并返回结果
        t = eval(value)
        # ord  它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值
        # t = ord(value) - ord("0")
        num += t * 10 ** index

    return num


# 统计一个文本中单词频次最高的10个单词？
def count_word():
    words = "The ord() function is a pairing function of the chr() function (for 8-bit ASCII strings) or the unichr() function (for Unicode objects). It takes a character (a string of length 1) as a parameter and returns the corresponding An ASCII value, or a Unicode value, raises a TypeError exception if the given Unicode character is outside the scope of your Python definition"
    counts = Counter(words.split(" "))
    return counts.most_common(10)


class a(object):
    def __init__(self):
        print("this a father")


class b(a):
    def __init__(self):
        super().__init__()
        print("this is a son")


class c(b):
    def __init__(self):
        super().__init__()
        print("this is a son son")


class Cat(object):
    def __init__(self, name="kitty"):
        self.name = name

    def sayHi(self):
        print(self.name)


# 使用setattr设置实例属性的值，getattr获取属性的值
# cat = Cat()
# cat.sayHi()
# # cat.__setattr__('name', "hello")
# setattr(cat, "name", "hello")
# cat.sayHi()
# getattr(cat, "sayHi")()
# cat = Cat()
# cat.sayHi()
# print(hasattr(cat, "sayHi"))
# setattr(cat, "name", "hello")
# getattr(cat, "sayHi")()


#
# print([i for i in range(0, 10)])
# print({i: "b" for i in range(0, 10)})
# print({i for i in range(0, 10)})

def test_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)

    return wrapper


# 手写一个判断时间的装饰器
@test_time
def func():
    time.sleep(3)


# 使用Python内置的filter()方法来过滤？
# print(list(filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7, 8])))
from functools import reduce


# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list(map(lambda x: x ** 2, a)))
# print(reduce(lambda x, y: x + y, a))

def compute(a, b, func):
    return func(a, b)


def max(a, b):
    return [a, b][a < b]


def min(a, b):
    return [a, b][a > b]


def sum(a, b):
    return int(a) + int(b)


# 请用“一行代码”实现将1-N的整数列表以3为单位分组
def sort_by_3():
    return [[x for x in range(300)][i:i + 3] for i in range(0, 300, 3)]


# 设置私有属性  1、设置为private + @property  2、通过__setattr__() 来自定义
class Function(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def getName(self):
        return self.__name

    @property
    def getAge(self):
        return self.__age


# f = Function("cjt", 24)
# print(f.getAge)
# print(f.getName)
# f.age = 30
# print(f.getName)


class Function2(object):
    name = "ccjjtt"

    def __init__(self):
        pass

    def __setattr__(self, key, value):
        # print('setting %r = %r' % (key, value))
        if key == "name":
            raise AttributeError("{} is read only".format(key))


# f = Function2()
# f.name = 23

r = re.match(r'(\d+).(\d+).(\d+).(\d+)', "10.3.38.110").group()
# 不管有多少个b替换成一个
b = re.sub(r'b+', 'b', "abbbccc")


# 写出开头匹配字母和下划线，末尾是数字的正则表达式？
# print(re.match(r'^[a-zA-Z_]\w+[0-9]$', "a_tttes9"))


# 请匹配出变量A 中的json字符串
def match_json():
    r = re.compile('({.*?})')
    print(r.match('json_393939({"name": "cjt", "age": 24})'))


# 将表情替换成字符串
def filter_emoji(desstr, restr=''):
    '''
    过滤表情
    '''
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)


def consume(q):
    while True:
        print(q.get())
        if q.empty():
            break


def generate(q):
    for i in range(10):
        q.put(i)


if __name__ == "__main__":
    q = Queue()
    p = Pool(2)
    p.apply_async(generate, (q,))
    p.apply_async(consume, (q,))


