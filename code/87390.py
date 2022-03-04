def solution(n, left, right):
    nlist = [i for i in range(n+1)]
    answer=[]
    left,right=int(left),int(right) # 테스트케이스 12,13 런타임 에러로 추가
    for i in range(left//n,n):
        answer+=[nlist[i+1]]*i+nlist[i+1:]
        if len(answer)>=(right-left+2*n): break

    return answer[left%n:left%n+right-left+1]
