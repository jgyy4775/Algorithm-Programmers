def solution(x):
    answer=sum([int(i) for i in str(x)])
    return True if x%answer==0 else False
