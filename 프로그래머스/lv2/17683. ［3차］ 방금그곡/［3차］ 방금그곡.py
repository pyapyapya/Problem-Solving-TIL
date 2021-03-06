from collections import deque

table = {
    'C#': 'H',
    'D#': 'I',
    'F#': 'J',
    'G#': 'K',
    'A#': 'L'
}

def parse(title):
    stack = [title[0]]
    table_key = set(table.keys())
    for i in range(1, len(title)):
        if stack[-1] + title[i] in table_key:
            temp = table[stack.pop() + title[i]]
            stack.append(temp)
        else:
            stack.append(title[i])
    return ''.join(stack)
    
def convert_hhmm_to_minutes(time):
    time = time.split(':')
    hour = int(time[0])
    minutes = int(time[1])
    
    per_minutes = hour * 60 + minutes
    return per_minutes
    
def search_music_title(query_melody, play_melody, play_time):
    query_melody = list(query_melody)
    len_query_melody = len(query_melody)
    deq = deque([], maxlen=len_query_melody)
    play_melody = play_melody * 1440
    for minute in range(play_time+1):
        deq.append(play_melody[minute])
        if query_melody == list(deq):
            return 1
    return 0

def solution(m, musicinfos):
    max_time = 0
    answer = ''
    m = parse(m)
    
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        start_time = musicinfo[0]
        end_time = musicinfo[1]
        music_title = musicinfo[2]
        melody = musicinfo[3]
        
        melody = parse(melody)
        start_time = convert_hhmm_to_minutes(start_time)
        end_time = convert_hhmm_to_minutes(end_time)
        play_time = end_time - start_time
        
        result = search_music_title(m, melody, play_time)
        if result == 1:
            if max_time < play_time:
                max_time = play_time
                answer = music_title
            elif max_time == play_time:
                continue
    if max_time == 0:
        answer = '(None)'
    return answer
