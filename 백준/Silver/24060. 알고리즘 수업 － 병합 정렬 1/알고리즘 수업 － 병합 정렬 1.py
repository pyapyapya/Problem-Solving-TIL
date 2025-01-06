n, k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

def merge_sort(arr, p, r, k, cnt = 0):
    if p < r:
        q = (p+r) // 2
        arr, cnt = merge_sort(arr, p, q, k, cnt)
        arr, cnt = merge_sort(arr, q+1, r, k, cnt)
        arr, cnt = merge(arr, p, q, r, k, cnt)
    return arr, cnt


def merge(arr, p, q, r, k, cnt):
    i = p
    j = q + 1
    tmp = []
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i <= q:
        tmp.append(arr[i])
        i += 1
    while j <= r:
        tmp.append(arr[j])
        j += 1
    
    i = p
    t = 0
    while i <= r:
        arr[i] = tmp[t]
        cnt += 1
        if cnt == k:
            print(arr[i])
        i += 1
        t += 1
    return arr, cnt

arr, cnt = merge_sort(arr, 0, len(arr) - 1, k)
if cnt < k:
    print(-1)