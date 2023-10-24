class Node:
    def __init__(self, key, red=True, parent=None, left=None, right=None):
        self.key = key
        self.red = red
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(None)
        self.TNULL.red = False
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def contain(self, key):
        sem = self.root
        while sem != self.TNULL:
            if sem.key == key:
                return True
            sem = sem.left if key < sem.key else sem.right
        return False

    def add(self, key):
        node = Node(key)
        if self.root is self.TNULL:
            self.root = node
            self.root.red = False
        else:
            parent = None
            current = self.root
            while current != self.TNULL:
                parrent = current
                if node.key < current.key:
                    current = current.left
                else:
                    current = current.right
            node.parent = parent
            if node.key < parent.key:
                parent.left = node
            else:
                parent.right = node

            self.balance(node)

    def addrec(self, sek, node):
        if node.key < sek.key:
            if sek is self.TNULL:
                sek = node
                node.parent = sek
            else:
                self.addrec(sek.left, node)
        else:
            if sek is self.TNULL:
                sek = node
                node.parent = sek
            else:
                self.addrec(sek.right, node)
        # node = Node(key)
        # node.parent = None
        # node.right = self.TNULL
        # node.left = self.TNULL
        # node.red = True

        # y = None
        # x = self.root

        # if self.contain(key):
        #     print(f'Node dengan nilai {key} sudah ada di tree')
        #     return

        # if self.root == self.TNULL:
        #     self.root = node
        # else:
        #     while x == self.TNULL:
        #         y = x
        #         x = x.left if key < x.key else x.right
        #     node.parent = y
        #     if y == None:
        #         self.root = node
        #         print(f'Berhasil insert node dengan nilai {key} ke tree')
        #     elif node.key < y.key:
        #         y.left = node
        #         print(f'Berhasil insert node dengan nilai {key} ke tree')
        #     else:
        #         y.right = node
        #         print(f'Berhasil insert node dengan nilai {key} ke tree')

        #     if node.parent == None:
        #         node.red = False
        #         return

        #     if node.parent.parent == None:
        #         return

        #     self.balance(node)

    def balance(self, node):
        while node.red:
            if node.parent == node.parent.parent.right:
                paman = node.parent.parent.left
                if paman.red:
                    paman.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotateToRight(node)
                    node.parent.red = False
                    node.parent.parent = True
                    print("Melakukan `Left Rotate` untuk menyeimbangkan tree")
                    self.rotateToLeft(node.parent.parent)
            else:
                node1 = node.parent.parent.right
                if node1 == True:
                    node1.red = False
                    node.parent.red = False
                    node.parent.parent.red = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node - node.parent
                        print("Melakukan `Right Rotate` untuk menyeimbangkan tree")
                        self.rotateToLeft(node.parent.parent)
            if node == self.root:
                break
        self.root.red = False

    def in_order(self):
        def display_in_order(node):
            if node != self.TNULL:
                display_in_order(node.left)
                print(node.key)
                display_in_order(node.right)
        display_in_order(self.root)
        print()

    def post_order(self):
        def post_order_traversal(node):
            if node != self.TNULL:
                post_order_traversal(node.left)
                post_order_traversal(node.right)
                print(node.key, end=' ')

        post_order_traversal(self.root)
        print()

    def pre_order(self):
        def pre_order_traversal(node):
            if node != self.TNULL:
                print(node.key, end=' ')
                pre_order_traversal(node.left)
                pre_order_traversal(node.right)

        pre_order_traversal(self.root)
        print()

    def rotateToRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y
        # print("Melakukan `Right Rotate` untuk menyeimbangkan tree")

    def rotateToLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y
        # print("Melakukan `Left Rotate` untuk menyeimbangkan tree")
