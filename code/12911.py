def solution(n):
    num = format(n, 'b')
    cnt1 = num.count('1')
    answer=n+1
    while True:
        tmp=format(answer, 'b')
        if tmp.count('1')==cnt1: return answer
        answer+=1
