def solution(record):
    answer = []
    udict = {}
    for r in record:
        tmp=r.split(' ')
        if tmp[0] == 'Enter':
            udict[tmp[1]] = tmp[2]
        if tmp[0] == 'Change':
            udict[tmp[1]] = tmp[2]
    for r in record:
        tmp=r.split(' ')
        if tmp[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(udict[tmp[1]]))
        elif tmp[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(udict[tmp[1]]))
    return answer
