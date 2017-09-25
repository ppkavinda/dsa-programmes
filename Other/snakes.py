inp1 = int(input())
for lands in range(inp1):
    num_levels = int(input())
    det_levels = input()
    levels = det_levels.split()

    for i in range(len(levels)):
        levels[i] = int(levels[i])

    ans = True

    if levels[0] != 1:
        ans = False

    if len(levels) % 2 == 0:
        ans = False

    center = levels[len(levels)//2]

    i = 0
    if ans is True:
        while i < len(levels):
            if i < levels.index(center):
                if levels[i] + 1 == levels[i+1]:
                    ans = True
                else:
                    ans = False
                    break
            if i > levels.index(center):
                if levels[i-1] == (levels[i] + 1):
                    ans = True
                else:
                    ans = False
                    break
            i += 1

    if ans is True:
        if len(levels[:levels.index(center)]) == len(levels[levels.index(center):]) - 1:
            ans = True
        else:
            ans = False

    if ans is True:
        print("yes")
    else:
        print("no")
