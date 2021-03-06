def get_person_place(people, place):
    for i in range(len(place)):
        for j in range(len(place)):
            if place[i][j] == 'P':
                people.append((i, j))


def keep_distance(people, place):
    global dx
    global dy

    for person in people:
        visit = [[False for _ in range(len(place))] for _ in range(len(place))]

        r = person[0]
        c = person[1]
        visit[r][c] = True
        q = [(r, c, 0)]

        while q:
            cur_r, cur_c, cur_d = q.pop(0)
            if cur_d <= 2:
                if 1 <= cur_d <= 2 and place[cur_r][cur_c] == 'P':
                    return False

                for i in range(4):
                    mv_r = cur_r + dx[i]
                    mv_c = cur_c + dy[i]
                    next_t = cur_d + 1
                    if 0 <= mv_r < len(place) and 0 <= mv_c < len(place) and not visit[mv_r][mv_c] and place[mv_r][mv_c] != 'X':
                        visit[mv_r][mv_c] = True
                        q.append((mv_r, mv_c, next_t))
    return True

def solution(places):
    global dx
    global dy
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = []
    for place in places:
        people = []
        get_person_place(people, place)
        check = keep_distance(people, place)
        if not check:
            answer.append(0)
        else:
            answer.append(1)
    return answer
