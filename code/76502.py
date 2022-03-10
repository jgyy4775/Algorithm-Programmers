def solution(s):
    answer = 0
    for _ in range(len(s)-1):
        ss,m,b=[-1],[-1],[-1]
        for j in s:
            if j =='(': 
                if -1 in ss: ss.remove(-1)
                ss.append(0)
            elif j=='{':
                if -1 in m: m.remove(-1)
                m.append(0)
            elif j=='[':
                if -1 in b: b.remove(-1)
                b.append(0)
            elif j==')' and 0 in ss: ss.remove(0)
            elif j=='}' and 0 in m: m.remove(0)
            elif j==']' and 0 in b: b.remove(0)
        if not ss and not m and not b: answer+=1
        s=s[1:]+s[0]
    return answer
