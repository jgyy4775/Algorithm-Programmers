def solution(dirs):
    sdict = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
    answer = set()
    x,y=0,0
    for d in dirs:
        if -5<=x+sdict[d][0]<=5 and -5<=y+sdict[d][1]<=5:
            answer.add((x, y,x+sdict[d][0], y+sdict[d][1]))
            answer.add((x + sdict[d][0], y + sdict[d][1], x, y))
            x += sdict[d][0]
            y += sdict[d][1]
    return len(answer)//2
