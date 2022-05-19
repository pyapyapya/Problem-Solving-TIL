"""
How to work LRU Algorithm
가장 오랫동안 참조되지 않은 페이지를 교체

How to define Cache Hit/Miss?

"""

from collections import deque


def LRU(cacheSize, cities):
    deq = deque([], maxlen=cacheSize)
    run_time = 0

    for city in cities:
        city = city.lower()
        if city in deq:
            if len(deq) <= cacheSize:
                deq.remove(city)
            run_time += 1
        else:
            run_time += 5

        deq.append(city)
    return run_time

def solution(cacheSize, cities):
    answer = 0
    answer = LRU(cacheSize, cities)
    return answer
