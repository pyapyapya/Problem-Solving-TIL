import sys
from sys import stdin, stdout

cases = int(stdin.readline())

for case in range(cases):
    n, n_query = map(int, sys.stdin.readline().split())
    arr = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

    row_sum = [0 for i in range(n)]
    col_sum = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            row_sum[i] += arr[i][j]
            col_sum[i] += arr[j][i]

    for query in range(n_query):
        r1, c1, r2, c2, v = map(int, stdin.readline().rstrip().split())

        for i in range(r1, r2+1):
            row_sum[i-1] += v * (c2-c1+1)

        for i in range(c1, c2+1):
            col_sum[i-1] += v * (r2-r1+1)

    stdout.write(' '.join(map(str, row_sum))+'\n')
    stdout.write(' '.join(map(str, col_sum))+'\n')

