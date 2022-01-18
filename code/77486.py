def solution(enroll, referral, seller, amount):
    resdict = {e:0 for e in enroll}
    parentdict={}
    for e, r in zip(enroll, referral):
        if r!='-': parentdict[e]=r
    for s, a in zip(seller, amount):
        a*=100
        while True:
            if s not in parentdict:
                resdict[s] += a-int(a * 0.1)
                break
            resdict[s]+=a-int(a*0.1)
            s=parentdict[s]
            a=int(a*0.1)
            if a <1: break
    return list(resdict.values())
