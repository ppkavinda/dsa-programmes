def buble(li):
    for i in range(1, len(li)+1):
        print()
        for j in range(1, len(li)+1-i):
            if li[j-1] > li[j]:
                tmp = li[j-1]
                li[j-1] = li[j]
                li[j] = tmp
            print(li)
            

            
L = [5, 4, 3, 2, 1, 6, 7, 9, 8, 0]
buble(L)
