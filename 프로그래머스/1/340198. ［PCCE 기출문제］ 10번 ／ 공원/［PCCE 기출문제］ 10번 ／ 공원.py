def has_seat(park, size, i, j):
    for s_h in range(size):
        for s_w in range(size):
            if park[i+s_h][j+s_w] != "-1":
                return False
    return True

def solution(mats, park):
    h = len(park)
    w = len(park[0])
    
    mats = sorted(mats, reverse=True)
    while mats:
        size = mats.pop(0)
        if h < size or w < size:
            continue
        for i in range(h-size+1):
            for j in range(w-size+1):
                if has_seat(park, size, i, j):
                    return size

    return -1