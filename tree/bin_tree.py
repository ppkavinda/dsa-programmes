# binary tree implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Bin_tree:
    def __init__(self, data_in):
        self.root = Node(data_in)

    # helper function for insert left method
    def ins_l(self, parent, target, data_in):
        new_node = Node(data_in)

        if parent.data == target:
            if parent.left is None:
                parent.left = new_node
                print("D")
            else:
                print("Error: Node already has a left child")
        else:
            if parent.left is not None:
                self.ins_l(parent.left, target, data_in)
            if parent.right is not None:
                self.ins_l(parent.right, target, data_in)
            print("E")

    def insert_left(self, target, data_in):
        new_node = Node(data_in)

        if self.root.data == target:
            self.root.left = new_node
            print("F")
        else:
            self.ins_l(self.root.left, target, data_in)
            print("G")

    # helper function for insert_right method
    def ins_r(self, parent, target, data_in):
        new_node = Node(data_in)

        if parent.data == target:
            if parent.right is None:
                parent.right = new_node
            else:
                print("Error: Node already has a right child")
        else:
            if parent.right is not None:
                self.ins_r(parent.right, target, data_in)
            if parent.left is not None:
                self.ins_r(parent.left, target, data_in)

    def insert_right(self, target, data_in):
        new_node = Node(data_in)
        if self.root.data == target:
            self.root.right = new_node
        else:
            self.ins_r(self.root.right, target, data_in)

    def pre_help(self, parent):
        if parent is not None:
            print(parent.data, " ", end='')
        if parent.left is not None:
            self.pre_help(parent.left)
        if parent.right is not None:
            self.pre_help(parent.right)

    def printT(self):
        self.pre_help(self.root)

tree = Bin_tree(1)
tree.insert_right(1, 2)
print("-")
tree.insert_left(1, 3)
print("-")
tree.insert_right(3, 4)
print("-")
tree.insert_right(4, 5)
tree.printT()
