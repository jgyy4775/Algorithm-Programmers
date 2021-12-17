def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[INF]*(n+1) for _ in range(n+1)]

     ## 그래프 초기화
    for f in fares: 
        graph[f[0]][f[1]] = f[2]
        graph[f[1]][f[0]] = f[2]
    for i in range(1, n + 1):  
        for j in range(1, n + 1):
            if i == j: graph[i][j] = 0

    ## i에서 k를 거쳐 j로 가는 비용과 바로 i에서 j로 가는 비용 중에서 최솟값 찾기
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 출발점 s에서 i를 거쳐 도착지점 a와 b까지 가는 최소비용 구하기 
    for i in range(1, n+1):
        answer=min(answer, graph[s][i]+graph[i][a]+graph[i][b])
    return answer
