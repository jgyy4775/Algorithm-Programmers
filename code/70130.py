from collections import Counter
def solution(a):
    if len(a)<=1: return 0 # 원소가 1개 이하면 return 0
    answer=0
    cntlist = Counter(a).most_common() # a의 원소들의 개수를 세어주고 내림차순 정렬
    cntlist = {n:cnt for n,cnt in cntlist} # 딕셔너리 변수로 변경
    print(cntlist)
    for n in cntlist: # n을 교집합으로 갖는 스타수열을 만든다.
        # 현재 원소로 만들수 있는 최대 스타수열 길이는 원소 길이의 *2이므로
        # 이 값이 현재까지 가장 긴 스타수열보다 작으면 계산 하지 않습니다.
        if cntlist[n]*2<=answer: continue

        idx=1
        cnt=0
        while idx<len(a):
            # a[idx-1] !=n and a[idx]!=n이면 둘 다 n 값이 없는 것이고
            # a[idx-1]==a[idx] 이면 스타수열의 조건에 위배
            if (a[idx-1] !=n and a[idx]!=n) or a[idx-1]==a[idx]:
                idx+=1
                continue
            cnt+=2
            idx+=2
        answer=max(answer,cnt)
    return answer
