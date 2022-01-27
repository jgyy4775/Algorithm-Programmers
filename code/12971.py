def solution(sticker):
    dp1,dp2 = [0]*len(sticker),[0]*len(sticker)
    dp1[0]=sticker[0]
    for i in range(1,len(sticker)-1):
        if i==1: dp1[i]=dp1[0]
        else: dp1[i]= max(dp1[i-2]+sticker[i], dp1[i-1])

    for i in range(1,len(sticker)):
        if i==1: dp2[i]=sticker[1]
        else: dp2[i]= max(dp2[i-2]+sticker[i], dp2[i-1])
    return max(max(dp1),max(dp2))
