import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
square = []
for i in range(n):
    line = list(map(int, input().strip()))
    square.append(line)

threshold = min(n, m)
area = 1
for i in range(n):
    for j in range(m):
        for k in range(threshold):
            if i + k < n and j + k < m:
                if square[i][j] == square[i+k][j] == square[i][j+k] == square[i+k][j+k]:
                    new_area = abs(k + 1) ** 2
                    area = max(area, new_area)

print(area)