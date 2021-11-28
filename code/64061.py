def solution(orders, course):
    bucket = []
    cnt = 0
    for c in course:
        for i in range(len(orders)):
            if orders[i][c-1] != 0:
                bucket.append(orders[i][c-1])
                orders[i][c - 1] = 0
                break
    while True:
        flag = False
        print(bucket)
        for i in range(1, len(bucket)):
            if bucket[i] == bucket[i-1]:
                flag = True
                cnt += 1
                break
        bucket = bucket[0:i-1] + bucket[i+1:]
        if flag == False:
            break
    return cnt*2
