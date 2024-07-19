import sys
input = sys.stdin.readline

def average(arr):
    return round(sum(arr) / len(arr))

def median(arr):
    return arr[len(arr) // 2]

def max_freq(counts):
    order = sorted(counts.items(), key=lambda x: (x[1], -x[0]), reverse=True)
    if len(order) > 1 and order[0][1] == order[1][1]:
        return order[1][0]
    else:
        return order[0][0]

def get_range(arr):
    return max(arr) - min(arr)

n = int(input())
arr = []
counts = {}
for i in range(n):
    num = int(input())
    arr.append(num)
    if num not in counts:
        counts[num] = 0
    counts[num] += 1
arr = sorted(arr)
print(average(arr))
print(median(arr))
print(max_freq(counts))
print(get_range(arr))