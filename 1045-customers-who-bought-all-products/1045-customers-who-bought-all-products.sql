# Write your MySQL query statement below
with filter as (
select * from Customer c
left join Product p
on c.product_key = p.product_key
where p.product_key is not null
),
cnt_a as (select customer_id, count(distinct(product_key)) as cnt from Customer group by customer_id)
select customer_id from cnt_a
where cnt = (select count(*) from Product)
