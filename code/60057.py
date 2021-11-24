def solution(s):
    if len(s)==1: return 1
    minlen = 1001
    for i in range(1,(len(s)//2)+1):
        answer = ''
        dlist = [s[j:j+i] for j in range(0, len(s), i)]
        cnt=0
        for d in range(len(dlist)-1):
            if dlist[d]==dlist[d+1]: cnt+=1
            else:
                if cnt+1!=1: answer += str(cnt+1)+dlist[d]
                else: answer += dlist[d]
                cnt=0
        if dlist[-1] == dlist[-2]: answer += str(cnt + 1) + dlist[-1]
        else: answer += dlist[-1]
        minlen=min(minlen, len(answer))
    return minlen
