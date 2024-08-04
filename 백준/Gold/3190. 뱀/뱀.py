from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    r, c = map(int, input().split(" "))
    apples.append((r-1, c-1))

directions = {} # time, direction
l = int(input())
for _ in range(l):
    line = input().split(" ")
    time, direction = int(line[0]), line[1].strip()
    directions[time] = direction

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
direct = 1
elapsed_time = 0
snake = deque([(0, 0)])

while True:
    cur_r, cur_c = snake[-1]
    mv_r = cur_r + dr[direct % 4]
    mv_c = cur_c + dc[direct % 4]
    elapsed_time += 1
    if (mv_r, mv_c) in snake or not 0 <= mv_r < n or not 0 <= mv_c < n:
        break
    
    if len(apples) > 0 and (mv_r, mv_c) in apples:
        snake.append((mv_r, mv_c))
        apples.remove((mv_r, mv_c))
    else:
        snake.append((mv_r, mv_c))
        snake.popleft()

    if elapsed_time in directions:
        direction = directions[elapsed_time]
        if direction == "L":
            direct -= 1
        elif direction == "D":
            direct += 1
        del directions[elapsed_time]
print(elapsed_time)