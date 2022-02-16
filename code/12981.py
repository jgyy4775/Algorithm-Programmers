def solution(n, words):
    worddict = {i:[] for i in range(n)}
    wlist = [words[0]]
    start=words[0][-1]
    worddict[0].append(words[0])
    for i in range(1,len(words)):
        worddict[i%n].append(words[i])
        if words[i] in wlist or start!=words[i][0]: return [i%n+1, len(worddict[i%n])]
        wlist.append(words[i])
        start=words[i][-1]
    return [0,0]
