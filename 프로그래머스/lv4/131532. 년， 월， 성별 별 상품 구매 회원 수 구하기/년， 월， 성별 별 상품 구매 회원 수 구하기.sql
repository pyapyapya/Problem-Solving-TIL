SELECT YEAR(sales_date), MONTH(sales_date), gender, count(distinct on_sale.user_id)
from online_sale on_sale
join (select * from user_info where gender is not null) u_info
on on_sale.user_id = u_info.user_id
group by YEAR(sales_date), MONTH(sales_date), gender
order by YEAR(sales_date), MONTH(sales_date), gender