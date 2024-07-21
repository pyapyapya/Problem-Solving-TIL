import sys
input = sys.stdin.readline

c, r = map(int, input().split(" "))
n = int(input())

answer = 0
dist = 0
total_dist = 2 * c + 2 * r
arr = []

for i in range(n):
    direction, dist = list(map(int, input().split(" ")))
    arr.append((direction, dist))
start_direct, start_point = map(int, input().split(" "))

get_answer = lambda x: min(x, total_dist - x)

while arr:
    target_direct, target_point = arr.pop()
    direct_pair = {start_direct, target_direct}
    if start_direct == target_direct:
        dist = abs(start_point - target_point)
        answer += get_answer(dist)
    elif direct_pair == {1, 2}:
        dist = start_point + target_point + r
        answer += get_answer(dist)
    elif direct_pair == {1, 3}:
        dist = start_point + target_point
        answer += get_answer(dist)
    elif direct_pair == {1, 4}:
        if start_direct == 1:
            dist = c - start_point + target_point
        else:
            dist = c - target_point + start_point
        answer += get_answer(dist)
    elif direct_pair == {2, 3}:
        if start_direct == 2:
            dist = start_point + r - target_point
        else:
            dist = target_point + r - start_point
        answer += get_answer(dist)
    elif direct_pair == {2, 4}:
        dist = c + r - (start_point + target_point)
        answer += get_answer(dist)
    elif direct_pair == {3, 4}:
        dist = start_point + target_point + c
        answer += get_answer(dist)
    else:
        ValueError("Invalid")
print(answer)