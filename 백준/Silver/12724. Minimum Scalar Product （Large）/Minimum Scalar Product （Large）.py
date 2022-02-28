import sys
t = int(sys.stdin.readline())

for case in range(t):
    v_size = int(sys.stdin.readline())
    vec1 = list(map(int, sys.stdin.readline().split()))
    vec2 = list(map(int, sys.stdin.readline().split()))

    vec1 = sorted(vec1)
    vec2 = sorted(vec2, reverse=True)

    ans = 0
    for i in range(v_size):
        ans += vec1[i] * vec2[i]

    sys.stdout.write(f'Case #{str(case+1)}: {str(ans)}\n')
