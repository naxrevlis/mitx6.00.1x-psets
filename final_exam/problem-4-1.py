L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 4
newL = []
while len(L) > n:
    i = 0
    subL = []
    while i < n:
        subL.append(L[i])
        i += 1


    L.pop(0)
    newL.append(subL)
