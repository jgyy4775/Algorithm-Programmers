import heapq
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append([e[1], 1])
        graph[e[1]].append([e[0], 1])
    q=[]
    distance=[int(1e9)]*(n+1)
    distance[1]=0
    heapq.heappush(q, [0, 1])
    while q:
        dist, now =  heapq.heappop(q)
        if distance[now]<dist: continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, [cost, i[0]])
    distance=distance[1:]
    maxdist=max(distance)

    return distance.count(maxdist)
