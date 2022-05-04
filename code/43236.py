def solution(distance, rocks, n):
    answer = 0
    rocks.sort()  ## 정렬
    start, end = 0, distance-rocks[0]
    while start<=end:
        mid=(start+end)//2  # 정답이라고 가정한 값
        del_s=0  # 제거된 돌의 개수
        st_s=0   # 시작 지점(기준이 되는 돌)
        for r in rocks:
            if r-st_s<mid: del_s+=1 # 돌 사이의 거리가 가정한 값보다 작으면 그 돌을 제거한다.
            else: st_s=r  # 그렇지 않으면 그 돌을 새로운 시작 지점으로 설정한다. 
            if del_s>n: break # 제거된 돌의 수가 n보다 크면 탐색을 종료한다.
        if del_s>n: end=mid-1 # 제거된 돌이 너무 많으면 가정한 값이 큰 것이므로 end를 줄여준다.
        else: # 그렇지 않으면 start를 늘려준다.
            answer=mid
            start=mid+1
    return answer
