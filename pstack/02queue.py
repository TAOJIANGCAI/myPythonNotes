class Queue(object):
    def __init__(self):
        self.items = []

    # 往队尾中添加一个item元素
    def enqueue(self, item):
        self.items.append(item)

    #  从队列头部删除一个元素
    def dequeue(self):
        return self.items.pop(0)

    # 判断一个队列是否为空
    def is_empty(self):
        return self.items is None

    # 返回队列的大小
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.size())
    q.dequeue()
    print(q.size())

