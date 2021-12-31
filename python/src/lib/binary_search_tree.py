class BSTNode:
    def __init__(self, data=None):
        self.p = None
        self.left = None
        self.right = None
        self.key = data


class BST:
    def __init__(self):
        self.root = None

    def tree_insert(self, z):
        if not self.root:
            self.root = z
            return
        y = None
        x = self.root
        while x and x.key:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if z.key < y.key:
            y.left = z
        else:
            y.right = z

    @staticmethod
    def tree_search(x, k):
        # if not x or k == x.key:
        #     return x
        # if k < x.key:
        #     return self.tree_search(x.left, k)
        # else:
        #     return self.tree_search(x.right, k)

        while x and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    @staticmethod
    def tree_minimum(x):
        while x.left:
            x = x.left
        return x

    @staticmethod
    def tree_maximum(x):
        while x.right:
            x = x.right
        return x

    def tree_successor(self, x):
        if x.right:
            return self.tree_minimum(x.right)
        y = x.p
        while y and x == y.right:
            x = y
            y = y.p
        return y

    def tree_predecessor(self, x):
        if x.left:
            return self.tree_maximum(x.left)
        y = x.p
        while y and x == y.left:
            x = y
            y = y.p
        return y

    def transplant(self, u, v):
        if not u.p:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v:
            v.p = u.p

    def tree_delete(self, z):
        if not z.left:
            # p167 (a)
            self.transplant(z, z.right)
        elif not z.right:
            # p167 (b)
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.p is not z:
                # p167 (d)
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            # p167 (c)
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

    def inorder_tree_walk(self, mode=None, x=None):
        # mode 0: from root
        if not mode:
            x = self.root
        if x and x.key:
            self.inorder_tree_walk(mode=1, x=x.left)
            print(x.key)
            self.inorder_tree_walk(mode=1, x=x.right)


if __name__ == "__main__":
    a = [10, 11, 7, 3, 6]
    T = BST()
    for i in a:
        z = BSTNode(i)
        T.tree_insert(z)
    T.inorder_tree_walk()
    x = T.tree_search(T.root, 7)
    print('search: ', x.key)
    print('max: ', T.tree_maximum(T.root).key)
    print('min: ', T.tree_minimum(T.root).key)
    print('successor: ', T.tree_successor(T.root.right))
    print('predecessor: ', T.tree_predecessor(T.root.right).key)
    T.tree_delete(T.root)
