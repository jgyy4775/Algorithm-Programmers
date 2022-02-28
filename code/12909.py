def solution(s):
    stack = []
    for ss in s:
        if ss=='(': stack.append(ss)
        else: 
            if not stack: return False
            stack.pop()
    if stack: return False
    else: return True
