from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = [[i,priorities[i]] for i in range(len(priorities))]
    q=deque(priorities)
    while True:
        p = q.popleft()
        for n in q:
            if n[1]>p[1]: q.append(p);break
        else:
            answer+=1
            if p[0]==location: break
    return answer
