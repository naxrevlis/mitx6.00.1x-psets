L = [10, 4, 6, 8, 3, 3, 4, 5, 7, 7, 2, 9]
L = [1, 1, 1, 1, 1]
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]

def longestRun(L):
    longestRunList = []
    if len(L) == 1:
        return 1
    elif len(L) == 0:
        return 0
    else:
        for i in range(0,len(L)):
            longestRunListTemp = []
            k = i
            longestRunListTemp.append(L[k])
            for k in range(k, len(L)-1):
                if L[k+1] >= L[k]:
                    longestRunListTemp.append(L[k+1])
                    print longestRunListTemp
                else:
                    break
            if len(longestRunListTemp) > len(longestRunList):
                longestRunList = longestRunListTemp
        return len(longestRunList)


print longestRun(L)
