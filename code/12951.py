def solution(s):
    answer = ''
    str=s.split(' ')
    for ss in str:
        if ss=='':answer+=' '
        else: answer+=ss[0].upper()+ss[1:].lower()+' '
    return answer[:-1]
