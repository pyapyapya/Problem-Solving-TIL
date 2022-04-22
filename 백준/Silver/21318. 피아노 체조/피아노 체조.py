from sys import stdin, stdout

n = int(stdin.readline())

score = list(map(int, stdin.readline().split()))
score.insert(0, 0)

suffix_sum = [0 for _ in range(n+1)]

cnt = 0
for i in range(1, n):
    if score[i] > score[i+1]:
        cnt += 1
        suffix_sum[i] = cnt
    else:
        suffix_sum[i] = cnt

suffix_sum[n] = cnt
m = int(stdin.readline())

for i in range(m):
    s, e = map(int, stdin.readline().split())
    ans = 0
    if e-s == 0:
        stdout.write(str(ans) + '\n')
    else:
        ans = suffix_sum[e-1] - suffix_sum[s-1]
        stdout.write(str(ans)+'\n')
