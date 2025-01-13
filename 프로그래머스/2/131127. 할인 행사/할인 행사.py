from collections import deque

def solution(want, number, discount):
    answer = 0
    
    # want에 없는 것은 넣지 않고 패스한다.
    # 만약 deque이 비었다면 채워준다.
    # {want:number} 딕셔너리를 만들고, 모든 원소가 음수가 되면 카운트한다.
    deq = deque()
    s = set(want)
    n_wants = sum(number)
    for idx in range(0, len(discount)-n_wants+1):
        if len(deq) == 0:
            deq = deque(discount[idx:idx+n_wants])
        else:
            deq.popleft()
            deq.append(discount[idx+n_wants-1])

        dic = dict(zip(want, number))
        if len(set(deq) - s) > 0:
            continue
        cnt = 0
        for item in deq:
            if dic[item] > 0:
                dic[item] -= 1
                cnt += 1
        if cnt == n_wants:
            answer += 1
        
    return answer