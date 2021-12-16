import heapq
def solution(food_times, k):
    if sum(food_times)<=k: return -1 # k시간 후에 더이상 먹을 음식이 없을 때
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) #(시간, 번호)로 heap에 삽입
    vsum=0 # 먹기 위해 사용된 시간
    prev = 0 # 직전에 다먹은 음식 시간
    length=len(food_times) # 남은 음식 수

    # 먹기 위해 사용된 시간 + (현재 음식 시간 - 직전에 다먹은 음식 시간) * 현재 남은 음식 개수와 k 비교
    while vsum+((q[0][0]-prev)*length)<=k:
        now=heapq.heappop(q)[0] # 현재 음식 시간
        vsum+=(now-prev)*length
        length-=1 # 다 먹은 음식 제외
        prev=now # 이전 음식을 현재 음식으로 교체
    q.sort(key=lambda x:x[1]) # 음식 번호 기준으로 정렬
    return q[(k-vsum)%length][1]
