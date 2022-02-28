def solution(s):
    for ss in s:
        if not ss.isdigit(): return False
    if len(s)==4 or len(s)==6: return True
    else: return False
