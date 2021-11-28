def solution(a, b):
    answer = sum([a[i]*b[i] for i in range(len(a))])
    return answer
