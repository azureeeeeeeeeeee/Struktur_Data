class Node:
    # if color = 0 -> red
    # if color = 1--> black
    def __init__(self, key, arti):  # Constructor
        self.key = key  # Node needs a key to be initialized
        self.arti = arti
        self.parent = None
        self.right = None
        self.left = None
        self.color = 0


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, None)
        self.nil.color = 1  # The root and the nil are black
        self.root = self.nil
        self.number_of_nodes = 0


    
    def search_en(self, arti):
        arti = arti.lower()

        def travers_in_order(node, arti):
            if node == self.nil:
                return 'Not Found'

            if node.arti == arti:
                return node.key  # Change 'kata' to 'key' to return the ID

            result_left = travers_in_order(node.left, arti)
            if result_left != 'Not Found':
                return result_left

            return travers_in_order(node.right, arti)

        return travers_in_order(self.root, arti)

    def search_id(self, kata):
        kata = kata.lower()
        def travers_in_order(node, kata):
            if node == self.nil:
                return 'Not Found'

            if node.key == kata:
                return node.arti

            result_left = travers_in_order(node.left, kata)
            if result_left != 'Not Found':
                return result_left

            return travers_in_order(node.right, kata)
        return travers_in_order(self.root, kata)


    def insert(self, key, arti):
        newNode = Node(key.lower(), arti.lower())  # Convert to lowercase only for internal storage
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
            self.number_of_nodes += 1
            return
        elif newNode.key < parent.key:
            parent.left = newNode
        else:
            parent.right = newNode

        if newNode.parent.parent is None:  # Parent is the root
            self.number_of_nodes += 1
            return

        self.insertFix(newNode)
        self.number_of_nodes += 1

    def insertFix(self, newNode):
        # Loop until we reach the root or parent is black
        while newNode != self.root and newNode.parent.color == 0:

            parentIsLeft = False  # Parent is considered left child by default

            # Assign uncle to appropriate node
            if newNode.parent == newNode.parent.parent.left:
                uncle = newNode.parent.parent.right
                parentIsLeft = True
            else:
                uncle = newNode.parent.parent.left

            # Case 1: Uncle is red -> Reverse colors of uncle, parent and grandparent
            if uncle.color == 0:
                newNode.parent.color = 1
                uncle.color = 1
                newNode.parent.parent.color = 0
                newNode = newNode.parent.parent

            # Case 2: Uncle is black -> check triangular or linear and rotate accordingly
            else:
                # Left-right condition (triangular)
                if parentIsLeft and newNode == newNode.parent.right:
                    newNode = newNode.parent  # Take care as we made the new node the parent
                    self.leftRotate(newNode)
                # Right-Left condition (triangular)
                elif not parentIsLeft and newNode == newNode.parent.left:
                    newNode = newNode.parent
                    self.rightRotate(newNode)
                # Left-left condition (linear)
                if parentIsLeft:
                    newNode.parent.color = 1  # the new parent
                    newNode.parent.parent.color = 0  # the new grandparent will be red
                    self.rightRotate(newNode.parent.parent)
                # Right-right condition (linear)
                else:
                    newNode.parent.color = 1
                    newNode.parent.parent.color = 0
                    self.leftRotate(newNode.parent.parent)

        self.root.color = 1  # Set root to black

    def leftRotate(self, node):
        """
                node              y
                  \     =>      /  \
                    y         node  d
                  /  \           \
                c     d           c
                """
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
        """
        node                    y
       /   \        =>        /   \
      y                     c    node
    /   \                        /
   c     d                      d
        """
        y = node.left
        node.left = y.right  # connect node to d
        if y.right != self.nil:  # connect d to node
            y.right.parent = node
        y.parent = node.parent  # connect y to node's parent

        if node.parent is None:  # connect b parent to a's parent
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.right = node  # connect y to node
        node.parent = y  # connect node to y

    # Function to print used in debugging
    def __printCall(self, node, indent, last):
        if node != self.nil:
            print(indent, end=' ')  # the default end character is new line
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 0 else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    # Function to call print
    def print_tree_id(self):
        self.__printCall(self.root, "", True)

    # Function to print used in debugging
    def __printCall2(self, node, indent, last):
        if node != self.nil:
            print(indent, end=' ')  # the default end character is new line
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 0 else "BLACK"
            print(str(node.arti) + "(" + s_color + ")")
            self.__printCall2(node.left, indent, False)
            self.__printCall2(node.right, indent, True)

    # Function to call print
    def print_tree_en(self):
        self.__printCall2(self.root, "", True)