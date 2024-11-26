"""
풀이 시간: 1시간 30분
예상 난이도: 백준 실버 1 / BFS
[접근 방식]
- BFS로 모든 지형을 탐색한다. 탐색 과정 중 아래의 조건을 만족해야 한다.
1) 각각의 chunk를 구분해야한다.
2) 각각의 chunk는 넓이를 가져야한다.
=> chunk number: chunk size를 같는 dict 자료 구조 필요

[오래걸린 부분]
1. size 처리.
- size를 초기화하기 위해 while queue 시작 부분에 size를 두었음

<왜 그렇게 생각했는가?>
- size를 계산하는 것은 queue가 돌아가는 횟수라 생각했고, mv 부분에서 size를 더해주었기 때문에 미래 시점의 size를 계산함
- => 넓이가 1보다 큰 경우와 1인 경우의 결과가 달랐음.

2. 디버깅
- 디버깅 할 때 무의식적으로 값을 한두번 바꾸어보는 행위를 반복
- 정신차리고 알고리즘 흐름에 집중

<앞으로..>
- 알고리즘 흐름에 집중하고, 문법에 맞게 적용하고 있는지 확인하기
"""

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
