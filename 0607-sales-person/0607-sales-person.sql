# Write your MySQL query statement below
with red_order as (
    select com_id from Company
    where name = 'RED'
),
with_red as (
    select sales_id from Orders o
    where o.com_id in (select * from red_order)
)
select s.name from SalesPerson s
where s.sales_id not in (select * from with_red)