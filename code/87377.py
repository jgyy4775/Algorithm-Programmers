def solution(line):
    joinlist=[]
    xmax, ymax=-float('inf'), -float('inf')
    xmin, ymin=float('inf'), float('inf')
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            mo=(line[i][0]*line[j][1]-line[i][1]*line[j][0])
            if mo==0:continue
            x=(line[i][1]*line[j][2]-line[i][2]*line[j][1])/mo
            y=(line[i][2]*line[j][0]-line[i][0]*line[j][2])/mo
            if x.is_integer() and y.is_integer():
                joinlist.append([int(x),int(y)])
                xmax,ymax=max(xmax,int(x)),max(ymax, int(y))
                xmin,ymin=min(xmin,int(x)),min(ymin, int(y))
    star = [['.']*(xmax-xmin+1) for _ in range(ymax-ymin+1)]
    for j in joinlist:
        x,y=j[0],j[1]
        star[ymax-y][x-xmin]='*'
    return [''.join(s) for s in star]
