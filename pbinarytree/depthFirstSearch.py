class Tree(object):

    # 前序遍历
    def pre_order(self, root):
        if root is None:
            return

        print(root.elem)
        self.pre_order(root.left)
        self.pre_order(root.right)

    # 中序遍历
    def in_order(self, root):
        if root is None:
            return

        self.in_order(root.left)
        print(root.elem)
        self.in_order(root.right)

    # 后序遍历
    def post_order(self, root):
        if root is None:
            return

        self.post_order(root.left)
        self.post_order(root.right)
        print(root.elem)
