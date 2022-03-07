from collections import deque
def bfs(matrix, visit, i, n):
    q=deque()
    q.append(i)
    cnt=1
    while q:
        a=q.popleft()
        visit[a]=True
        for j in range(1,n+1):
            if matrix[a][j]==1 and not visit[j]:
                q.append(j)
                cnt+=1
    return cnt

def solution(n, wires):
    matrix=[[0]*(n+1) for _ in range(n+1)]
    answer=int(1e9)
    for wire in wires:
        matrix[wire[0]][wire[1]]=1
        matrix[wire[1]][wire[0]]=1
    for wire in wires:
        matrix[wire[0]][wire[1]] = 0
        matrix[wire[1]][wire[0]] = 0
        visit = [False] * (n + 1)
        visit[1]=True
        cnt=bfs(matrix, visit, 1, n)
        answer=min(answer, abs(cnt-(n-cnt)))
        matrix[wire[0]][wire[1]]=1
        matrix[wire[1]][wire[0]]=1
    return answer
