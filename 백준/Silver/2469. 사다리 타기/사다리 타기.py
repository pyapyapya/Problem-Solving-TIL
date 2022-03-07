from sys import stdin, stdout

k = int(stdin.readline())
n = int(stdin.readline())


start = [chr(ord('A')+i) for i in range(k)]
wants = list(stdin.readline().rstrip())

ladder = [stdin.readline() for i in range(n)]

pivot = -1


for i in range(n):
    if ladder[i][0] == '?':
        pivot = i
        break

    for j in range(k-1):
        if ladder[i][j] == '-':
            start[j], start[j+1] = start[j+1], start[j]

for i in range(n-1, pivot, -1):
    for j in range(k - 1):
        if ladder[i][j] == '-':
            wants[j], wants[j + 1] = wants[j + 1], wants[j]

check = 0
ans = ''
for i in range(k-1):
    if check >= 2:
        break
    if start[i] != wants[i]:
        start[i], start[i + 1] = start[i + 1], start[i]
        check += 1
        ans += '-'
    else:
        check = 0
        ans += '*'

if check >= 2:
    ans = 'x' * (k-1)
    print(ans)
else:
    print(ans)