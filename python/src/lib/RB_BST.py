from binary_search_tree import BST

class RBBSTNode:
    def __init__(self, data=None):
        self.p = None
        self.left = None
        self.right = None
        self.color = None
        self.key = data


class RBBST(BST):
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.p = x
        y.p = x.p
        if not x.p:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.p = x
        y.p = x.p
        if not x.p:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def rb_insert(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if not y:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = None
        z.right = None
        z.color = 'RED'
        self.rb_insert_fixup(z)
        self.inorder_tree_walk()
        print('aaaa')

    def rb_insert_fixup(self, z):
        if not z.p:
            z.color = 'RED'
            return
        while z.p and z.p.color == 'RED':
            if z.p.p:
                if z.p is z.p.p.left:
                    y = z.p.p.right
                    if y and y.color == 'RED':
                        z.p.color = 'BLACK'
                        y.color = 'BLACK'
                        z.p.p.color = 'RED'
                        if z.p.p:
                            z = z.p.p
                    elif z is z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    if z and z.p:
                        z.p.color = 'BLACK'
                    if z and z.p and z.p.p:
                        z.p.p.color = 'RED'
                    if z and z.p and z.p.p:
                        self.right_rotate(z.p.p)
                else:
                    y = z.p.p.left
                    if y and y.color == 'RED':
                        z.p.color = 'BLACK'
                        y.color = 'BLACK'
                        z.p.p.color = 'RED'
                        if z.p.p:
                            z = z.p.p
                    elif z is z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    if z and z.p:
                        z.p.color = 'BLACK'
                    if z and z.p and z.p.p:
                        z.p.p.color = 'RED'
                    if z and z.p and z.p.p:
                        self.left_rotate(z.p.p)

            self.root.color = 'BLACK'

    def inorder_tree_walk(self, mode=None, x=None):
        # mode 0: from root
        if not mode:
            x = self.root
        if x and x.key:
            self.inorder_tree_walk(mode=1, x=x.left)
            print(x.key, x.color)
            self.inorder_tree_walk(mode=1, x=x.right)

if __name__ ==  "__main__":
    a = [1, 2, 4, 5, 7, 8, 11, 14, 15]
    T = RBBST()
    for i in a:
        z = RBBSTNode(i)
        T.rb_insert(z)
    T.inorder_tree_walk()
