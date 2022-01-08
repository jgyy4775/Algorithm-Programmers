import heapq
def solution(operations):
    heap = []
    for operation in operations:
        id, n = operation.split(' ')
        if id == 'I':
            heapq.heappush(heap, int(n))
        if id=='D' and heap:
            if n=='1':
                heap.sort()
                heap.pop()
            else:
                heapq.heappop(heap)
    if not heap: return [0,0]
    else: return [max(heap), min(heap)]
