def solution(n,a,b):
    answer = 0
    while n>0:
        answer+=1
        for i in range(1,n+1,2):
            if (i==a and i+1==b) or (i==b and i+1==a): return answer
        a=(a+1)//2
        b=(b+1)//2
        n//=2
