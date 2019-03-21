class Dqueue(object):
    def __init__(self):
        self.items = []

    # 从队头加入一个item元素
    def add_front(self, item):
        self.items.insert(0, item)
        pass

    # 从队尾加入一个item元素
    def add_rear(self, item):
        self.items.append(item)

    # 从队头删除一个item元素
    def remove_front(self):
        return self.items.pop(0)

    # 从队尾删除一个item元素
    def remove_rear(self):
        return self.items.pop()

    # 判断双端队列是否为空
    def is_empty(self):
        return self.items is None

    #  返回队列的大小
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    dq = Dqueue()
    dq.add_front(1)
    dq.add_front(2)
    dq.add_rear(4)
    dq.add_rear(5)
    print(dq.size())
    print(dq.remove_front())
    print(dq.remove_rear())
    print(dq.size())
    print(dq.is_empty())
