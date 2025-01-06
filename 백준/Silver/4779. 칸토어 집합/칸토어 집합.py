def recursion(s, n):
    if n == 1:
        return s
    else:
        n //= 3
        l = "-" * n
        m = " " * n
        r = "-" * n

        l = recursion(l, n)
        r = recursion(r, n)
        return l + m + r


while True:
    try:
        n = int(input())
        s = '-' * (3 ** n)
        s = recursion(s, len(s))
        print(s)
    except EOFError:
        break 