from math import ceil

def time_convert(time):
    time = time.split(':')
    minutes = int(time[0]) * 60 + int(time[1])
    return minutes

def solution(fees, records):
    answer = []
    
    dic = {}
    
    free_time = fees[0]
    start_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]
    
    for record in records:
        (cur_time, car_number, cur_state) = record.split(' ')
        
        cur_time = time_convert(cur_time)
        
        if car_number not in dic:
            dic[car_number] = (cur_time, 'IN', 0)
        else:
            last_time, last_state, total_times = dic[car_number]
            if cur_state == 'OUT':
                usage_time = cur_time - last_time
                total_times += usage_time
                dic[car_number] = (cur_time, 'OUT', total_times)
            else:
                dic[car_number] = (cur_time, 'IN', total_times)
    dic = sorted(dic.items(), key=lambda x: x[0])
    for key, value in dic:
        cur_time, state, total_times = value
        if state == 'IN':
            total_times += (60 * 24 - 1) - cur_time
        total_times = total_times - free_time

        if total_times < 0:
            total_times = 0
        fee = start_fee + ceil((total_times) / per_time) * per_fee
        answer.append(fee)

    return answer
