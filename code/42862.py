def solution(n, lost, reserve):
    reserve.sort();lost.sort()
    inter = set(lost)&set(reserve)
    lost = list(set(lost)-inter);reserve=list(set(reserve)-inter)
    lostcnt = len(lost)
    for l in lost:
        for r in range(len(reserve)):
            if abs(l-reserve[r])==1:
                lostcnt-=1
                del reserve[r]
                break
    answer = n-lostcnt
    return answer
