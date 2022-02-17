# [hackerrank] Weather Observation Station 5
[link](https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true)

## 문제 설명
<li>도시 정보를 가진 테이블이 주어졌을 때, 가장 짧은 길이를 가진 도시 이름과 그에 대한 길이와 가장 긴 길이를 가진 도시 이름과 그에 대한 길이를 구하는 문제였다.</li>
<li>길이가 같은 경우에는 알파벳 순으로 정렬했을 때 가장 앞에 있는 것을 선택하는 조건이 있었다.</li>

## 풀이과정
<li>생각보다 정렬 문제로 접근할 수 있었지만, 두 번의 select 과정을 거쳐야 하는 과정에서 어려움이 있었다.</li>
<li>서브 쿼리를 써야할까? 라는 생각을 했지만, 서브 쿼리를 쓰는 것에 익숙치 않아서 그마저도 어려웠다.</li>
<li>이후 문제에서 두 개의 쿼리로 분리해서 문제를 풀어도 된다고 한 것을 발견하여 생각보다 단순한 구조로 문제를 해결할 수 있었다.</li>

## 문제점 & 피드백
<li>SQL 문법과 구조에 대해서 많이 적응을 해야할 필요성을 느꼈다.</li>
<li>난이도가 쉬운 편에 속해 서브 쿼리를 안써도 되는 문제들이었지만, 앞으로 문제를 풀 때는 최대한 서브 쿼리를 익힐 수 있도록 노력해야겠다.</li>

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
