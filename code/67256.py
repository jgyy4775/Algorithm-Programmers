def solution(numbers, hand):
    answer = ''
    posdict = {'1':(0,0), '2':(0,1), '3':(0,2), '4':(1,0), '5':(1,1),
               '6':(1,2), '7':(2,0), '8':(2,1), '9':(2,2), '0':(3,1), '*':(3,0), '#':(3,2)}
    lfinger, rfinger = '*','#'
    for n in numbers:
        n=str(n)
        if n in ['1','4','7'] :
            answer += 'L'
            lfinger = n
        elif n in ['3','6','9'] :
            answer += 'R'
            rfinger = n
        else:
            rdis = abs(posdict[n][0]-posdict[rfinger][0])+abs(posdict[n][1]-posdict[rfinger][1])
            ldis = abs(posdict[n][0] - posdict[lfinger][0]) + abs(posdict[n][1] - posdict[lfinger][1])
            if rdis>ldis: answer+='L'; lfinger=n
            elif rdis<ldis: answer+='R'; rfinger=n
            elif rdis==ldis:
                if hand == 'right': answer+='R'; rfinger=n
                else: answer+='L';lfinger=n

    return answer
