def solution(numbers):
    numbers=list(map(str, numbers))
    originidx={i:numbers[i] for i in range(len(numbers))}
    numbers=[(numbers[i]*4)[:4] for i in range(len(numbers))]
    newid = {i:numbers[i] for i in range(len(numbers))}
    newid=sorted(newid.items(), reverse=True, key=lambda x:x[1])
    answer=''
    for i in newid:
        answer+=originidx[i[0]]
    return str(int(answer))
