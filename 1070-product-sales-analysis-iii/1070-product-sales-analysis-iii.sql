# Write your MySQL query statement below
select s.product_id, s.year as first_year, s.quantity, s.price from (select *, rank() over(partition by product_id order by year) as d_rank from Sales s) s
where d_rank = 1