def solution(board, skill):
    answer = 0
    summatrix=[[0]*(len(board[0])+1) for _ in range(len(board[0])+1)]
    for s in skill:
        if s[0]==1:
            summatrix[s[1]][s[2]] -= s[-1]
            summatrix[s[3]+1][s[4]+1] -= s[-1]
            summatrix[s[3]+1][s[2]] += s[-1]
            summatrix[s[1]][s[4]+1] += s[-1]
        if s[0]==2:
            summatrix[s[1]][s[2]] += s[-1]
            summatrix[s[3] + 1][s[4] + 1] += s[-1]
            summatrix[s[3] + 1][s[2]] -= s[-1]
            summatrix[s[1]][s[4] + 1] -= s[-1]
    for i in range(len(summatrix[0])):
        for j in range(1, len(summatrix)):
            summatrix[j][i]+=summatrix[j-1][i]
    for i in range(len(summatrix)):
        for j in range(1, len(summatrix)):
            summatrix[i][j]+=summatrix[i][j-1]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]+summatrix[i][j]>0: answer+=1
    return answer
