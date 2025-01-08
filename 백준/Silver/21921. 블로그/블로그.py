n, x = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

answer = 0
cnt = 0

for i in range(n-x+1):
    if i == 0:
        visits = sum(arr[:x])
    else:
        visits = visits - arr[i-1] + arr[i+x-1]

    if visits > answer:
        answer = visits
        cnt = 1
    elif visits == answer:
        cnt += 1

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(cnt)