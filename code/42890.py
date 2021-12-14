from itertools import combinations
def solution(relation):
    relen = len(relation[0])
    key_idx = [i for i in range(relen)]
    candidate=[]
    for i in range(1,relen+1):
        combi = list(combinations(key_idx,i))
        for c in combi:
            hist = []
            for r in relation:
                currkey = [r[j] for j in c]
                if currkey in hist: break # 하나라도 중복되는 경우는 식별 불가능
                else: hist.append(currkey)
            else: # 하나도 중복 안 된 경우에는 식별 가능, 현재까지 구해진 후보키와 비교
                for can in candidate:
                    if set(can).issubset(set(c)): break  #최소성 확인 
                else: candidate.append(c)
    return len(candidate)
