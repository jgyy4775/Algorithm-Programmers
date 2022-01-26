from itertools import product
def solution(word):
    alpha=['A','E','I','O','U']
    allist=[]
    for i in range(1,6):
        allist+=list(product(alpha, repeat=i))
    allist.sort()
    return allist.index(tuple(word))+1
