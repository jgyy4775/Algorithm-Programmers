def solution(arr):
    global answer
    answer = [0, 0]
    search(arr, [0,0], len(arr))
    return answer

def search(arr, ij, n):
    i, j, ans = ij[0], ij[1], arr[ij[0]][ij[1]]
    for x in range(n):
        for y in range(n):
            if ans!=arr[i+x][j+y]:
                search(arr, [i, j], n//2)
                search(arr, [i, j+n//2], n//2)
                search(arr, [i+n//2, j], n//2)
                search(arr, [i+n//2, j+n//2], n//2)
                return
    answer[ans]+=1
