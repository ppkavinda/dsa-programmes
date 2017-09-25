class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
        self.count += 1

    def _insert(self, data, current):
        if data<current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(data, current.left)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(data, current.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root is None:
            print("Tree is empty!")
        else:
            print(root.data)
            if root.left is not None:
                self._inorder(root.left)
            if root.right is not None:
                self._inorder(root.right)

t = Tree()
t.insert(5)
t.insert(6)
t.insert(4)
t.inorder()