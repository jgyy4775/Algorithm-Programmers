def solution(msg):
    answer = []
    alphadict = {'A':1, 'B':2, 'C':3, 'D':4,'E':5, 'F':6, 'G':7, 'H':8, 'I':9,'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16,'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23,'X':24, 'Y':25, 'Z':26}
    start = 27
    while True:
        w =''
        for m in msg:
            w+=m
            if w not in alphadict:
                w=w[:-1]
                break
        answer.append(alphadict[w])
        msg=msg[len(w):]
        if not msg: break
        w+=msg[0]
        alphadict[w]=start;start+=1
    return answer
