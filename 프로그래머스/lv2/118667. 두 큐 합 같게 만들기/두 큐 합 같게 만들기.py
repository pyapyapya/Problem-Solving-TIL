from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    length = len(queue1) * 2
    half_sum = (sum1 + sum2) // 2
    
    if sum1 == half_sum:
        return 0
    
    arr = queue1.extend(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    idx1 = 0
    idx2 = 0
    answer = 0
    while idx1 < length and idx2 < length:
        if sum1 == half_sum:
            return idx1 + idx2
        elif sum1 > half_sum:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            idx1 += 1
            queue2.append(queue1.popleft())
        else:
            sum2 -= queue2[0]
            sum1 += queue2[0]
            idx2 += 1
            queue1.append(queue2.popleft())
        answer += 1
    return -1
