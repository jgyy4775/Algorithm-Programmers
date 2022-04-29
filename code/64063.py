import sys
sys.setrecursionlimit(100000)
def find(room, rdict):
    # 현재 방에 아무도 배정되어 있지 않은 경우
    if room not in rdict:
        rdict[room]=room+1 # 현재 방 번호 기준 다음으로 빈방 좌표 저장
        return room # 방 번호 반환
    # 아무도 배정 받지 않은 방이 나올 때까지 재귀 함수 시행
    empty=find(rdict[room], rdict)
    rdict[room]=empty+1
    return empty

def solution(k, room_number):
    answer = []
    rdict={} # 해당 방 번호를 기준으로 그 번호보다 값이 크면서 빈방이면 좌표를 저장

    for room in room_number:
        n=find(room, rdict)
        answer.append(n)
    return answer
