def solution(queue1, queue2):
    head = 0
    tail = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1.extend(queue2)

    half_sum = (sum1 + sum2) // 2
    
    if sum1 == half_sum:
        return 0
    answer = 0
    while tail < len(queue1):
        if sum1 == half_sum:
            return answer
        elif sum1 > half_sum:
            sum1 -= queue1[head]
            sum2 += queue1[head]
            head += 1
            answer += 1
        else:
            sum1 += queue1[tail]
            sum2 -= queue1[tail]
            tail += 1
            answer += 1
    return -1