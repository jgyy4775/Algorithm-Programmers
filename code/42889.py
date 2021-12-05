def solution(N, stages):
    fail = []
    stages.sort()
    for i in range(1,N+1):
        start = -1
        for j in range(len(stages)):
            if stages[j] >= i: start=j;break
        if start != -1:
            tmp=len(stages[start:])
            fail.append(stages.count(i)/tmp)
        else:
            fail.append(0)
    answer = sorted(range(len(fail)), key=lambda k: fail[k], reverse=True)
    answer = [a+1 for a in answer]
    return answer
