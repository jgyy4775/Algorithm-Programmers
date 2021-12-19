def solution(clothes):
    cdict = {}
    for c in clothes:
        if c[1] not in cdict: cdict[c[1]]=0
        cdict[c[1]]+=1
    cnt=1
    for i in cdict.values():
        cnt*=(i+1)
    return cnt-1
