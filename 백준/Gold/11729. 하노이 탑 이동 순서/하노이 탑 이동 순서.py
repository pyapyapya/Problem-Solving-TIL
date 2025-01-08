n = int(input())

def recursive(n, a, c, arr):
    if n == 1:
        return [(a, c)]
    else:
        b = 6-a-c
        return recursive(n-1, a, b, arr) + recursive(1, a, c, arr) + recursive(n-1, b, c, arr)

arr = []
arr = recursive(n, 1, 3, arr)
print(len(arr))
for x, y in arr:
    print(x, y)