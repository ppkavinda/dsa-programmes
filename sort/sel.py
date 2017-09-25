def sel(l):
    for i in range(len(l)):
        m = l[i]
        print(l)
        k = i
        for j in range(i+1, len(l)):
            if m>l[j]:
                m = l[j]
                k = j
        l[i],l[k]=m, l[i]

L = [5, 4, 3, 2, 1, 6, 7, 0, 9, 8]
sel(L)
