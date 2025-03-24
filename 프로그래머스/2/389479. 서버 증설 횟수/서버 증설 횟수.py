def solution(players, m, k):
    servers = [0 for _ in range(24)]
    for hour, n_players in enumerate(players):
        cur_server = sum(servers[max(0, hour-k+1):hour+1])
        max_players_capacity = (cur_server * m) + m - 1
        while n_players > max_players_capacity:
            servers[hour] += 1
            max_players_capacity += m
    return sum(servers)