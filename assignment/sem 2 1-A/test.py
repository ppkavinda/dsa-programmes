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


print(positionOfLine([[1, 1], [5, 5]], [[-5, 6], [-1, 1]]))
print(positionOfLine([[1, 1], [5, 5]], [[-2, -3], [4, -3]]))
print(positionOfLine([[1, 1], [5, 5]], [[1, 1], [-5, 5]]))
