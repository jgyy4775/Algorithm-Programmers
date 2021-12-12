def checktr(t, timelist):
    c=0
    start=t
    end=t+1000
    for tt in timelist:
        if tt[1]>=start and tt[0]<end: c+=1
    return c
def solution(lines):
    answer = 0
    timelist = []
    for line in lines:
        data, stime, time = line.split(' ')
        h, m, s = stime.split(':')
        time = float(time.replace('s',''))*1000
        end = (int(h)*3600 + int(m)*60 + float(s))*1000
        start = end-time+1
        timelist.append([start, end])
    for t in timelist:
        answer = max(answer, checktr(t[0], timelist), checktr(t[1], timelist))
    return answer
