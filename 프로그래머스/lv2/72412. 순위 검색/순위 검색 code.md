### 접근 방법
- 단순히 리스트로 반복하게 되면 시간초과가 될 것이라고 생각했고, query에 대해서 순서대로 적절히 select할 수 있을 것이라고 판단함
- 4중 딕셔너리를 만들어야 하는데, 상당한 노가다 작업이나 문법을 읽어봐야 할 것 같았고, 이것이 최선인가?
- 결국 다른 사람들의 풀이를 보았는데, 4개의 column을 하나로 파싱하여 key-value로 만든 점이 생각하지 못했다.
- 이때 key-value 조합은 다양하게 나올 수 있는데, 조합을 위해서 comb method를 처음으로 사용해 봄
- 그리고 이 문제의 핵심 접근 방식은 한 info에 대해 접근할 수 있는 경우의 수는 2x2x2x2 = 16가지 방법인데, 나는 그런 생각보다는, 만들수 있는 경우의 수에만 집중했던 것 같다.
- score는 이진 탐색을 사용하면 될 것이라고 생각은 했지만, 모호하게 생각했던 것 같고, bisect library 사용해본 적이 없어서, 이 부분도 공부하면 좋을 것 같다.


```python
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    info_dict = {}
    
    for i in info:
        information = i.split()
        key = information[:-1]
        value = int(information[-1])
        for n in range(5):
            comb_key = list(combinations(key, n))
            for k in comb_key:
                info_key = ''.join(k)
                if info_key not in info_dict:
                    info_dict[info_key] = [value]
                else:
                    info_dict[info_key].append(value)
    
    for key in info_dict.keys():
        info_dict[key] = sorted(info_dict[key])
    
    answer = []
    for q in query:
        q_value = q.split()[-1]
        key = q[:-len(q_value)].strip().split(' and ')
        key = ''.join(key)
        key = key.replace('-', '')

        if key not in info_dict:
            answer.append(0)
        else:
            value = info_dict[key]
            q_value = int(q_value)
            
            ans = bisect_left(value, q_value)
            answer.append(len(value) - ans)
        
    return answer
```
