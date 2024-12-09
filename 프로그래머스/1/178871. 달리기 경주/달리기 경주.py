from collections import deque

def solution(players, callings):
    players_rank = {k:v for v, k in enumerate(players)}
    callings = deque(callings)
    while callings:
        player = callings.popleft()
        rank = players_rank[player]
        overtaked_player = players[rank-1]
        players[rank-1], players[rank] = players[rank], players[rank-1]
        
        players_rank[player] -= 1
        players_rank[overtaked_player] += 1
    return players