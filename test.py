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

    def remove(self, data):
        tmp = self.root
        ptmp = tmp
        # find the target node
        while tmp.data != data and tmp is not None:
            ptmp = tmp
            if tmp.data > data:
                tmp = tmp.left
            else:
                tmp = tmp.right
        # tmp is now the  target node & ptmp is the parent of that

        # delete case 1 [no children]
        if tmp.right is None and tmp.left is None:
            if ptmp.left.data == tmp.data:
                ptmp.left = None
            else:
                ptmp.right = None
        # delete case 2 [one child]
        elif tmp.right is None and tmp.left is not None:
            if ptmp.data > tmp.data:
                ptmp.left = tmp.left
            else:
                ptmp.right = tmp.left
        elif tmp.left is None and tmp.right is not None:
            if ptmp.data > tmp.data:
                ptmp.left = tmp.right
            else:
                ptmp.right = tmp.right
        # case 3 [two children]
        else:
            rmc = tmp.left      # rmc = right most child
            prmc = rmc          # prmc = parent of rmc
            while rmc.right is not None:        # finding rmc
                prmc = rmc
                rmc = rmc.right

            # if root is deleted
            if data == self.root.data:
                rmc.right = self.root.right
                rmc.left = self.root.left
                self.root = rmc
                prmc.right = None

            # if target is a left child
            elif ptmp.data > rmc.data:
                # if rmc has no children
                if tmp.left.data == rmc.data:
                    ptmp.left = rmc
                    rmc.right = tmp.right
                    # print(ptmp.right.data)
                else:
                    ptmp.left = rmc
                    rmc.left = tmp.left
                    rmc.right = tmp.right
                    prmc.right = None
            # if target is a right child
            else:
                # if rmc has no children
                if tmp.left.data == rmc.data:
                    ptmp.right = rmc
                    rmc.right = tmp.right
                else:
                    ptmp.right = rmc
                    rmc.left = tmp.left
                    rmc.right = tmp.right
                    prmc.right = None

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root is None:
            print("Tree is empty!")
        else:
            print(root.data, end=' ')
            if root.left is not None:
                self._inorder(root.left)
            if root.right is not None:
                self._inorder(root.right)

t = Tree()
t.insert(25)

t.insert(10)
t.insert(50)

t.insert(5)
t.insert(15)
t.insert(40)
t.insert(60)

t.insert(30)
t.insert(45)
t.insert(55)
t.insert(70)

t.insert(35)
t.insert(26)
t.insert(4)

t.inorder()
print()
t.remove(50)
t.remove(30)
t.remove(5)
t.remove(15)
t.remove(26)
t.remove(45)
t.inorder()
