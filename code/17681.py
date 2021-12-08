def solution(n, arr1, arr2):
    answer = []
    arr1 = [format(a, 'b').zfill(5) for a in arr1]
    arr2 = [format(a, 'b').zfill(5) for a in arr2]
    for i in range(n):
        tmp = ''
        for j in range(n):
            if arr1[i][j]=='1' or arr2[i][j]=='1':
                tmp+='#'
            else: tmp+=' '
        answer.append(tmp)
    return answer
