# complete

import sys
WHITE = 0
GRAY = 1
BLACK = 2


class Node:
    def __init__(self, data):
        self.data = data
        self.bottom = None
        self.color = WHITE
        self.right = None
        self.parent = None
        self.distance = sys.maxsize


class Graph:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, v1, v2):
        self._add(v1, v2)
        self._add(v2, v1)

    def _add(self, v1, v2):
        if self.head is None:
            n1 = Node(v1)
            self.head = n1
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
                    prev1.bottom = tmp.bottom

                while tmp2.right is not None:
                    prev2 = tmp2
                    # print(prev2.data)
                    tmp2 = tmp2.right
                    if tmp2.data == v:
                        prev2.right = tmp2.right

    def find(self, v):
        tmp = self.head
        while tmp is not None:
            if tmp.data == v:
                return tmp
            tmp = tmp.bottom
        return None

    def bfs(self, v1):
        tmp = self.head
        while tmp is not None:
            tmp.color = WHITE
            tmp.distance = sys.maxsize
            tmp = tmp.bottom
        q = []  # queue for breadth first search
        #   finding the v1 node in toBottom list
        tmp1 = self.find(v1)
        tmp1.color = GRAY
        tmp1.distance = 0
        tmp1.parent = None
        q.append(tmp1)      # enqueue it to the q

        # start BFSearching
        while 0 < len(q):      # looping through the q
            u = q.pop(0)
            tmp = self.find(u.data)
            # tmp =  adjacent nodes of u
            while tmp is not None:      # finding adjacent nodes
                tmp3 = self.find(tmp.data)  # get the appropriate node(tmp3) from the toBottom list
                if tmp3.color == WHITE:     # if tmp3 is white do the changes
                    tmp3.color = GRAY
                    tmp3.distance = u.distance + 1
                    tmp3.parent = u
                    q.append(tmp3)
                tmp = tmp.right
            u.color = BLACK

    def printg(self):
        tmp = self.head
        while tmp is not None:
            # print(tmp.data)
            tmp2 = tmp
            while tmp2 is not None:
                print("(" + str(tmp2.data) + ") d-" + str(tmp2.distance) + " c-" + str(tmp2.color), end=' >> ')
                tmp2 = tmp2.right
            print()
            tmp = tmp.bottom

g = Graph()
g.add(1, 2)
g.add(2, 9)
g.add(2, 7)
g.add(2, 5)
g.add(4, 5)
g.add(4, 6)
g.add(4, 8)
g.add(5, 6)
g.add(5, 8)
g.add(7, 8)
g.add(8, 9)
g.printg()
print("LKJ")
# g.remove(5)
# g.remove(6)
g.bfs(4)
g.printg()
