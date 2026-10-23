# Write your MySQL query statement below
select 
ro.customer_id, 
count(*) as total_orders,
round(sum(
    case
        when hour(ro.order_timestamp) between 11 and 13 or hour(ro.order_timestamp) between 18 and 20
        then 1 
        else 0
    end
) / count(*), 2) * 100 as peak_hour_percentage,
round(avg(ro.order_rating), 2) as average_rating
from restaurant_orders ro
group by ro.customer_id
having
count(*) >= 3 and
round(sum(
    case
        when hour(ro.order_timestamp) between 11 and 13 or hour(ro.order_timestamp) between 18 and 20
        then 1 
        else 0
    end
) / count(*), 2) * 100 >= 60 and
round(avg(ro.order_rating), 2) >= 4.0 and
sum(
    case
        when ro.order_rating is not null
        then 1 
        else 0
    end
) / count(*) >= 0.5
order by average_rating desc, ro.customer_id desc