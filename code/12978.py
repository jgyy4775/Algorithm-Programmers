import heapq
def solution(N, road, K):
    graph=[[] for _ in range(N+1)]
    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))
    distance=[int(1e9)]*(N+1)
    q=[]
    heapq.heappush(q,(0, 1))
    distance[1]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist: continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost, i[0]))
    answer=0
    for d in distance:
        if d<=K: answer+=1
    return answer
