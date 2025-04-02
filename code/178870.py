def solution(sequence, k):
    answer_s, answer_e = 0, len(sequence)
    tmp_sum,end = 0,0
    for i in range(len(sequence)):
        while tmp_sum<k and end < len(sequence):
            tmp_sum += sequence[end]
            end+=1
        if tmp_sum==k:
            if end-i < answer_e-answer_s :
                answer_s, answer_e = i, end
            
        tmp_sum-=sequence[i]
    return [answer_s, answer_e-1]
