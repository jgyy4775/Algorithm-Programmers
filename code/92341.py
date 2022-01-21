import math
def solution(fees, records):
    answer = {}
    cardict = {}
    for r in records:
        time, num, info = r.split(' ')
        if num not in cardict:
            cardict[num]=[-1,-1,-1,0] # 세번째는 입출차 여부(1이면 입차상태,0이면 출차)
        if info=='IN':
            cardict[num][0]=int(time.split(':')[0])*60+int(time.split(':')[1])
            cardict[num][2]=1
        elif info=='OUT':
            cardict[num][1]=int(time.split(':')[0])*60+int(time.split(':')[1])
            cardict[num][2]=0
            cardict[num][3]+=cardict[num][1]-cardict[num][0]
    for car in cardict:
        if cardict[car][2]==1:
            cardict[car][1]=23*60+59
            cardict[car][3] += cardict[car][1] - cardict[car][0]
        if cardict[car][3]<=fees[0]: answer[car]=fees[1]
        else:
            fee=fees[1]+(math.ceil((cardict[car][3]-fees[0])/fees[2]))*fees[3]
            answer[car]=fee
    answer=sorted(answer.items(), key=lambda x:x[0])
    answer=[int(a[1]) for a in answer]
    return answer
