SELECT 
o.order_ID,
i.Price,
o.Quantity,
i.item_category,
i.item_name,
o.created_at,
a.Address_1,
a.city,
a.zipcode
FROM orders o
LEFT JOIN items i on o.item_id = i.item_id
LEFT JOIN address a on o.add_id = a.add_id;

with stock1 as (SELECT 
S1.item_name,
s1.ingred_id,
s1.ing_name,
s1.ing_weight,
s1.ing_price_USD,
s1.order_quantity,
s1.recipe_quantity,
s1.order_quantity*recipe_quantity as ordered_weight,
s1.ing_price_USD/s1.ing_weight as unit_cost,
(s1.order_quantity*s1.recipe_quantity)*(s1.ing_price_USD/s1.ing_weight)/100 as ingredient_cost

from (select 
o.item_id,
i.sku,
i.item_name,
r.ingred_id,
ing.ing_name,
r.quantity as recipe_quantity,
sum(o.quantity) as order_quantity,
ing.ing_weight,
ing.ing_price_USD
from orders o
left join items i on o.item_id = i.item_id
left join recipe r on i.sku = r.recipe_id
left join ingredient ing on ing.ing_id = r.ingred_id
group by o.item_id, i.sku,i.item_name, r.ingred_id, r.quantity,ing.ing_name, ing.ing_weight, ing.ing_price_USD) S1)

select * FROM stock1
