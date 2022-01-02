from itertools import permutations
def solution(numbers):
    answer = []
    numbers=sorted(list(numbers), reverse=True)
    for i in range(1, len(numbers)+1):
        tmplist = list(permutations(numbers, i))
        for t in tmplist:
            t=''.join(t)
            if int(t)==1 or int(t)==0: continue
            for j in range(2,int(t)):
                if int(t)%j==0:break
            else: answer.append(int(t))
    answer=set(answer)
    return len(answer)
