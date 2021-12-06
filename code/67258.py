def solution(gems):
    gemdict = {gems[0]:1} # start와 end사이의 보석의 종류를 갯수별로 저장하는 딕셔너리 변수
    allgems = len(set(gems)) # 총 보석의 종류 수
    gemlist = [0, len(gems)-1] # 답이 될 수 있는 start와 end의 구간(정답 후보)
    start, end = 0, 0
    while (start < len(gems) and end<len(gems)): # start, end가 보석의 길이를 넘지 않을 동안 반복
        if len(gemdict)==allgems: # 모든 보석을 다 살 수 있을 때
            if end-start < gemlist[1]-gemlist[0]: 현재의 구간의 길이가 더 적으면
                gemlist=[start, end] # 정답 후보를 현재 구간으로 교체 
            if gemdict[gems[start]]==1: #start를 옮기기전 현재 start의 보석 종류가 1개면 dict에서 아예 삭제
                del gemdict[gems[start]]
            else:
                gemdict[gems[start]]-=1 # 그렇지 않으면 1개 감소
            start+=1 # start를 한칸 옮겨 새로운 출발점에서 검사 시작
        else: # 아직 모든 보석을 다 사지 못했을 때
            end+=1  # 끝점을 하나 증가
            if end==len(gems): break
            if gems[end] in gemdict.keys(): # 현재 보석이 이미 샀던 보석이면 
                gemdict[gems[end]]+=1  # 보석 수 1 증가
            else:  # 그렇지 않으면 dict에 추가
                gemdict[gems[end]]=1
    return [gemlist[0]+1, gemlist[1]+1]
