# Write your MySQL query statement below
select * from (
    select p.product_id, 'store1' as store, p.store1 as price from Products p 
    union all
    select p.product_id, 'store2' as store, p.store2 as price from Products p
    union all
    select p.product_id, 'store3' as store, p.store3 as price from Products p
) a
where a.price is not null
