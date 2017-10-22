import math


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



7
1
1 1 4 4
7 2 9 6
-2 -2 -5 -7
-4 5 -1 8
-6 1 -3 4
-3 9 1 5
1 11 6 8



3
2
-4 7 -2 3
-2 7 2 5
1 2 4 5