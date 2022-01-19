def solution(numbers):
    answer = 0
    for n in range(10):
        if n not in numbers: answer+=n
    return answer
