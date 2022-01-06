def find_parent(parent, x):
    if parent[x]!=x: parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b: parent[b]=a
    else: parent[a]=b

def solution(n, costs):
    parent=[0]*n
    result=0
    edges=[]
    for i in range(n):
        parent[i]=i
    for c in costs:
        edges.append((c[2],c[0],c[1]))
        edges.append((c[2], c[1], c[0]))
    edges.sort()
    for e in edges:
        c,a,b=e
        if find_parent(parent,a)!=find_parent(parent,b):
            union_parent(parent,a,b)
            result+=c
    return result
