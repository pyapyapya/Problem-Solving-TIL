"""
처음에는 Greedy하게 돌리면 될 것 같았는데 그러면 O(N^2)이 나와서 시간 초과가 나올 것이고,
투포인터로 하기에는 구현 방법을 떠올리지 못했는데, 고민하다가 다른 사람의 풀이에서 힌트를 많이 받았다.
"""

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
