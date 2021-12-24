def bfs(computers,visit,a,n):
    q=deque()
    q.append(a)
    while q:
        i = q.popleft()
        visit[i]=True
        for j in range(n):
            if computers[i][j]==1 and not visit[j]:
                q.append(j)
    return computers
def solution(n, computers):
    answer=0
    visit=[False]*n
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            computers =bfs(computers,visit,i,n)
            answer+=1
    return answer
