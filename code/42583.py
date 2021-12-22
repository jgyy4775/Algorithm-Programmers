from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    q=deque(truck_weights)
    while q:
        answer+=1
        tmpd = []
        total=0
        for b in bridge:
            if b[1] + 1 <= bridge_length:
                tmpd.append([b[0], b[1] + 1])
                total+=b[0]
        bridge = tmpd
        if len(bridge)<bridge_length :
            tmp = q[0]
            if total+tmp<=weight:
                bridge.append([tmp,1])
                q.popleft()
    return answer+(bridge_length-bridge[-1][1])+1
