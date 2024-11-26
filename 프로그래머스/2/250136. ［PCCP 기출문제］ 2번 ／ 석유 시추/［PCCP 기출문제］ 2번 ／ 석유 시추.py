def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    
    check = [[0 for _ in range(m)] for _ in range(n)]
    
    chunks = {}
    num = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0 or check[i][j] > 0:
                continue
            
            queue = [(i, j)]
            size = 0
            while queue:
                cur_x, cur_y = queue.pop(0)
                check[cur_x][cur_y] = num
                for x, y in zip(dx, dy):
                    mv_x = cur_x + x
                    mv_y = cur_y + y
                    if not (0 <= mv_x < n and 0 <= mv_y < m):
                        continue
                    if land[mv_x][mv_y] == 0:
                        continue
                    if check[mv_x][mv_y] > 0:
                        continue
                    check[mv_x][mv_y] = num
                    queue.append((mv_x, mv_y))
                size += 1
            chunks[num] = size
            num += 1
    for j in range(m):
        chunk_nums = set()
        for i in range(n):
            if check[i][j]:
                chunk_nums.add(check[i][j])
        sizes = sum([chunks[size] for size in chunk_nums])
        answer = max(answer, sizes)
    return answer
