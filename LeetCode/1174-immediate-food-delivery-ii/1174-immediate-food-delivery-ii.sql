-- # Write your MySQL query statement below

-- with d as (select d.customer_id, d.order_date, d.customer_pref_delivery_date from (
--     select 
--     *,
--     rank() over(
--         partition by d.order_date
--         order by d.order_date) as d_rank from Delivery d
-- ) d
-- where d.d_rank = 1
-- )

select round(sum(case when d.order_date = d.customer_pref_delivery_date then 1 else 0 end) / count(*) * 100, 2) as immediate_percentage from (
    select 
    *,
    rank() over(
        partition by d.customer_id
        order by d.order_date) as d_rank from Delivery d
) d
where d.d_rank = 1


-- select round(sum(d.p) / count(*), 2) as immediate_percentage from (
--     select d.customer_id, sum(d.n) / count(*) * 100 as p from (
--     select 
--     d.customer_id,
--     case
--         when d.order_date = d.customer_pref_delivery_date
--         then 1
--         else 0
--     end as n
--     from Delivery d
--     where d.order_date <= d.customer_pref_delivery_date
--     ) d
--     group by d.customer_id
-- ) d


-- select d.customer_id, d.order_date, d.customer_pref_delivery_date from (
--     select 
--     *,
--     rank() over(
--         partition by d.customer_id
--         order by d.order_date) as d_rank from Delivery d
-- ) d
-- where d.d_rank = 1