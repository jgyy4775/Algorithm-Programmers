from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []    
    for c in course:
        combi = []
        for order in orders:
            order = sorted(order) 
            combi.extend(list(combinations(order, c)))
        count = Counter(combi)
        if count:
            if max(count.values()) >= 2:
                for k, v in count.items():
                    if v == max(count.values()):
                        answer.append("".join(k))
    return sorted(answer)
