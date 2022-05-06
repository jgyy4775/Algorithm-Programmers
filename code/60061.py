def solution(n, build_frame):
    answer = []
    for x,y,aa,b in build_frame:
        if b==1: ## 설치
            answer.append([x,y,aa])
            for a in answer:
                if a[2]==0: ## 기둥인 경우
                    # 바닥위에 있고,
                    # 보의 한쪽 끝 부분에 있고
                    # 다른 기둥 위에 있는지 위 3조건을 검사
                    if a[1]==0 or [a[0]-1, a[1], 1] in answer or [a[0],a[1],1] in answer or [a[0],a[1]-1,0] in answer:
                        continue
                    else: # 조건중 하나라도 만족하지 않으면 설치될 수 없으므로 제거
                        answer.remove([x,y,aa])
                        break
                elif a[2]==1:  ## 보인 경우
                    # 한쪽 끝 부분이 기둥위에 있거나
                    # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는지 2조건을 검사
                    if [a[0],a[1]-1,0] in answer or [a[0]+1,a[1]-1,0] in answer or ([a[0]-1,a[1],1] in answer and [a[0]+1, a[1], 1] in answer):
                        continue
                    else: # 조건중 하나라도 만족하지 않으면 설치될 수 없으므로 제거
                        answer.remove([x,y,aa])
                        break
        else:  ## 삭제
            answer.remove([x,y,aa])
            for a in answer:
                if a[2]==0:
                    if a[1]==0 or [a[0]-1, a[1], 1] in answer or [a[0],a[1],1] in answer or [a[0],a[1]-1,0] in answer:
                        continue
                    else:
                        answer.append([x,y,aa])
                        break
                elif a[2]==1:
                    if [a[0],a[1]-1,0] in answer or [a[0]+1,a[1]-1,0] in answer or ([a[0]-1,a[1],1] in answer and [a[0]+1, a[1], 1] in answer):
                        continue
                    else:
                        answer.append([x,y,aa])
                        break

    return sorted(answer)
