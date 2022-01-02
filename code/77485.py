def solution(rows, columns, queries):
    answer=[]
    matrix=[[0]*(columns) for _ in range(rows)]
    a=1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j]=a
            a+=1
    for q in queries:
        q=[x-1 for x in q]
        tmp=matrix[q[0]][q[1]]
        minnum=tmp
        # left
        for i in range(q[0]+1, q[2]+1):
            matrix[i-1][q[1]]=matrix[i][q[1]]
            minnum=min(minnum,matrix[i][q[1]])
        # bottom
        for i in range(q[1]+1, q[3]+1):
            matrix[q[2]][i-1]=matrix[q[2]][i]
            minnum=min(minnum,matrix[q[2]][i])
        # right
        for i in range(q[2]-1, q[0]-1, -1):
            matrix[i+1][q[3]]=matrix[i][q[3]]
            minnum=min(minnum,matrix[i][q[3]])
        # top
        for i in range(q[3]-1, q[1]-1,-1):
            matrix[q[0]][i+1]=matrix[q[0]][i]
            minnum=min(minnum,matrix[q[0]][i])
        matrix[q[0]][q[1]+1]=tmp
        answer.append(minnum)
    return answer
