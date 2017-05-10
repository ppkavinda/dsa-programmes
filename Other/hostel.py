def rooms():
    times = int(input())
    i = 0
    ans = 0
    while i < times:
        inp = input().split()
        if (int(inp[1]) - int(inp[0])) >= 2:
            ans += 1
        i += 1
    print(ans)

rooms()
