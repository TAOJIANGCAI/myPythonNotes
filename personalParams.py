class PersonalParam(object):
    def __init__(self):
        # 单前下划线，类对象和子类可以访问，但from somemodule import *禁止导入
        self._num = 3
        # 双前下划线，无法在外部直接访问
        self.__num = 4
        # 双前后下划线，系统定义名字
        self.__num__ = 5
        # 单后置下划线，用于避免与Python关键词的冲突
        self.num_ = 6

    # 对类私有属性的访问方式：
    # 1,getter和setter
    def getNum(self):
        return self.__num

    def setNum(self, value):
        self.__num = value

    # 2.property()
    num = property(getNum, setNum)

    # 3,@property
    @property
    def num2(self):
        return self.__num

    @num2.setter
    def num2(self, value):
        self.__num = value


p = PersonalParam()
# print(p._num, p.__num__, p.num_, dir(p))
# 次方法可以访问双前下划线定义的私有变量，但不推荐
# print(p._PersonalParam__num)

# 1,getter  setter
# p.set_num(10)
# print(p.get_num())


# 2,property()
# print(p.num)
# p.num = 10
# print(p.num)


# 3,@property
print(p.num2)
p.num2 = 50
print(p.num2)
