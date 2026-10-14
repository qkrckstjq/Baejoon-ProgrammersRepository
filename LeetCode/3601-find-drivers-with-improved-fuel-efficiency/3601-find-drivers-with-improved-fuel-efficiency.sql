# Write your MySQL query statement below
select 
d.driver_id,
d.driver_name,
ROUND(a.first_half_avg, 2) as first_half_avg,
ROUND(a.second_half_avg, 2) as second_half_avg,
ROUND(a.second_half_avg - a.first_half_avg, 2) as efficiency_improvement 
from
drivers d
left join (
    select
    t.driver_id,
    AVG(
        case
            when MONTH(t.trip_date) <= 6
            then (t.distance_km / t.fuel_consumed)
            else null
        end
    ) as first_half_avg,
    AVG(
        case
            when MONTH(t.trip_date) > 6
            then (t.distance_km / t.fuel_consumed)
            else null
        end
    ) as second_half_avg
    from trips t
    group by t.driver_id, YEAR(t.trip_date)
) a
on d.driver_id = a.driver_id
where a.second_half_avg > a.first_half_avg
order by efficiency_improvement desc, d.driver_name