import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    if scoville[0] >= K: return 0
    while True:
        if len(scoville)<=1:
            return -1
        newfood = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, newfood)
        if newfood >= K and scoville[0] >= K:
            return cnt+1
            break
        else:
            cnt += 1
