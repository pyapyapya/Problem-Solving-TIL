import sys
input = sys.stdin.readline

r, c = map(int, input().strip().split(" "))
k = int(input())
check = [[False for _ in range(c)] for _ in range(r)]
for _ in range(k):
    br, bc = map(int, input().strip().split(" "))
    check[br][bc] = True
cur_r, cur_c = map(int, input().strip().split(" "))
check[cur_r][cur_c] = True
queue = list(map(int, input().strip().split(" ")))
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

i = 0
count = 0
direct = queue[i] - 1

while True:
    move_r = cur_r + dr[direct]
    move_c = cur_c + dc[direct]
    if 0 <= move_c < c and 0 <= move_r < r and not check[move_r][move_c]:
        cur_r = move_r
        cur_c = move_c
        check[cur_r][cur_c] = True
        count = 0
    else:
        i += 1
        direct = queue[i%4] - 1
        count += 1
    
    if count > 4:
        break

print(cur_r, cur_c)