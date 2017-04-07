class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        newnode = Tree(data)

        if self.left is None:
            self.left = newnode
        elif self.right is None:
            self.right = newnode
        else:
            self.left.insert(data)

    # def insertRight(self, data):
    #     newnode = Tree(data)
    #
    #     if self.left is None:
    #         self.left = newnode
    #     elif self.right is None:
    #         self.right = newnode
    #     else:
    #         self.right.insertRight(data)

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

t = Tree("a")
t.insert("b")
t.insert("c")
t.insert("d")
t.insert("e")
t.insert("f")
print("\npre")
t.preorder()
print("\nin")
t.inorder()
print("\npost")
t.postorder()
