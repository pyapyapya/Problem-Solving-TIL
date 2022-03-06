n = int(input())
k = int(input())
arr = list(map(int, input().split()))
ans = 0
if n <= k:
    print(ans)
else:
    arr = sorted(arr)
    diff = [arr[i+1]-arr[i] for i in range(n-1)]
    diff = sorted(diff)
    for i in range(n-k):
        ans += diff[i]
    print(ans)
