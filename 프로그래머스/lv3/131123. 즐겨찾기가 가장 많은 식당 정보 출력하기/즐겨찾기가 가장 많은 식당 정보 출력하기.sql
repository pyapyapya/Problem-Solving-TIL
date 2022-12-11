SELECT food_type, rest_id, rest_name, favorites
from (
    select food_type
    , rest_id
    , rest_name
    , favorites
    , row_number() over (partition by food_type order by favorites desc) as favorites_rank
    from rest_info 
) r_info
where favorites_rank = 1
order by food_type desc