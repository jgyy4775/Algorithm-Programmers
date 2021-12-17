def solution(play_time, adv_time, logs):
    if play_time==adv_time: return "00:00:00"
    play_time = int(play_time.split(':')[0])*3600+int(play_time.split(':')[1])*60+int(play_time.split(':')[2])
    adv_time = int(adv_time.split(':')[0])*3600+int(adv_time.split(':')[1])*60+int(adv_time.split(':')[2])
    total = [0]*(play_time+1)
    for l in logs:
        s,e=l.split('-')
        s=int(s.split(':')[0])*3600+int(s.split(':')[1])*60+int(s.split(':')[2])
        e=int(e.split(':')[0])*3600+int(e.split(':')[1])*60+int(e.split(':')[2])
        total[s]+=1
        total[e]-=1
    for _ in range(2):
        for i in range(1, len(total)):
            total[i] = total[i]+total[i-1]
    maxview, maxtime=0, 0
    for i in range(adv_time-1, play_time):
        if i>= adv_time:
            if maxview<total[i]-total[i-adv_time]:
                maxview=total[i]-total[i-adv_time]
                maxtime=i-adv_time+1
        else:
            if maxview<total[i]:
                maxview=total[i]
                maxtime=i-adv_time+1
    h = maxtime // 3600
    h = '0' + str(h) if h < 10 else str(h)
    maxtime = maxtime % 3600
    m = maxtime // 60
    m = '0' + str(m) if m < 10 else str(m)
    maxtime = maxtime % 60
    s = '0' + str(maxtime) if maxtime < 10 else str(maxtime)
    return h + ':' + m + ':' + s
