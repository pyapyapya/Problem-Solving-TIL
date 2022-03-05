n, p = map(int, input().split())

arr = [n]
ans = []

while True:
    check = False
    for d_n in arr:
        num = 0
        while d_n > 0:
            mod = d_n % 10
            d_n = d_n // 10
            num += pow(mod, p)
        if num not in arr:
            arr.append(num)
        else:
            ans = arr.index(num)
            check = True
    if check:
        break

print(ans)
