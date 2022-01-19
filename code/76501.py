def solution(absolutes, signs):
    answer=0
    for a, s in zip(absolutes, signs):
        if not s: answer-=a
        else: answer+=a
    return answer
