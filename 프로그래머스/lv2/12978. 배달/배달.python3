import heapq

def dijkstra(N, graph, start_node):
    dist = [1e6 for i in range(N+1)]
    dist[start_node] = 0
    pq = []
    heapq.heappush(pq, (0, start_node))
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        print(cur_node, cur_dist)
        if dist[cur_node] < cur_dist:
            continue
        for (next_node, weight) in graph[cur_node]:
            next_dist = cur_dist + weight
            if dist[next_node] > next_dist:
                dist[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))
    return dist
        
def solution(N, road, K):
    answer = 0
    graph = [[] for i in range(N+1)]
    for (a, b, c) in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    dist = dijkstra(N, graph, 1)
    
    for idx in range(1, N+1):
        if dist[idx] <= K:
            answer += 1
    return answer
