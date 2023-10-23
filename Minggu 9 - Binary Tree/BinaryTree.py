class Node():
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def setRight(self, ri):
        self.right = ri

    def setLeft(self, le):
        self.left = le

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getValue(self):
        return self.key


class Tree():
    def __init__(self):
        self.root = None

    def add(self, key):
        newNode = Node(key)
        if self.root == None:
            self.root = newNode
            print(f'Berhasil insert Node bernilai {key} ke Tree!\n')
            return

        sem = self.root
        if self.contains(key):
            print(
                f'Node dengan nilai {key} sudah ada di Tree, tidak boleh ada duplikat\n')
            return
        else:
            while True:
                if key < sem.getValue():
                    if sem.getLeft() is None:
                        sem.setLeft(newNode)
                        print(
                            f'Berhasil insert Node bernilai {key} ke Tree!\n')
                        return
                    sem = sem.getLeft()
                else:
                    if sem.getRight() is None:
                        sem.setRight(newNode)
                        print(
                            f'Berhasil insert Node bernilai {key} ke Tree!\n')
                        return
                    sem = sem.getRight()

    def contains(self, key):
        sem = self.root
        while sem:
            if key == sem.getValue():
                return True
            sem = sem.getLeft() if key < sem.getValue() else sem.getRight()
        return False

    def remove(self, key):
        def remove_node(node, key):
            if node is None:
                return node

            if key < node.getValue():
                node.setLeft(remove_node(node.getLeft(), key))
            elif key > node.getValue():
                node.setRight(remove_node(node.getRight(), key))
            else:
                if node.getLeft() is None:
                    return node.getRight()
                elif node.getRight() is None:
                    return node.getLeft()
                sem = self.find_min(node.getRight())
                node.key = sem.key
                node.setRight(remove_node(node.getRight(), sem))
            return node

        if self.contains(key):
            self.root = remove_node(self.root, key)
            print(f'Node dengan nilai {key} berhasil dihapus dari Tree!')
        else:
            print(f'Node dengan nilai {key} tidak ditemukan di Tree!')

    def find_min(self, node):
        sem = node
        while sem.getLeft():
            sem = sem.getLeft()
        return sem

    def in_order(self):
        def display_in_order(node):
            if node:
                display_in_order(node.getLeft())
                print(node.getValue(), end=' ')
                display_in_order(node.getRight())
        display_in_order(self.root)
        print()

    def post_order(self):
        def post_order_traversal(node):
            if node:
                post_order_traversal(node.getLeft())
                post_order_traversal(node.getRight())
                print(node.getValue(), end=' ')

        post_order_traversal(self.root)
        print()

    def pre_order(self):
        def pre_order_traversal(node):
            if node:
                print(node.getValue(), end=' ')
                pre_order_traversal(node.getLeft())
                pre_order_traversal(node.getRight())

        pre_order_traversal(self.root)
        print()


# Menginisiasi Tree
tree = Tree()

# Menambahkan node dengan nilai 1-5 ke tree
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)

# Print nilai yang ada di tree
print('Nilai nilai di Node:')
print('In-order: ')
tree.in_order()
print('Pre-order: ')
tree.pre_order()
print('Post-order: ')
tree.post_order()

# Menghapus Node dengan nilai 5 dan 6
tree.remove(5)
tree.remove(6)

# Print nilai di tree setelah menghapus Node dengan nilai 5 dan 6
print('\nNilai di tree setelah remove Node dengan nilai 5 dan 6:')
print('In-order: ')
tree.in_order()
print('Pre-order: ')
tree.pre_order()
print('Post-order: ')
tree.post_order()
