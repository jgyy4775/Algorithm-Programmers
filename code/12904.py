def solution(s):
    maxnum=0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            tmp=s[i:j]
            if tmp==tmp[::-1]: maxnum=max(maxnum, len(tmp))
    return maxnum
