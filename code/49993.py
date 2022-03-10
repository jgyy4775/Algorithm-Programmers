def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        tmp=list(skill)
        for s in st:
            if s in tmp:
                if s!=tmp[0]: break
                else: tmp=tmp[1:]
        else: answer+=1
    return answer
