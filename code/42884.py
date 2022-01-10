def solution(routes):
    answer = 0
    routes.sort()
    end = routes[0][1]
    idx=1
    while idx<len(routes):
        if routes[idx][0] > end:
            answer+=1
            end = routes[idx][1]
        else:
            end = min(end,routes[idx][1] )
        idx+=1
    return answer+1
