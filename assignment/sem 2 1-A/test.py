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


# print(positionOfLine([[1, 1], [5, 5]], [[-5, 6], [-1, 1]]))
# print(positionOfLine([[1, 1], [5, 5]], [[-2, -3], [4, -3]]))
# print(positionOfLine([[1, 1], [5, 5]], [[1, 1], [-5, 5]]))


def intersectPoint(target):
    pass


def lineIntersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [x, y]

print(lineIntersection([[1, 11], [6, 8]], [[-6, 1], [-3, 4]]))
print(positionOfPoint([[1, 0], [1, 1]], [2, 0]))