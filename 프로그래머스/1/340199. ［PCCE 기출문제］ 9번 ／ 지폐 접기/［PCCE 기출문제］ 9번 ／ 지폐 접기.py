def solution(wallet, bill):
    answer = 0
    wallet_min = min(*wallet)
    wallet_max = max(*wallet)
    while min(*bill) > wallet_min or max(*bill) > wallet_max:
        if bill[0] < bill[1]:
            bill[1] //= 2
        elif bill[0] > bill[1]:
            bill[0] //= 2
        answer += 1
    return answer