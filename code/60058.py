def divide(p):
    lnum, rnum = 0, 0
    for s in range(len(p)):
        if p[s]=='(': lnum+=1
        elif p[s]==')': rnum+=1
        if lnum==rnum:
            return p[:s+1], p[s+1:]
def check(u):
    stack = []
    for i in u:
        if i=='(':
            stack.append(i)
        else:
            if not stack: return False
            stack.pop()
    return True

def solution(p):
    if not p : return "" ## 1
    u, v = divide(p)  ## 2
    if check(u):  ## 3
        return u+solution(v)  ## 3-1
    else:  ## 4
        answer='('  ## 4-1
        answer+=solution(v)  ## 4-2
        answer+=')'  ## 4-3

        for i in u[1:len(u)-1]:   ## 4-4
            if i=='(': answer+=')'
            else: answer+='('
    return answer   ## 4-5
