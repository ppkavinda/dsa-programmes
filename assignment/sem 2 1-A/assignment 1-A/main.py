import re
import math
import time
start_time = time.clock()


N = int(input())
S = int(input())
lines = []     # for store all lines(lists) >> [ [[st_x, st_y], [en_x, en_y]], [[st_x, st_y], [en_x, en_y]] ]

for _ in range(N):      # appending lines(lists) to 'points' point(list)
    i = input()
    line = re.findall(r'[+-]?\d+(?:\.\d+)?', i)
    lines.append([[int(line[0]), int(line[1])], [int(line[2]), int(line[3])]])


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
    # print("exp", mainLine, point, exp)
    return exp


def positionOfLine(mainLine, target):
    p1 = positionOfPoint(mainLine, target[0])
    p2 = positionOfPoint(mainLine, target[1])

    if p1 == 0 and p2 == 0:
        # print("on")
        return 3
    elif p1 >= 0 and p2 >= 0:
        # print("front")
        return 0
    elif p1 <= 0 and p2 <= 0:
        # print("back")
        return 1
    else:
        # print("intersect")
        return 2


def lineIntersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        # print(line1, line2)
        raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [x, y]


class Node:
    def __init__(self, data):
        self.data = data
        self.front = None
        self.back = None
        self.inFrontOfAll = False


class Tree:
    def __init__(self):
        self.root = Node(lines[S-1])
        self.cont = 0

    def insert(self):
        allInFrontOf = False  # to check if all lines are in front of others
        # for j in lines:  # checking...
        #     if positionOfLine(lines[S-1], j) == 0:
        #         allInFrontOf = False
        #         break  # break if not

        if not allInFrontOf and len(lines) > 1:
            self._insert(lines[S-1], lines, self.root)

    def _insert(self, mainLine, data, current):
        # front, back for hold the front & back lines, tmp for hold the first ele of data(first line)
        front, back, tmp = [], [], [mainLine]
        print("tst", current.data, self.root.data, mainLine)
        if current is not self.root:
            tmp = [data[0]]
            mainLine = tmp[0]

        while len(data) > 0:        # divide data(lines) onto two lists(back/front)
            j = data.pop(0)          # j is a line [[x1, y1], [x2, y2]]
            if j != mainLine:
                posLine = positionOfLine(mainLine, j)       # posLine = position of line
                if posLine == 0:        # j is in front of mainLine
                    front.append(j)
                elif posLine == 1:      # j is in back of mainLine
                    back.append(j)
                elif posLine == 2:      # j is intersecting mainLine
                    intPoint = lineIntersection(mainLine, j)        # intPoint = intersecting point
                    if positionOfLine(mainLine, [j[0], intPoint]) == 0:     # dividing line to two segments
                        front.append([j[0], intPoint])
                        back.append([intPoint, j[1]])
                    else:
                        front.append([intPoint, j[1]])
                        back.append([j[0], intPoint])
                elif posLine == 3:      # j is on the mainLine
                    tmp.append(j)       # append it to the root of current level

        fnode = Node(front)
        bnode = Node(back)
        current.front = fnode
        current.back = bnode
        current.data = tmp

        allInFrontOf = True     # to check if all lines are in front of others
        for j in front:         # checking...
            if positionOfLine(j, mainLine) != 0:
                allInFrontOf = False
                break           # break if not

        if allInFrontOf and len(current.front.data) > 0:
            current.front.inFrontOfAll = True

        # if conditions are true continue to front and back
        if not allInFrontOf and len(front) > 1:
            self._insert(tmp[0], current.front.data, current.front)
        if not allInFrontOf and len(back) > 1:
            self._insert(tmp[0], current.back.data, current.back)

    def printTree(self):        # inOrder traversal
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, current):
        if current.back is not None:
            self._printTree(current.back)
        print(current.inFrontOfAll, current.data)
        if current.front is not None:
            self._printTree(current.front)

    def getFrontMost(self):     # get the front-most node
        tmp = self.root         # the line which is in front of all
        prev = tmp
        while True:
            if tmp.front is not None:
                if len(tmp.front.data) > 0:
                    prev = tmp
                    tmp = tmp.front
                else:
                    if tmp.inFrontOfAll:
                        return [prev.data, tmp.data]
                    else:
                        return tmp.data

            else:
                if tmp.inFrontOfAll:
                    return [prev.data, tmp.data]
                else:
                    return tmp.data

    def getFaceToFace(self):
        if self.root is not None:
            self._getFaceToFace(self.root, self.root)

    def _getFaceToFace(self, prev, current):
        if current.front is not None:
            self._getFaceToFace(current, current.front)

        if current.inFrontOfAll:
            print([prev.data, current.data])

        if current.back is not None:
            self._getFaceToFace(current, current.back)


t = Tree()
t.insert()
t.printTree()
print("front most", t.getFrontMost())
print("face2face: ")
t.getFaceToFace()
# print(time.clock() - start_time)
