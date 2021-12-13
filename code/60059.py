def rotation(key):
    rkey = []
    for i in range(len(key[0])):
        tmp=[]
        for j in range(len(key)):
            tmp.append(key[j][i])
        tmp.reverse()
        rkey.append(tmp)
    return rkey

def check(x, y, key, lock, size, start, end):
    explist = [[0]*size for _ in range(size)]

    for i in range(len(key)):
        for j in range(len(key)):
            explist[x+i][y+j]+=key[i][j]
    for i in range(start, end):
        for j in range(start, end):
            explist[i][j] += lock[i-start][j-start]
            if explist[i][j]!=1:
                return False
    return True

def solution(key, lock):
    start = len(key)-1
    end=start+len(lock)
    size = len(lock)+start*2
    for _ in range(4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, size, start, end): return True
        key=rotation(key)
    return False
