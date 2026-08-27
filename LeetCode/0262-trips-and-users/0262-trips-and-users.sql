# Write your MySQL query statement below
with temp as (
    select * from (
        select t.driver_id, t.status, t.request_at from Trips t
        join Users u1
        on t.client_id = u1.users_id and u1.banned = 'No'
        ) t
    join Users u
    on t.driver_id = u.users_id and u.banned = 'No'
    where t.request_at between '2013-10-01' and '2013-10-03'
)
select t.request_at as 'Day', round(IFNULL(c.cancel, 0) / t.total, 2) as 'Cancellation Rate' 
from (select t.request_at, count(*) as total from temp t group by t.request_at) t
left join (select t.request_at, count(*) as cancel from temp t
    where t.status in ('cancelled_by_driver', 'cancelled_by_client')
    group by t.request_at) c
on t.request_at = c.request_at
where IFNULL(t.total, 0) >= IFNULL(c.cancel, 0)
