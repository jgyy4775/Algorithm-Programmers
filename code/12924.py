def solution(n):
    answer = 0
    start=1
    while start<=n:
        tmp=0
        for i in range(start, n+1):
            tmp+=i
            if tmp==n: 
                answer+=1
                break
            elif tmp>n: break
        start+=1
    return answer
