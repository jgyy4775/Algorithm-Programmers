def solution(tickets):
    answer = []
    airportdict = {}
    for t in tickets:
        if t[0] not in airportdict:
            airportdict[t[0]]=[]
        airportdict[t[0]].append(t[1])
        airportdict[t[0]].sort()
    stack = ['ICN']
    while stack:
        s = stack[-1]
        if s not in airportdict or len(airportdict[s])==0:
            answer.append(stack.pop())
        else:
            stack.append(airportdict[s].pop(0))
    return answer[::-1]
