def solution(brown, yellow):
    for i in range(3, brown+yellow+1):
        if (brown+yellow)%i==0:
            w, h = max(i, (brown+yellow+1)//i), min(i, (brown+yellow+1)//i)
            if (w-2)*(h-2)==yellow: return [w,h]
