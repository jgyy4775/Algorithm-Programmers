def solution(genres, plays):
    answer = []
    gdict = {}
    for g,p in zip(genres,plays):
        if g not in gdict: gdict[g]=0
        gdict[g]+=p
    gdict=sorted(gdict.items(), key=lambda x:x[1], reverse=True)
    gdict=[g[0] for g in gdict]
    for g in gdict:
        tmp=[]
        for i, (gen,pl) in enumerate(zip(genres, plays)):
            if g==gen: tmp.append((pl, i))
        tmp.sort(key=lambda x:x[0], reverse=True)
        tmp=tmp[:2] if len(tmp)>2 else tmp;print(tmp)
        answer+=[t[1] for t in tmp]
    return answer
