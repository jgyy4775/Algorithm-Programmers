import re
def solution(dartResult):
    square = {'S':1, 'D':2, 'T':3}
    score = re.findall('\d+', dartResult)
    bonus = re.findall('\D+', dartResult)
    reslist = [0]
    for i in range(len(score)):
        if '*' in bonus[i]:
            reslist[-1] *=2
            reslist.append(2 * pow(int(score[i]), square[bonus[i][0]]))
        elif '#' in bonus[i]:
            reslist.append(-1*pow(int(score[i]), square[bonus[i][0]]))
        else:
            reslist.append(pow(int(score[i]), square[bonus[i][0]]))
    return sum(reslist)
