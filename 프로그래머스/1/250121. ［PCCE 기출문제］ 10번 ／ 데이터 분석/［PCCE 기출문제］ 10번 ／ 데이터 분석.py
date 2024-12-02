def solution(data, ext, val_ext, sort_by):
    answer = []
    maps = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3,
    }
    
    for d in data:
        idx = maps[ext]
        if d[idx] < val_ext:
            answer.append(d)
    idx = maps[sort_by]
    answer = sorted(answer, key=lambda x: x[idx])
    return answer