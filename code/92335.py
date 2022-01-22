def solution(n, k):
    answer = 0
    tmp=''
    while n>0:
        n, mod=divmod(n,k)
        tmp+=str(mod)
    tmp=tmp[::-1]
    for t in tmp.split('0'):
        if t=='1' or t=='': continue
        t=int(t)
        for i in range(2, int(t**0.5) + 1):
            if t % i == 0: break
        else: answer+=1
    return answer
