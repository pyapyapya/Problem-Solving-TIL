def solution(diffs, times, limit):
    low = 1
    limit_level = max(diffs)
    high = 100000
    answer = 100000
    while low <= high:
        level = (low + high) // 2
        clear_times = 0
        is_timeout = False
        is_level_exceeded = False

        for idx, (diff, time_cur) in enumerate(zip(diffs, times)):
            if idx == 0:
                clear_times += time_cur
                continue
            iters = diff-level if diff-level > 0 else 0
            time_prev = times[idx-1]
            clear_times += (time_prev+time_cur) * iters + time_cur
            if clear_times > limit:
                is_timeout = True
                break

        if is_timeout:
            low = level + 1
        else:
            answer = min(level, answer)
            high = level - 1
    return answer