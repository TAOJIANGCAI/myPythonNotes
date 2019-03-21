class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        # 添加一个新的元素item到栈顶
        self.items.append(item)

    def pop(self):
        # 弹出栈顶元素
        self.items.pop()

    # 返回栈顶元素
    def peek(self):
        return self.items.pop()

    #  判断栈是否为空
    def is_empty(self):
        return self.items is None

    # 返回栈的元素个数
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.peek())
    print(s.size())