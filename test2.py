class Node:
    def __init__(self, data):
        self.data = data
        self.bottom = None
        self.right = None


class Graph:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, v1, v2):
        if self.head is None:
            self.head = Node(v1)
            self.head.right = Node(v2)

        else:
            tmp = self.head
            while tmp.bottom is not None:
                if tmp.data == v1:
                    break
                tmp = tmp.bottom

            if tmp.bottom is not None or tmp.data == v1:
                print("SDf")
                # tmp = tmp.bottom
                tmp2 = Node(v2)
                tmp2.right = tmp.right
                tmp.right = tmp2
                # del tmp2
            else:
                tmp.bottom = Node(v1)
                tmp.bottom.right = Node(v2)

    def remove(self, v):
        if self.head.data == v:
            self.head = self.head.bottom
        else:
            tmp = self.head
            p =tmp
            while tmp is not None:
                if tmp.data == v:
                    p
                    print(tmp.data)
                    tmp.bottom = tmp.bottom.bottom
                tmp2 = tmp
                while tmp2 is not None:
                    if tmp2.data == v:
                        tmp2.right = tmp2.right.right
                    tmp2 = tmp2.right
                tmp = tmp.bottom


    def printg(self):
        tmp = self.head
        while tmp is not None:
            # print(tmp.data)
            tmp2 = tmp
            while tmp2 is not None:
                print(tmp2.data, end=', ')
                tmp2 = tmp2.right
            print()
            tmp = tmp.bottom

g = Graph()
g.add(5, 6)
g.add(2, 3)
g.add(4, 5)
g.add(5, 8)
g.add(2, 7)
g.add(2, 4)
g.add(4, 5)
g.add(1, 5)
g.printg()
print("LKJ")
g.remove(2)
g.printg()
# print(g.head.data, g.head.right.data, g.head.right.right)
# print(g.head.bottom.data, g.head.right.data, g.head.bottom.right.right)
# print(g.head.bottom.bottom.data, g.head.right.data, g.head.bottom.bottom.right.right)
# print(g.head.bottom.bottom.bottom.data, g.head.right.data, g.head.bottom.bottom.bottom.right.right)