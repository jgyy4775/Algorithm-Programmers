import math
def solution(n, k):
    nlist = [i for i in range(1,n+1)]
    answer=[]
    while n:
        pern = math.factorial(n)//n # 어떤수하나가 맨앞에오는 가지수
        idx=k//pern
        k%=pern
        if k==0: answer.append(nlist.pop(idx-1))
        else: answer.append(nlist.pop(idx))
        n-=1
    return answer
