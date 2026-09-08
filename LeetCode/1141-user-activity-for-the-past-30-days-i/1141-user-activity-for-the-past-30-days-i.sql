# Write your MySQL query statement below
select c.activity_date as day, count(*) as active_users from 
(
    select * from Activity a
    where a.activity_date between date('2019-06-28') and date('2019-07-27')
    group by a.activity_date, a.user_id
) c
group by c.activity_date
order by day

-- a.activity_date as day, count(*) as active_users

-- select * from Activity a
-- where a.activity_date between date('2019-07-01') and date('2019-07-31')
-- group by a.activity_date, a.user_id
-- group by a.activity_date, a.user_id
