from itertools import permutations
def solution(user_id, banned_id):
    answer = []
    combi = list(permutations(user_id, len(banned_id)))
    banned_id = [b.replace('*','.') for b in banned_id]
    for c in combi:
        c=list(c)
        ban = False
        for i in range(len(banned_id)):
            if len(banned_id[i])==len(c[i]) and re.findall(banned_id[i],c[i]): pass
            else: ban =True
        if not ban: answer.append(c)
    tmp = []
    answer = [sorted(a) for a in answer]
    for a in answer:
        if a not in tmp: tmp.append(a)
    return len(tmp)
