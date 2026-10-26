# Write your MySQL query statement below
select * from (
    select
    ua.user_id,
    round(avg(case when activity_type = 'free_trial' then ua.activity_duration else null end), 2)  as trial_avg_duration,
    round(avg(case when activity_type = 'paid' then ua.activity_duration else null end), 2) as paid_avg_duration
    from UserActivity ua
    group by ua.user_id
) a
where a.trial_avg_duration is not null and a.paid_avg_duration is not null
order by a.user_id 