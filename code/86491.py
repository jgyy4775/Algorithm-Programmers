def solution(sizes):
    sizes.sort(reverse=True)
    maxsize= max(sizes[0][0], sorted(sizes,key=lambda x:x[1],reverse=True)[0][1])
    maxsize2=0
    for s in sizes:
        if abs(s[0]-maxsize)>abs(s[1]-maxsize):
            maxsize2=max(maxsize2,s[0])
        else:
            maxsize2=max(maxsize2,s[1])
    return maxsize2*maxsize
  
  
  '''
  def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
  '''
