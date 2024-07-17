import sys
input = sys.stdin.readline

n, w, l = map(int, input().split(" "))
trucks = list(map(int, input().split(" ")))
state = 0
time = 0
stack = []
while True:
    time += 1

    for idx in range(len(stack) - 1, -1, -1):
        if idx == 0 and stack[0][1] == w:
            state -= stack[0][0]
            stack.pop(0)
            break
        
        stack[idx] = (stack[idx][0], stack[idx][1] + 1)

    if len(stack) < w and len(trucks) > 0 and trucks[0] + state <= l:
        truck = trucks.pop(0)
        state += truck
        stack.append((truck, 1))

    if not stack:
        break

print(time)