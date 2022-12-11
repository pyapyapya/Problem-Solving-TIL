select j.flavor
from july j
left join first_half fh
on fh.shipment_id = j.shipment_id
group by j.flavor
order by sum(fh.total_order) + sum(j.total_order) desc
limit 3