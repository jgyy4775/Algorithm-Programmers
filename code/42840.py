def solution(answers):
    score = [0, 0, 0]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == p1[i%5]:
            score[0] += 1
        if answers[i] == p2[i%8]:
            score[1] += 1
        if answers[i] == p3[i%10]:
            score[2] += 1

    maxscore = max(score)
    result = []
    if score[0]==maxscore:
        result.append(1)
    if score[1]==maxscore:
        result.append(2)
    if score[2]==maxscore:
        result.append(3)
    return result
