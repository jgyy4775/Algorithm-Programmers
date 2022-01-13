def solution(A, B):
    A.sort()
    B.sort()
    answer, aidx, bidx = 0, 0, 0
    while aidx<len(A) and bidx<len(B):
        if A[aidx]>=B[bidx]: bidx+=1
        else:
            answer+=1
            aidx+=1
            bidx+=1
    return answer
