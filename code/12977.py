from itertools import combinations
import math
def solution(nums):
    answer=0
    nlist = list(combinations(nums, 3))
    for n in nlist:
        for i in range(2, int(math.sqrt(sum(n)))+1):
            if sum(n)%i==0: break
        else: answer+=1
    return answer
