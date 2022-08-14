def solution(arr):
    answer = 0
    n_arr = len(arr)
    if n_arr <= 2:
        return n_arr
    
    l_min = arr[0]
    r_min = arr[-1]
    
    left = [arr[0]]
    right = [arr[-1]]
    
    for i in range(1, n_arr):
        if l_min > arr[i]:
            l_min = arr[i]
        left.append(l_min)
        if r_min > arr[-i-1]:
            r_min = arr[-i-1]
        right.append(r_min)
    
    right.reverse()

    for i in range(1, n_arr-1):
        if left[i-1] > arr[i] or right[i+1] > arr[i]:
            answer += 1

    answer += 2
            
    return answer
