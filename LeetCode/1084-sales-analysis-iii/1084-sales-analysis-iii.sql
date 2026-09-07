# Write your MySQL query statement below

with cond as (
    select *, count(*) as cnt from Sales s
    where s.sale_date between date('2019-01-01') and date('2019-03-31')
    group by product_id
),
def as (
    select *, count(*) as cnt from Sales s
    group by s.product_id
)
select p.product_id, p.product_name from def d
inner join cond c
on d.product_id = c.product_id and d.cnt = c.cnt
left join Product p
on d.product_id = p.product_id




