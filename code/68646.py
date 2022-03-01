def solution(a):
    answer = [False]*len(a)
    leftmin, rightmin = float('inf'), float('inf')
    for i in range(len(a)):
        if a[i]<leftmin:
            leftmin=a[i]
            answer[i]=True
        if a[-1-i]<rightmin:
            rightmin=a[-1-i]
            answer[-1-i]=True
    return sum(answer)
