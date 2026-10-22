# Write your MySQL query statement below
select 
ae.session_id, 
ae.user_id, 
timestampdiff(minute, min(ae.event_timestamp), max(ae.event_timestamp)) as session_duration_minutes,
sum(case when ae.event_type = 'scroll' then 1 else 0 end) as scroll_count
from app_events ae
group by ae.session_id
having timestampdiff(minute, min(ae.event_timestamp), max(ae.event_timestamp)) > 30 and
sum(case when ae.event_type = 'scroll' then 1 else 0 end) >= 5 and
sum(case when ae.event_type = 'click' then 1 else 0 end) / sum(case when ae.event_type = 'scroll' then 1 else 0 end) < 0.2 and
sum(case when ae.event_type = 'purchase' then 1 else 0 end) = 0
order by scroll_count desc, ae.session_id asc