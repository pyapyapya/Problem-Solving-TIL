### 접근 방법
- 도전을 거의 3~4번 한 문제였는데, 여전히 푸는데 어려움이 있었다.
- 이번에는 꼭 풀자는 마인드로 1주일동안 고민하고 풀이도 봤지만, 여전히 내 풀이가 어떤 문제점을 가지고 있는지 찾기가 어려웠다.
- 최종적으로 깨달은 점은, 유일성을 만족하는 것만 찾고 있었고, 최소성을 이해하지 못했다 (계속 이 정의를 보고 있었음에도 불구하고)
- 예를 들어, A, B, C .. 가 있을 때, A, (B, C)가 있으면 (B, D, E)가 최소성이 보장이 안된다고 생각을 했었다.
- 이 부분을 처리해 줌으로써 해결을 하였다.


``` python3
from itertools import combinations


def solution(relation):
    answer = 0
    
    n_row = len(relation)
    n_col = len(relation[0])

    num = [i for i in range(n_col)]
    check = [False for i in range(n_col)]
    candidate_key = []
    
    for i in range(1, n_col+1):
        combination = list(combinations(num, i))
        for comb in combination:
            s = set()
            check_candidate = True
                
            for row in relation:
                key = ''
                for idx in comb:
                    key += row[idx]
                if key not in s:
                    s.add(key)
                else:
                    check_candidate = False
                    break
            if check_candidate:
                flag = True
                for key in candidate_key:
                    if set(key).issubset(comb):
                        flag = False
                        break
                if flag:
                    candidate_key.append(comb)
    return len(candidate_key)

```
