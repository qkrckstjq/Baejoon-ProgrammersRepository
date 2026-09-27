# Write your MySQL query statement below
select a.sell_date, count(*) as num_sold, GROUP_CONCAT(a.product order by a.product) as products from (
    select * from Activities a
    group by a.sell_date, a.product
) a
group by a.sell_date
order by a.sell_date
