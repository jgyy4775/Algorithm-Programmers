def solution(s):
    answer = []
    s=s[2:-2].split('},{')

    s.sort(key=len)
    for t in s:
        t = t.split(',')
        for i in t:
            if int(i) not in answer:
                answer.append(int(i))
    return answer
