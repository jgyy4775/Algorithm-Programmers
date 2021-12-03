from collections import deque
def solution(places):
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for place in places:
        people = []
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i,j))
        for p in people:
            q = deque()
            q.append(p)
            visited = [[0] * 5 for i in range(5)]
            distance = [[0] * 5 for i in range(5)]
            visited[p[0]][p[1]] = 1
            while q:
                i, j = q.popleft()
                for d in range(4):
                    x = i + dx[d]
                    y = j + dy[d]
                    if 0<=x<5 and 0<=y<5 and visited[x][y] != 1:
                        if place[x][y] =='O':
                            q.append((x,y))
                            visited[x][y] =1
                            distance[x][y] = distance[i][j]+1
                        if place[x][y] == 'P' and distance[i][j] <= 1:
                            flag = 0
                            break
        answer.append(flag)
    return answer
