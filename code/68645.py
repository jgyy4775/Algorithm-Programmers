def solution(n):
    answer = [[0 for _ in range(1, i+1)] for i in range(1,n+1)]
    x,y=-1,0
    now=1
    for i in range(n):
        for _ in range(i,n):
            if i%3==0: x+=1 #하
            elif i%3==1: y+=1 # 우
            else: # 상
                x-=1
                y-=1
            answer[x][y]=now
            now+=1
    return sum(answer,[])
