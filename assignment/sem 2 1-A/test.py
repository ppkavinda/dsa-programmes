list1 = []
n = int(input())
s = int(input())
for i in range(n):
    line = input()
    line = (line.replace(",", " ").replace("(", " ").replace(")", " ").strip().split())
    list1.append([int(line[0]), int(line[1]), int(line[2]), int(line[3])])

master = list1[s - 1]


def front_or_back(rootline, line):
    x1 = int(rootline[0])
    y1 = int(rootline[1])
    x2 = int(rootline[2])
    y2 = int(rootline[3])
    x3 = int(line[0])
    y3 = int(line[1])
    x4 = int(line[2])
    y4 = int(line[3])
    value1 = y3 * (x2 - x1) - x3 * (y2 - y1) + x1 * (y2 - y1) - y1 * (x2 - x1)
    value2 = y4 * (x2 - x1) - x4 * (y2 - y1) + x1 * (y2 - y1) - y1 * (x2 - x1)

    if (value1 > 0 and value2 >= 0 or value1 >= 0 and value2 > 0):
        return 0
    elif (value1 == 0 and value2 == 0):
        return 1
    elif (value1 < 0 and value2 <= 0 or value1 <= 0 and value2 < 0):
        return 2
    elif (value1 > 0 and value2 < 0 or value1 < 0 and value2 > 0):
        return 3


def point(rootline, line):
    x1 = int(rootline[0])
    y1 = int(rootline[1])
    x2 = int(rootline[2])
    y2 = int(rootline[3])
    x3 = int(line[0])
    y3 = int(line[1])
    x4 = int(line[2])
    y4 = int(line[3])
    y = ((y1 - y2) * (x3 * (y4 - y3) - y3 * (x4 - x3)) - ((y3 - y4) * (x1 * (y2 - y1) - y1 * (x2 - x1)))) / (
    ((x2 - x1) * (y3 - y4)) - ((y1 - y2) * (x4 - x3)))  # find the y coordinate of cross point
    x = ((x4 - x3) * (x1 * (y2 - y1) - y1 * (x2 - x1)) - ((x2 - x1) * (x3 * (y4 - y3) - y3 * (x4 - x3)))) / (
    ((x2 - x1) * (y3 - y4)) - ((y1 - y2) * (x4 - x3)))  # find the x coordinate of cross point
    y0 = round(y, 2)
    x0 = round(x, 2)
    return (x0, y0)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BST:
    def __init__(self, master):
        self.root = Node(list1)
        self.master = master

    def insert(self, node):
        self.insertnode(self.root, list1)

    def insertnode(self, node, lines):
        root = self.master
        print(node.data)
        listf = []
        listb = []

        if node is not self.root:
            root = lines[0]

        for j in lines:
            x3 = int(j[0])
            y3 = int(j[1])
            x4 = int(j[2])
            y4 = int(j[3])
            if (j != root):
                x = front_or_back(root, j)
                if (x == 0):
                    listf.append(j)
                elif (x == 2):
                    listb.append(j)
                elif (x == 3):
                    p = point(root, j)
                    z = front_or_back(root, [p[0], p[1], x3, y3])
                    if (z == 0):
                        listf.append([p[0], p[1], x3, y3])
                        listb.append([p[0], p[1], x4, y4])
                    elif (z == 2):
                        listf.append([p[0], p[1], x4, y4])
                        listb.append([p[0], p[1], x3, y3])

        a1, a2 = listf, listb
        # print("\nfront lines :", len(a1))
        # print("\nback lines :", len(a2))

        # if (len(a1)==1):
        # print("\n\n%s line is in front of all other lines :"%a1)

        newnode1 = Node(listf)
        newnode2 = Node(listb)
        node.right = newnode1  # not self.root (new node should set as the right child of CURRENT node
        node.left = newnode2  # same here

        m = True
        for k in listf:  # When the front of lines in front face each other
            if root != k:
                p = front_or_back(k, root)
                if p != 0:
                    m = False
                    break

        if not m and len(listf) > 1:  # not >0    #When the line does not have anything in front
            self.insertnode(node.right, listf)
        if not m and len(listb) > 1:  # not >0
            self.insertnode(node.left, listb)

    def inordertraversal(self):
        if self.root.left != None:
            self._inordertraversal(self.root)

    def _inordertraversal(self, currentnode):
        if currentnode.left != None:
            self._inordertraversal(currentnode.left)
        print(currentnode.data)
        if currentnode.right != None:
            self._inordertraversal(currentnode.right)


t = BST(master)
t.insert(t.root)
t.inordertraversal()

