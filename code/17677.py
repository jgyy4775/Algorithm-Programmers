def solution(str1, str2):
    str1 = [str1[i:i+2] for i in range(len(str1)-1)]
    str2 = [str2[i:i+2] for i in range(len(str2)-1)]
    str1list, str2list = [], []
    for s in str1:
        if s[0].isalpha() and s[1].isalpha(): str1list.append(s.lower())
    for s in str2:
        if s[0].isalpha() and s[1].isalpha(): str2list.append(s.lower())
    len2=len(str2list)
    intercnt = 0
    for s in str1list:
        if s in str2list:
            intercnt+=1
            str2list.remove(s)
    unioncnt = len(str1list)+len2-intercnt
    if unioncnt==0: return 65536
    answer = int((intercnt/unioncnt)*65536)
    return answer
