def to_seconds(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])

def to_datetime(sec):
    print(sec)
    return f"{str(sec // 60).zfill(2)}:{str(sec % 60).zfill(2)}"

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)

    if op_start <= pos <= op_end:
        pos = op_end

    for command in commands:
        if command == "prev":
            pos = max(0, pos - 10)
        elif command == "next":
            pos = min(pos + 10, video_len)
        
        if op_start <= pos <= op_end:
            pos = op_end
    answer = to_datetime(pos)
    
    return answer