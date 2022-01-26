from itertools import permutations
def solution(k, dungeons):
    combi=list(permutations(dungeons,len(dungeons)))
    answer=0
    for c in combi:
        tmp,tmpanswer=k,0
        for d in c:
            if d[0]<=tmp and tmp-d[1]>=0:
                tmpanswer+=1
                tmp-=d[1]
            else: break
        answer=max(answer,tmpanswer)
    return answer
