def ins(l):
    for i in range(1, len(l)):
        j = i
        print()
        while j>0 and l[j-1] > l[j]:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1
            print(l)
                

L = [5, 4, 3, 2, 1, 0, 9, 8, 7]
ins(L)
