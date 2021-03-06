def solution(files):
    answer = []
    for file in files:
        file += '#'
        head = ''
        number = ''
        tail = ''
        
        is_head = False
        is_number = False
        
        number_idx = 0
        for idx, ch in enumerate(file):
            if is_head and ((not ch.isdigit()) or idx - head_idx > 4):
                number = file[head_idx:idx]
                tail = file[idx:]
                answer.append((head, number, tail))
                print(head, number, tail)
                break
            if not is_head and ch.isdigit():
                head_idx = idx
                head = file[:head_idx]
                is_head = True
    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(file)[:-1] for file in answer]
    return answer
