import re
def solution(files):
    sortfiles = sorted(files, key = lambda x: (re.findall('\D+',x.lower())[0], int(re.findall('\d+',x)[0])))
    return sortfiles
