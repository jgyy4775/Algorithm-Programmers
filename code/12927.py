import heapq
def solution(n, works):
    if sum(works)<=n: return 0
    works=[[-w,w] for w in works]
    heapq.heapify(works)
    while n>0:
        a,b=heapq.heappop(works)[1],works[0][1]
        tmp=a-b
        if tmp==0:
            heapq.heappush(works, [-(a-1),a-1])
            n-=1
        else:
            tmpn=n
            n-=tmp
            if n<0: heapq.heappush(works, [-(a-tmpn),a-tmpn])
            else: heapq.heappush(works, [-(a - tmp), a - tmp])
    answer = 0
    for w in works:
        answer+=(w[1]*w[1])
    return answer
