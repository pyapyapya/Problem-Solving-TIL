def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
        answer += max(len(deliveries), len(pickups)) * 2

        n_delivers = cap
        while n_delivers > 0 and deliveries:
            house = len(deliveries) - 1
            if n_delivers >= deliveries[house]:
                n_delivers -= deliveries[house]
                deliveries.pop()
            else:
                deliveries[house] -= n_delivers
                n_delivers = 0

        n_delivers = cap
        while n_delivers > 0 and pickups:
            house = len(pickups) - 1
            if n_delivers >= pickups[house]:
                n_delivers -= pickups[house]
                pickups.pop()
            else:
                pickups[house] -= n_delivers
                n_delivers = 0
        
    
    return answer