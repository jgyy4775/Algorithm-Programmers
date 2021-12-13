def solution(m, n, board):
    answer = 0
    for i in range(m):  ## 입력을 리스트로 변경
        board[i] = list(board[i])
    while True:   ## 더이상 지워지는 블록이 없을 때까지 반복
        remove = [[0]*n for _ in range(m)]  ## 지워졌는지 여부를 저장하는 배열 선언(지워지면 1)

        # 모든 배열을 검사하며 2*2짜리 같은 블록을 찾음(i,j를 기준으로 오른쪽, 아래, 대각선 검사)
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]!=0 and board[i][j]==board[i][j+1] and board[i][j]==board[i+1][j] and board[i][j]==board[i+1][j+1]:
                    # i,j와 오른쪽, 아래, 대각선이 모두 같으면 remove각 칸을 1로 변경
                    remove[i][j],remove[i][j+1],remove[i+1][j],remove[i+1][j+1]=1,1,1,1
        cnt=0
        for i in range(m):
            cnt+=sum(remove[i]) # 현재 board에서 몇개나 지워졌는지 count
        answer+=cnt
        if cnt==0: break # 지워지는 칸이 하나도 없으면 탐색을 종료

        # 지워진 칸들을 위에 있는 블록들로 채움
        for i in range(m-1,-1,-1):  # 가장 밑에 행부터 검사 시작
            for j in range(n):
                if remove[i][j]==1: # (i,j)가 지워진 행이라면
                    x=i-1  # 바로 윗행 검사
                    while x>=0 and remove[x][j]==1: # 지워지지 않은 블록이 나올때까지 위로 올라감
                        x-=1
                    if x<0: board[i][j]=0 (i,j)  # 위에 더이상 블록이 없다면 board[x][j]를 0으로 바꿈
                    else:                        # 그렇지 않으면 있는 블록으로 교체
                        board[i][j]=board[x][j]
                        remove[x][j]=1

    return answer
