from collections import deque
def solution(begin, target, words):
    q=deque()
    q.append([begin,0])
    while q:
        w,a=q.popleft()
        if w==target:return a
        for word in words:
            cnt=0
            if len(w)==len(word):
                for w1,w2 in zip(list(w), list(word)):
                    if w1==w2:cnt+=1
            if cnt+1==len(w):
                q.append([word,a+1])
                del words[words.index(word)]
    return 0
