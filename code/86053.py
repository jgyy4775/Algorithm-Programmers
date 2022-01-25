def solution(a, b, g, s, w, t):
    start=0
    end=(10 ** 9) * (10 ** 5) * 4
    answer = (10 ** 9) * (10 ** 5) * 4
    while start<=end:
        mid=(start+end)//2  # 주어진 시간
        cur_gold=0    ## 총 운반 가능한 금 무게
        cur_silver=0  ## 총 운반 가능한 은 무게
        total=0
        for i, time in enumerate(t):
            cnt=(mid-time)//(time*2)+1  # 주어진 시간에서 이동할 수 있는 최대 횟수

            # 이동 횟수와 한번에 옮길 수 있는 무게의 곱이 금보다 크면 금을 전부
            # 옮길 수 있는 것이므로 cur_gold에 더해준다.
            if cnt * w[i] > g[i]: cur_gold += g[i]

            # 이동 횟수와 한번에 옮길 수 있는 무게의 곱이 금보다 작다면 금을 전부
            # 옮길 수 없으므로 옮길 수 있는 만큼만 cur_gold에 더해준다.
            if cnt * w[i] <= g[i]: cur_gold += cnt*w[i]

            # 은에 대해서도 금과 동일한 과정을 거치면 된다.
            if cnt * w[i] > s[i]: cur_silver += s[i]
            if cnt * w[i] <= s[i]: cur_silver += cnt * w[i]

            # 운반된 금과 은의 무게가 현재 시간에서 운반가능한 무게보다 작다면
            # 그것들을 전부 옮길 수 있으므로 total에 더해준다.
            if s[i] + g[i] < cnt * w[i]: total += s[i]+g[i]

            # 그렇지 않으면 옮길 수 있는 만큼만 더해준다.
            if s[i] + g[i] >= cnt * w[i]: total += cnt * w[i]

        # 모든 도시에 대해 검사를 마치면 총 운반된 금과 은의 무게가 필요한 무게 이상으로
        # 옮겨졌는지 둘을 합한 무게가 필요한 무게 이상인지 검사하고 너무 많이 옮겨지면 
        # end를 감소시킨다.
        if cur_gold >= a and cur_silver >= b and total >= a+b:
            end=mid-1
            answer=min(answer, mid)
        # 그렇지 않으면 start를 증가시킨다.
        else: start=mid+1
    return answer
