def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0: return len(cities)*5
    cache = []
    for c in cities:
        c=c.lower()
        if c not in cache:
            answer+=5
            if len(cache)<cacheSize: cache.append(c)
            else:
                del cache[0]
                cache.append(c)
        else:
            answer+=1
            del cache[cache.index(c)]; cache.append(c)
    return answer
​
