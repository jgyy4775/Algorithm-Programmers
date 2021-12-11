def solution(m, musicinfos):
    answer = ["", ""]
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    mdict = {}
    for info in musicinfos:
        start, end, title, music = info.split(',')
        music = music.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        start = [int(s) for s in start.split(':')]
        end = [int(e) for e in end.split(':')]
        duration = (end[0]-start[0])*60 + (end[1]-start[1]+1)
        music = music*(duration//len(music)) + music[:duration%len(music)]
        mdict[title] = music
    for k in mdict:
        if m in mdict[k]:
            if len(answer[1]) < len(mdict[k]):
                answer[0] = k
                answer[1] = mdict[k]
    return "(None)" if len(answer[0]) ==0 else answer[0]
