from itertools import permutations
def solution(n, weak, dist):
    answer=len(dist)+1
    length=len(weak)
    
    # 길이를 두배로 늘려 원형을 일자 형태로 변형
    for i in range(length):
        weak.append(weak[i]+n)
        
    # 0부터 length-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            cnt=1  # 투입할 친구의 수
            
            # 현재 차례인 친구가 점검할 수 있는 마지막 위치
            position=weak[start]+friends[cnt-1]
            
            # 시작점부터 모든 취약 지점을 확인
            for i in range(start, start+length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[i]:
                    cnt+=1 # 새 친구 투입
                    if cnt>len(dist): break # 모든 사람이 투입되면 종료
                    
                    # 그 지점부터 새로운 사람으로 다시 시작
                    position = weak[i]+friends[cnt-1]
            answer=min(answer,cnt)
    if answer>len(dist): return -1
    return answer
