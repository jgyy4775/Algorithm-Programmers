def solution(n, t, m, timetable):
    answer = 0
    # 시간은 모두 분으로 변경
    timetable = [int(t.split(':')[0])*60+int(t.split(':')[1]) for t in timetable]
    timetable.sort()
    bus = [9*60+t*i for i in range(n)]
    i=0
    for b in bus:
        cnt=0 # 버스에 타있는 크루수

        # 버스가 다 차지 않고, 버스 도착 시간보다 크루가 먼저 왔다면
        while cnt<m and i <len(timetable) and timetable[i]<=b:
            i+=1  # 다음 크루로 이동
            cnt+=1 # 버스 탑승 인원 1증가
        if cnt<m: answer=b # 버스에 자리 남았다면 가장 마지막 버스 시간에 맞춰오면 됨
        else: answer=time[i-1]-1 # 버스에 남는 자리가 없다면 가장 마지막에 온 크루보다 1분 먼저 오면 됨
    return str(answer//60).zfill(2)+':'+str(answer%60).zfill(2)
