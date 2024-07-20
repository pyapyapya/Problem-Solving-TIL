import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
r, c, n = map(int, input().split(" "))

maps = []
for i in range(r):
    line = list(input().strip())
    maps.append(line)

for i in range(r):
    for j in range(c):
        if maps[i][j] == "O":
            maps[i][j] = 2
        else:
            maps[i][j] = 0


def print_answer(maps):
    for i in range(r):
        for j in range(c):
            if maps[i][j] > 0:
                sys.stdout.write("O")
            else:
                sys.stdout.write(".")
        sys.stdout.write("\n")


def set_bombs(maps):
    for i in range(r):
        for j in range(c):
            if maps[i][j] > 0:
                maps[i][j] -= 1
            else:
                maps[i][j] = 3
    return maps


def check_bombs(maps, check):
    queue = []
    for i in range(r):
        for j in range(c):
            if check[i][j]:
                maps[i][j] = 0
    return maps

def explode_bombs(maps):
    queue = []
    for i in range(r):
        for j in range(c):
            maps[i][j] -= 1
            if maps[i][j] == 0:
                queue.append((i, j))
    return maps, queue

if n == 1:
    print_answer(maps)
elif n % 2 == 0:
    maps = [[3 for _ in range(c)] for _ in range(r)]
    print_answer(maps)
else:
    time = 1
    while time != n:
        time += 1
        if time % 2 == 0:
            maps = set_bombs(maps)
            continue
        maps, queue = explode_bombs(maps)
        check = [[False for _ in range(c)] for _ in range(r)]
        while queue:
            cur_y, cur_x = queue.pop()
            check[cur_y][cur_x] = True
            for x, y in zip(dx, dy):
                move_x, move_y = (x + cur_x, y + cur_y)
                if 0 <= move_x < c and 0 <= move_y < r:
                    check[move_y][move_x] = True
                    
        maps = check_bombs(maps, check)

    print_answer(maps)