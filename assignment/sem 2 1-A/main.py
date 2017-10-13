import re
import math


# # a class for store the 2 points of a line
# class Line:
#     def __init__(self, l):
#         self.st = l[0]     # start point
#         self.en = l[1]     # end point

N = int(input())
S = int(input())
lines = []     # for store all lines(lists) >> [ [[st_x, st_y], [en_x, en_y]], [[st_x, st_y], [en_x, en_y]] ]

for _ in range(N):      # appending lines(lists) to 'points' point(list)
    i = input()
    line = re.findall(r"[+-]?\d+(?:\.\d+)?", i)
    lines.append([[int(line[0]), int(line[1])], [int(line[2]), int(line[3])]])


def lengthToPoint(mainLine, point):     # calculate the perpendicular length to point from mainLine  **NOT USED
    x1 = mainLine[0][0]
    y1 = mainLine[0][1]
    x2 = mainLine[1][0]
    y2 = mainLine[1][1]
    x3 = point[0]
    y3 = point[1]

    up = (y2 - y1) * x3 + (x1 - x2) * y3 + (y1 - y2) * x1 + (x2 - x1) * y1
    down = math.sqrt((y2-y1)**2 + (x1-x2)**2)
    return up / down


def positionOfPoint(mainLine, point):
    x1 = mainLine[0][0]
    y1 = mainLine[0][1]
    x2 = mainLine[1][0]
    y2 = mainLine[1][1]
    x3 = point[0]
    y3 = point[1]
    exp = -(x1 - x2) * y3 + (y1 - y2) * x3 + x1 * y2 - x2 * y1
    if y1-y2 < 0:
        exp = -exp
    print("exp", point, exp)
    return exp

# print(positionOfPoint(lines[S-1], [2, 0]))
# print(positionOfPoint(lines[S-1], [0, 2]))
# print(positionOfPoint(lines[S-1], [-2, 0]))
# print(positionOfPoint(lines[S-1], [0, -2]))


def positionOfLine(mainLine, target):
    p1 = positionOfPoint(mainLine, target[0])
    p2 = positionOfPoint(mainLine, target[1])

    if p1 > 0 and p2 > 0:
        print("front")
        return 0
    elif p1 < 0 and p2 < 0:
        print("back")
        return 1
    else:
        print("on")
        return 2

# positionOfLine(lines[S-1], [[1, 1], [2, 2]])


class Node:
    def __init__(self, data):
        self.data = data
        self.front = None
        self.back = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = Node(lines[S-1])
        self.cont = 0

    def insert(self):
        allInFrontOf = True  # to check if all lines are in front of others
        for j in lines:  # checking...
            if not positionOfLine(lines[S-1], j) > 0:
                allInFrontOf = False
                break  # break if not

        if not allInFrontOf and len(lines) > 1:
            self._insert(lines[S-1], lines, self.root)

    def _insert(self, mainLine, data, current):
        # front, back for hold the front & back lines, tmp for hold the first ele of data(first line)
        front, back, tmp = [], [], data[0]
        print(front, back, tmp)
        while len(data) > 0:        # divide data(lines) onto two lists(back/front)
            j = data.pop()
            print("DONE", j)
            if positionOfLine(mainLine, j) == 0:
                print("0")
                front.append(j)
            elif positionOfLine(mainLine, j) == 1:
                print("1")
                back.append(j)

        fnode = Node(front)
        bnode = Node(back)
        current.front = fnode
        current.back = bnode
        current.data.append(tmp)

        allInFrontOf = True     # to check if all lines are in front of others
        for j in front:         # checking...
            if not positionOfLine(tmp, j) > 0:
                allInFrontOf = False
                break           # break if not

        # if conditions are true continue to front and back
        if not allInFrontOf and len(front) > 1:
            self._insert(tmp, current.front.data, current.front)
        if not allInFrontOf and len(back) > 1:
            self._insert(tmp, current.back.data, current.back)

    def printTree(self):        # traversal FOR TESTING PURPOSE ONLY
        if self.root is not None:
            print(self.root.data)
        if self.root.front is not None:
            self._pre_order(self.root)

    def _pre_order(self, current_node):
        if current_node.front is not None:
            print(current_node.front.data)
            self._pre_order(current_node.front)

        if current_node.back is not None:
            print(current_node.back.data)
            self._pre_order(current_node.back)


t = Tree()
t.insert()
print(t.root.data)
print("T")
t.printTree()


