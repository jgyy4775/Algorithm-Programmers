from collections import deque
def solution(maps):
    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]
    q=deque()
    q.append([0,0])
    while q:
        x,y=q.popleft()
        for i,j in zip(dx, dy):
            xx=x+i
            yy=y+j
            if 0<=xx<len(maps) and 0<=yy<len(maps[0]) and maps[xx][yy]==1:
                maps[xx][yy]=maps[x][y]+1
                q.append([xx,yy])
    if maps[-1][-1]>1: return maps[-1][-1]
    else: return -1
