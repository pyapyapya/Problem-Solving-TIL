def solution(plans):
    answer = []
    queue = []
    
    diff = None
    for plan in plans:
        time = list(map(int, plan[1].split(":")))
        plan[1] = time[0] * 60 + time[1]
        plan[2] = int(plan[2])
    
    plans = sorted(plans, key=lambda x: x[1])
    
    while len(plans) > 1:
        name, start, playtime = plans.pop(0)
        end = plans[0][1]
        diff = end - start
        
        # queue가 있는 경우
        while diff >= playtime: # 과제를 끝낼 수 있는 경우
            diff -= playtime
            answer.append(name)
            if queue:
                name, end, playtime = queue.pop()
            else:
                break

        else: # 과제를 끝낼 수 없는 경우
            playtime -= diff
            start = end
            queue.append([name, start, playtime])
    else:
        while plans:
            plan = plans.pop(0)
            answer.append(plan[0])
        while queue:
            delayed_plan = queue.pop()
            answer.append(delayed_plan[0])
    return answer
