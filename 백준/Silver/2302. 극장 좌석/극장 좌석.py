import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [False for _ in range(n)]
dp = [0 for i in range(n+1)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(m):
    vip = int(sys.stdin.readline())
    arr[vip-1] = True

cnt = 0
ans = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

for i in range(n):
    if not arr[i]:
        cnt += 1
    else:
        ans *= dp[cnt]
        cnt = 0

if cnt > 0:
    ans *= dp[cnt]
print(ans)
