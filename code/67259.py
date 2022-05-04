from collections import deque
def solution(board):
    q=deque([])
    q.append([0,0,0,0])
    q.append([0,0,1,0])
    cost=[[[int(1e9) for _ in range(len(board))] for _ in range(len(board))] for _ in range(4)]
    dd=[0,1,2,3]
    dx, dy = [0, 1, 0, -1],[1, 0, -1, 0]
    while q:
        i,j,c,val=q.popleft()
        for d in range(4):
            ni, nj = i+dx[d], j+dy[d]
            if 0<=ni<len(board) and 0<=nj<len(board) and board[nj][ni]!=1:
                newv=val+1
                if c!=dd[d]: newv+=5
                if cost[dd[d]][ni][nj]>newv:
                    cost[dd[d]][ni][nj]=newv
                    if ni==len(board)-1 and nj==len(board)-1: continue
                    q.append([ni, nj, d, newv])
    answer=int(1e9)
    for i in range(4):
        answer=min(answer, cost[i][-1][-1])
    return answer*100
