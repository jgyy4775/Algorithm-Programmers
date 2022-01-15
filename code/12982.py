def solution(d, budget):
    answer, total = 0,0
    d.sort()
    for dd in d:
        if total+dd<=budget:
            total+=dd
            answer+=1
    return answer
