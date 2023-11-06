class Node:
    # if color = 0 -> red
    # if color = 1--> black
    def __init__(self, key, value, descID, descEN): 
        self.key = key
        self.value = value
        self.descID = descID
        self.descEN = descEN
        self.parent = None
        self.right = None
        self.left = None
        self.color = 0


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, None, None, None)
        self.nil.color = 1
        self.root = self.nil


    def search_en(self, value):
        value = value.lower()

        def travers_in_order(node, value):
            if node == self.nil:
                return 'Not Found'

            if node.value == value:
                return node.key

            result_left = travers_in_order(node.left, value)
            if result_left != 'Not Found':
                return result_left

            return travers_in_order(node.right, value)

        return travers_in_order(self.root, value)


    def search_id(self, kata):
        kata = kata.lower()
        def travers_in_order(node, kata):
            if node == self.nil:
                return 'Not Found'

            if node.key == kata:
                return node.value

            result_left = travers_in_order(node.left, kata)
            if result_left != 'Not Found':
                return result_left

            return travers_in_order(node.right, kata)
        return travers_in_order(self.root, kata)

    def search_descen(self, value):
        value = value.lower()

        def travers_in_order(node, value):
            if node == self.nil:
                return 'Not Found'

            if node.value == value:
                return node.descEN

            result_left = travers_in_order(node.left, value)
            if result_left != 'Not Found':
                return result_left

            return travers_in_order(node.right, value)

        return travers_in_order(self.root, value)


    def search_descid(self, kata):
        kata = kata.lower()
        def travers_in_order(node, kata):
            if node == self.nil:
                return 'Not Found'

            if node.key == kata:
                return node.descID

            result_left = travers_in_order(node.left, kata)
            if result_left != 'Not Found':
                return result_left

            return travers_in_order(node.right, kata)
        return travers_in_order(self.root, kata)

    def insert(self, key, value, descID, descEN):
        newNode = Node(key.lower(), value.lower(), descID, descEN)
        newNode.left = self.nil
        newNode.right = self.nil
        node = self.root
        parent = None

        while node != self.nil: 
            parent = node
            if newNode.key < node.key:
                node = node.left
            else:
                node = node.right
        newNode.parent = parent

        if parent is None:
            newNode.color = 1
            self.root = newNode
            return
        elif newNode.key < parent.key:
            parent.left = newNode
        else:
            parent.right = newNode

        if newNode.parent.parent is None:
            return

        self.balance(newNode)


    def balance(self, newNode):
        while newNode != self.root and newNode.parent.color == 0:

            parentIsLeft = False

            if newNode.parent == newNode.parent.parent.left:
                uncle = newNode.parent.parent.right
                parentIsLeft = True
            else:
                uncle = newNode.parent.parent.left

            if uncle.color == 0:
                newNode.parent.color = 1
                uncle.color = 1
                newNode.parent.parent.color = 0
                newNode = newNode.parent.parent
            else:
                if parentIsLeft and newNode == newNode.parent.right:
                    newNode = newNode.parent
                    self.leftRotate(newNode)
                elif not parentIsLeft and newNode == newNode.parent.left:
                    newNode = newNode.parent
                    self.rightRotate(newNode)
                if parentIsLeft:
                    newNode.parent.color = 1 
                    newNode.parent.parent.color = 0 
                    self.rightRotate(newNode.parent.parent)
                else:
                    newNode.parent.color = 1
                    newNode.parent.parent.color = 0
                    self.leftRotate(newNode.parent.parent)

        self.root.color = 1 


    def leftRotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.nil:
            y.left.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node
        node.parent = y


    def rightRotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.nil:
            y.right.parent = node
        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.right = node
        node.parent = y


    def print_tree_id(self):
        def helperPrintId(node, indent, last):
            if node != self.nil:
                print(indent, end=' ')
                if last:
                    print("R----", end=' ')
                    indent += "     "
                else:
                    print("L----", end=' ')
                    indent += "|    "

                s_color = "RED" if node.color == 0 else "BLACK"
                print(str(node.key) + "(" + s_color + ")")
                helperPrintId(node.left, indent, False)
                helperPrintId(node.right, indent, True)
        
        helperPrintId(self.root, "", True)

    def print_tree_en(self):
        def helperPrintEn(node, indent, last):
            if node != self.nil:
                print(indent, end=' ')
                if last:
                    print("R----", end=' ')
                    indent += "     "
                else:
                    print("L----", end=' ')
                    indent += "|    "

                s_color = "RED" if node.color == 0 else "BLACK"
                print(str(node.value) + "(" + s_color + ")")
                helperPrintEn(node.left, indent, False)
                helperPrintEn(node.right, indent, True)
        
        helperPrintEn(self.root, "", True)