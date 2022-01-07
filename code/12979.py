import math
def solution(n, stations, w):
    answer = 0
    dist=[]
    for s in stations:
        dist.append([max(1,s-w), min(n, s+w)])
    if (dist[0][0]-1)>0: answer += math.ceil((dist[0][0] - 1) / (2 * w + 1))
    for i in range(len(dist)-1):
        if dist[i+1][0]-dist[i][1]>1:
            answer+=math.ceil(((dist[i+1][0]-dist[i][1])-1)/(2*w+1))
    if (n-dist[-1][1])>0: answer+=math.ceil((n-dist[-1][1])/(2*w+1))
    return answer
