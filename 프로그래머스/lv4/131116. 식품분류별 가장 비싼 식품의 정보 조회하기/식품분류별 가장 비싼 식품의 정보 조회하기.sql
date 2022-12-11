SELECT category, price, product_name
from (
    select category,
    price,
    product_name,
    row_number() over (partition by category order by price desc) as category_price_rank
    from food_product
    where category like '%과자%' or category like '%국%' or category like '%김치%'
or category like '%식용유%') food_product_rank
where category_price_rank = 1
order by price desc