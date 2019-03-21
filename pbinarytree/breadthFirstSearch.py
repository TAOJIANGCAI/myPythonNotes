def breadth_search(self, root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        cur = queue.pop(0)
        print(cur.elem, end="")
        if cur.left is not None:
            queue.append(cur.left)
        elif cur.right is not None:
            queue.append(cur.right)
