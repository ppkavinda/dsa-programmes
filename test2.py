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
            while tmp.bottom is not None:
                prev1 = tmp
                tmp2 = prev1
                tmp = tmp.bottom
                if tmp.data == v:

                    # print(tmp.data)
                    prev1.bottom = tmp.bottom
                while tmp2.right is not None:
                    prev2 = tmp2
                    # print(prev2.data)
                    tmp2 = tmp2.right
                    if tmp2.data == v:
                        prev2.right = tmp2.right

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
g.add(1, 6)
g.add(2, 3)
g.add(3, 5)
g.add(4, 5)
g.add(5, 8)
g.add(4, 7)
g.add(4, 7)
g.add(4, 5)
g.add(1, 5)
g.add(5, 2)
g.printg()
print("LKJ")
g.remove(5)
g.remove(6)
g.printg()
