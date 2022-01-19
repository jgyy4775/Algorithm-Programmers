def solution(id_list, report, k):
    report=list(set(report))
    cnt = {id:0 for id in id_list}
    idreport={id:[] for id in id_list}
    banlist = []
    for r in report:
        a, b = r.split(' ')
        cnt[b]+=1
        idreport[a].append(b)
        if cnt[b]>=k: banlist.append(b)
    answer=[]
    for i in idreport:
        answer.append(len(set(idreport[i])&set(banlist)))
    return answer
​
