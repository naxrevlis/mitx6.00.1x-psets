def isSeven(N):
    if N == 7: return 1
    else return 0
def count7(N):
    if N == 0:
        return 0
    return isSeven(N % 10) + count7(N/10)
