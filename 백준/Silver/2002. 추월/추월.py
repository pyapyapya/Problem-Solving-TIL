import sys
input = sys.stdin.readline

n = int(input()) * 2
d = {}

answer = 0
order = 1
min_n = 1
for _ in range(n):
    c_number = input().strip()
    if c_number not in d:
        d[c_number] = order
        order += 1
    else:
        if d[c_number] > min_n:
            answer += 1
        del d[c_number]
        if d:
            min_n = min(d.values())
print(answer)