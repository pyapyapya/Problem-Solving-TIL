select fh.flavor
from first_half fh
join july j
on fh.flavor = j.flavor
group by fh.flavor
order by sum(fh.total_order) + sum(j.total_order) desc
limit 3