def to_minutes(time):
    return time // 100 * 60 + time % 100

def check_late(schedule, timelog, startday):
    s = startday
    for t in timelog:
        if s in {6, 7}:
            s += 1
            if s == 8:
                s = 1
            continue
        if to_minutes(t) > to_minutes(schedule) + 10:
            return True
        s += 1

    return False

def solution(schedules, timelogs, startday):
    answer = 0
    for idx, schedule in enumerate(schedules):
        timelog = timelogs[idx]
        is_late = check_late(schedule, timelog, startday)
        if not is_late:
            answer += 1
    return answer