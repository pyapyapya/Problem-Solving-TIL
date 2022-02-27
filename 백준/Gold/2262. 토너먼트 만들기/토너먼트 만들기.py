import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0

while len(arr) > 1:
    cur_tournament = set()
    for num in range(len(arr), 1, -1):
        idx = arr.index(num)
        if idx == 0:
            if arr[idx+1] in cur_tournament:
                break
            ans += abs(arr[idx]-arr[idx+1])

        elif idx == len(arr)-1:
            if arr[idx-1] in cur_tournament:
                break
            ans += abs(arr[idx]-arr[idx-1])

        else:
            if arr[idx-1] in cur_tournament and arr[idx+1] in cur_tournament:
                break
            ans += min(abs(arr[idx]-arr[idx-1]), abs(arr[idx]-arr[idx+1]))
        arr.pop(idx)
print(ans)
