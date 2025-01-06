n = int(input())


def is_palindrome(s):
    recursion(s, 1)

def recursion(s, cnt):
    if len(s) <= 1:
        print(1, cnt)
        return True

    if s[0] != s[-1]:
        print(0, cnt)
        return False
    else:
        recursion(s[1:-1], cnt+1)


for i in range(n):
    s = input()
    is_palindrome(s)
