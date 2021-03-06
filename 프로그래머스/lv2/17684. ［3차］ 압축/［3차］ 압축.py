def solution(msg):
    dic = {}
    answer = []
    for i in range(26):
        dic[chr(ord('A')+i)] = i+1
    
    idx = 27
    s = msg[0]
    for w in msg[1:]:
        s += w
        if s not in dic:
            dic[s] = idx
            answer.append(dic[s[:-1]])
            s = s[-1]
            idx += 1
    answer.append(dic[s])

    return answer
