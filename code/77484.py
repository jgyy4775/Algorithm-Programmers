def solution(lottos, win_nums):
    mingrade = 7 - (len(set(lottos).intersection(set(win_nums))))
    maxgrade = 7 - ((len(set(lottos).intersection(set(win_nums)))) + lottos.count(0))
    if mingrade == 7: mingrade=6
    if maxgrade == 7: maxgrade=6 
    return [maxgrade, mingrade]
