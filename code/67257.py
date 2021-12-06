import re
def calculate(numbers, op, p):
    while p:
        tmp = p.pop(0)
        while tmp in op:
            idx = op.index(tmp)
            op.pop(idx)
            l, r = numbers.pop(idx), numbers.pop(idx)
            if tmp=='+': result = l+r
            if tmp=='-': result = l-r
            if tmp=='*': result = l*r
            numbers.insert(idx, result)
    return numbers[0]

def solution(expression):
    answer = 0
    numbers = re.findall('\d+',expression);print(numbers)
    numbers = [int(n) for n in numbers]
    op = re.findall('\D+', expression);print(op)
    oppermu = [["+", "-", "*"], ["+", "*", "-"], ["-", "+", "*"], ["-", "*", "+"], ["*", "-", "+"], ["*", "+", "-"]]
    for p in oppermu:
        answer = max(abs(calculate(numbers[:], op[:], p)), answer)
    return answer
