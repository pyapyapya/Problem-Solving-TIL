# [hackerrank] Weather Observation Station 5
[link](https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true)

## 풀이과정
<li>이전 문제들이 간단한 select문제여서 슥슥 밀다가 처음으로 난관에</li>
<li>서브 쿼리를 써야할까? 라는 생각을 했지만, 서브 쿼리를 쓰는 것에 익숙치 않아서 그마저도 어려웠다.</li>
<li>생각보다 정렬 문제로 접근할 수 있었고, 서브 쿼리 해결 방식도 익혀두어야 할 것 같다.</li>

## 문제점 & 피드백
<li>오랜만에 쓰는 SQL이었는데, 꾸준히 연습해둬야 필요할 때 빠르게 쓸 수 있을 것 같다.</li>

## 코드

```SQL
select city, length(city)
from station
order by length(city), city
limit 1;

select city, length(city)
from station
order by length(city) desc, city
limit 1;
```
