# Write your MySQL query statement below
select * from products p
where regexp_like(p.description, '(^|\\s)SN[0-9]{4}-[0-9]{4}(\\s|$)', 'c')
order by p.product_id