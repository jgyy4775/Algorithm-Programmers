def convert(num, n):
    tmp = '0123456789ABCDEF'
    q,r = divmod(num, n)
    if q==0: return tmp[r]
    else: return convert(q, n)+tmp[r]

def solution(n, t, m, p):
    answer=''
    allstring = '0'
    for i in range(1,t*m):
        tmp=convert(i, n)
        allstring+=tmp
    for i in range(len(allstring)):
        if i%m==p-1: answer+=allstring[i]
        if len(answer)==t: return answer
