"""
1. 4개 찾기
2. 블록 내리기
3. 4개 블럭이 없을 때 끝나는 경우 구현
"""

def pop_elements(checklist, board, n_row, n_col):
    dx = (1, 1, 0)
    dy = (0, 1, 1)
    while checklist:
        cur_x, cur_y = checklist.pop()
        board[cur_x][cur_y] = '0'
        for i in range(3):
            mv_x = cur_x + dx[i]
            mv_y = cur_y + dy[i]
            board[mv_x][mv_y] = '0'

        
def drop_elements(board, n_row, n_col):
    for y in range(n_col):
        friends = []
        for x in range(n_row):
            if board[x][y] != '0':
                friends.append(board[x][y])
        if friends:
            for x in range(n_row-len(friends)):
                board[x][y] = '0'
            for x in range(n_row-len(friends), n_row):
                board[x][y] = friends.pop(0)


def get_answer(board, n_row, n_col):
    answer = 0
    for row in range(n_row):
        for col in range(n_col):
            if board[row][col] == '0':
                answer += 1
    return answer

def solution(m, n, board):
    n_row = m
    n_col = n
    board = [list(board[x]) for x in range(n_row)]
    answer = 0
    
    dx = (1, 1, 0)
    dy = (0, 1, 1)
    check = False
    while not check:
        checklist = []
        check = True
        for x in range(n_row-1):
            for y in range(n_col-1):
                cnt = 1
                cur_str = board[x][y]
                if cur_str == '0':
                    continue
                for i in range(3):
                    mv_x = x + dx[i]
                    mv_y = y + dy[i]
                    mv_str = board[mv_x][mv_y]
                    if cur_str == mv_str:
                        cnt += 1
                if cnt == 4:
                    checklist.append((x, y))
                    answer += 1
                    check = False
        pop_elements(checklist, board, n_row, n_col)
        drop_elements(board, n_row, n_col)
    answer = get_answer(board, n_row, n_col)
    return answer
