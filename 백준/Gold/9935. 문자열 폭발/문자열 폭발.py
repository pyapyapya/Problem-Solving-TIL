string = input()
window = list(input())
window_size = len(window)
stack = []

for s in string:
    stack.append(s)
    while len(stack) >= window_size and stack[-window_size:] == window:
        cnt = 0
        while cnt != window_size:
            stack.pop()
            cnt += 1

if not stack:
    print('FRULA')
else:
    print(''.join(stack))