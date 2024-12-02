def solution(board, h, w):
    answer = 0
    n = len(board)
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    color = board[h][w]
    
    for i in range(4):
        mv_h = h + dh[i]
        mv_w = w + dw[i]
        if 0 <= mv_w < n and 0 <= mv_h < n:
            if board[mv_h][mv_w] == color:
                answer += 1

    return answer