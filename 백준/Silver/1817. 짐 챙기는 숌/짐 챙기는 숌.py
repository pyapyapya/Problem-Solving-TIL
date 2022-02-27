import sys

n_book, box_weight = map(int, sys.stdin.readline().split())
if n_book == 0:
    print(0)
else:
    book_weights = list(map(int, sys.stdin.readline().split()))

    ans = 0
    cur_weight = book_weights[0]
    for i in range(len(book_weights)-1):
        if cur_weight + book_weights[i+1] > box_weight:
            cur_weight = 0
            ans += 1
        cur_weight += book_weights[i+1]
    if cur_weight > 0:
        ans += 1
    print(ans)
