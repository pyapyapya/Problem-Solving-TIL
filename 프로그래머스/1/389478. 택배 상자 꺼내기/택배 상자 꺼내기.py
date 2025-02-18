def solution(n, w, num):
    answer = 0
    
    h = 0
    p = 0
    i = 1
    s = [[] for _ in range(w)]
    while i <= n:
        if h % 2 == 0:
            s[p].append(i)
        else:
            s[w-p-1].append(i)
        p += 1
        if i % w == 0:
            h += 1
            p = 0
        i += 1
    
    check = False
    for p in range(w):
        answer = 0
        i = 0
        while s[p]:
            answer += 1
            if s[p].pop() == num:
                check = True
                break
        if check:
            break

    return answer