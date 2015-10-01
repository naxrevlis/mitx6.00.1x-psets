def isUnique(value, aDict):
    n = 0
    for key in aDict:
        if aDict[key] == value:
            n += 1
    if n > 1: return False
    else: return True

def uniqueValues(aDict):
    uniqueList = []
    for key in aDict:
        if isUnique(aDict[key],aDict):
            uniqueList.append(key)
    return uniqueList
