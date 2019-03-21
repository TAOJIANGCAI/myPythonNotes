class Node(object):
    def __init__(self, elem=-1):
        self.elem = elem
        self.left = None
        self.right = None


class binaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        n = Node(elem)
        if self.root is None:
            self.root = n
            return

        queue = list()
        queue.append(self.root)
        while queue:
            cur = queue.pop(0)
            if cur.left is None:
                cur.left = n
                return
            else:
                queue.append(cur.left)

            if cur.right is None:
                cur.right = n
                return
            else:
                queue.append(cur.right)

    def breadth_search(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            cur = queue.pop(0)
            print(cur.elem)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

    def pre_order(self, item):
        if item is None:
            return
        print(item.elem)
        self.pre_order(item.left)
        self.pre_order(item.right)

    def in_order(self, item):
        if item is None:
            return

        self.in_order(item.left)
        print(item.elem)
        self.in_order(item.right)


bt = binaryTree()
bt.add(1)
bt.add(2)
bt.add(3)
bt.add(4)
bt.add(5)

bt.in_order(bt.root)
