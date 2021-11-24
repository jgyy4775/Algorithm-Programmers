def solution(new_id):
    
    new_id = new_id.lower()
    res = ''
    for s in new_id:
        if s.isalpha() or s.isdigit() or s == '-' or s == '_' or s == '.':
            res +=s
    new_id=res 
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')
    if len(new_id)==0:
        new_id = 'a'
    if len(new_id)>=16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    if len(new_id) <=2:
        new_id = new_id+new_id[-1]*(3-len(new_id))
    
    return new_id
