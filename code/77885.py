def solution(numbers):
    answer = []
    for n in numbers:
        n=int(n)
        n=bin(n)[2:]
        if n[-1]=='0':answer.append(int(n[:-1]+'1',2))
        else:
            if n.count('0')==0:
                answer.append(int('10' + n[1:], 2))
            else:
                idx=n.rfind('0')
                n = n[:idx]+'10'+n[idx+2:]
                answer.append(int(n, 2))
    return answer
