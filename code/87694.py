from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[0] * 101 for i in range(101)]
    cX = 2 * characterX
    cY = 2 * characterY
    iX = 2 * itemX
    iY = 2 * itemY
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 상하좌우이동
    visited = [[0] * 101 for i in range(101)]
    visited[cX][cY] = 1
    queue = deque([(cX, cY)]) # 캐릭터 위치를 큐에 삽입

    for x1, y1, x2, y2 in rectangle: # 테두리와 내부를 1로 설정하기
        for i in range(2 * x1, 2 * x2 + 1):
            for j in range(2 * y1, 2 * y2 + 1):
                board[i][j] = 1

    for x1, y1, x2, y2 in rectangle: # 내부를 0으로 채워주기
        for i in range(2 * x1 + 1, 2 * x2):
            for j in range(2 * y1 + 1, 2 * y2):
                board[i][j] = 0

    while queue:
        x, y = queue.popleft()
        if (x, y) == (iX, iY):
            return (board[x][y] - 1) // 2 # 최종 이동거리에서 1/2만 리턴
        for i, j in d:
            xTemp = x + i
            yTemp = y + j

            # 이동 범위가 배열의 범위를 벗어나지 않고 테두리이며, 방문한 적이 없는 곳이면 그곳으로 이동
            if 0 <= xTemp < 101 and 0 <= yTemp < 101 and board[xTemp][yTemp] != 0 and visited[xTemp][yTemp] == 0:
                board[xTemp][yTemp] = board[x][y] + 1    # (xTemp, yTemp) 까지의 이동거리
                visited[xTemp][yTemp] = 1
                queue.append((xTemp, yTemp))
