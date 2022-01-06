def solution(n, s):
    if n>s: return [-1]
    reslist = [s//n]*n
    n=s%n
    idx=0
    for i in range(n):
        reslist[idx]+=1
        idx+=1
    reslist.sort()
    return reslist
