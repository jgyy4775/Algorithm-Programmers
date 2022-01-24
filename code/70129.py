def solution(s):
    zcnt,cnt=0,0
    while True:
        if s=='1':break
        tmpcnt=s.count('0')
        s=str(bin(len(s)-tmpcnt))[2:]
        cnt+=1
        zcnt+=tmpcnt
    return [cnt, zcnt]
