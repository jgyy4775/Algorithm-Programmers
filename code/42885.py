def solution(people, limit):
    answer,i,j = 0,0,len(people)-1
    people.sort()
    while i<=j:
        answer += 1
        if people[i]+people[j]<=limit: i+=1
        j-=1
    return answer
