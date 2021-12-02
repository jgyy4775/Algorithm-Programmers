from itertools import combinations as combi
from collections import defaultdict

def solution(infos, querys):
    answer = []
    infodict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            for c in combi(info_key, i):
                tmp_key = ''.join(c)
                infodict[tmp_key].append(info_val)
    for k in infodict.keys():
        infodict[k].sort()
    for q in querys:
        q = q.split(' ')
        q_score = int(q[-1])
        q = q[:-1]
        for i in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        tmp_q = ''.join(q)

        if tmp_q in infodict:
            scores =  infodict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end)//2
                    if scores[mid]>=q_score: end=mid
                    else: start = mid+1
                answer.append(len(scores)-start)
        else: answer.append(0)
    return answer
