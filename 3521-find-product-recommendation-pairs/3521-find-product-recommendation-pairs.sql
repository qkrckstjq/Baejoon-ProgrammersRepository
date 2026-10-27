# Write your MySQL query statement below
with q as (
    select pp.*, p1.category from ProductPurchases pp
    left join ProductInfo p1
    on pp.product_id = p1.product_id
),
temp as (
    select pp1.user_id as user_id, pp1.product_id as product1_id, pp2.product_id as product2_id, pp1.category as product1_category, pp2.category as product2_category from q pp1
    left join q pp2
    on pp1.product_id < pp2.product_id and pp1.product_id != pp2.product_id and pp1.user_id = pp2.user_id
    where pp2.product_id is not null
    group by pp1.user_id, product1_id, product2_id
)
select t.product1_id, t.product2_id, t.product1_category, t.product2_category, count(*) as customer_count from temp t
group by t.product1_id, t.product2_id
having count(*) >= 3
order by customer_count desc, t.product1_id, t.product2_id