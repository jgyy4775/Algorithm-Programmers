from itertools import combinations_with_replacement
from collections import Counter
def solution(n, info):
    maxdiff,max_comb=0,{}
    for combi in combinations_with_replacement(range(11), n):
        cnt=Counter(combi)
        score1, score2=0,0 # 라이언 점수, 어피치 점수
        for i in range(1, 11):
            if info[10-i]<cnt[i]: score1+=i #점수i를 라이언이 더 많이 맞췄다면 라이언이 점수 획득
            elif info[10-i]>0: score2+=i # 그외의 경우에는 어피치가 점수 획득
        diff=score1-score2# 라이언과 어피치의 점수 차
        if diff>maxdiff:# 현재까지 가장 큰 점수차를 낸 경우라면
            max_comb=cnt # 각 점수에 맞힌 횟수를 max_comb에 저장
            maxdiff=diff # 두 점수의 차이 값을 maxdiff에 저장
    if maxdiff>0:
        answer=[0]*11
        for n in max_comb:
            answer[10-n]=max_comb[n]
        return answer
    else: return [-1]
    
    
#깊이 우선 탐색을 이용한 풀이
'''
from copy import deepcopy
max_diff, max_board = 0, []
def solution(n, info):
    def dfs(ascore, lscore, cnt, idx, board):
        # 어피치점수, 라이언점수, 현재까지 쏜 화살의 수, 현재 살펴볼 점수, 라이언의 점수 보드

        global max_diff, max_board
        if cnt > n: return # 모든 화살을 다 쏜 경우
        if idx > 10: # 마지막 점수까지 모두 살펴본 후
            diff = lscore - ascore # 라이언과 어피치의 점수차
            if diff > max_diff: # 최대 점수차 보다 더 크다면
                board[10] = n - cnt
                max_board = board  # 각 점수에 맞힌 횟수를 max_comb에 저장
                max_diff = diff  # 두 점수의 차이 값을 maxdiff에 저장
            return
        if cnt < n: # 아직 쏠 수 있는 활이 남은 경우
            board2 = deepcopy(board);
            board2[10 - idx] = info[10 - idx] + 1 # 해당 점수를 어피치보다 한발 더 맞춘 경우
            dfs(ascore, lscore + idx, cnt + info[10 - idx] + 1, idx + 1, board2)
        board1 = deepcopy(board)
        if info[10 - idx] > 0: # 해당 점수를 어피치가 맞춘 경우
            # 라이언이 그 점수를 맞추지 않아 어피치가 점수를 얻은 경우
            dfs(ascore + idx, lscore, cnt, idx + 1, board1)
        else:
            # 라이언과 어피치 모두 그 점수를 얻지 못하는 경우
            dfs(ascore, lscore, cnt, idx + 1, board1)
    dfs(0, 0, 0, 0, [0] * 11)
    return max_board if max_board else [-1]
'''
