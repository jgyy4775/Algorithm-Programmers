def solution(board):
    answer=0
    if len(board) == 1 and len(board[0]) == 1:
        if board[0][0] == 0: return 0
        elif board[0][0] == 1: return 1
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] and board[i][j-1] and board[i-1][j] and board[i-1][j-1]:
                board[i][j]=min(board[i][j-1], board[i-1][j], board[i-1][j-1])+1
            answer=max(answer, board[i][j])
    return answer**2
