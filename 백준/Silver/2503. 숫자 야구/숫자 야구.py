import sys
input = sys.stdin.readline

turns = int(input())
counts = []
for i in range(turns):
    num, strikes, balls = map(int, input().split(" "))
    counts.append((num, strikes, balls))

check = [False for _ in range(1000)]
for i in range(1000):
    src = str(i)
    if len(set(src)) != 3 or "0" in src:
        continue

    is_win = True
    for n, strikes, balls in counts:
        n_strikes = 0
        n_balls = 0
        tar = str(n)
        for j in range(3):
            if src[j] == tar[j]:
                n_strikes += 1
            elif src[j] == tar[(j+1)%3] or src[j] == tar[(j+2)%3]:
                n_balls += 1
        if n_strikes != strikes or n_balls != balls:
            is_win = False
    if is_win:
        check[i] = True

answer = 0
for i in range(10, 1000):
    if check[i]:
        answer += 1
print(answer)