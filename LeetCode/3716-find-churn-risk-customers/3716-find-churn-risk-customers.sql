# Write your MySQL query statement below
with temp as (
    select 
    *,  
    (case when se.event_type = 'downgrade' then 1 else 0 end) as downgrade_cnt,
    FIRST_VALUE(event_type) over(partition by se.user_id order by se.event_date desc) as last_event,
    FIRST_VALUE(plan_name) over(partition by se.user_id order by se.event_date desc) as last_plan,
    FIRST_VALUE(monthly_amount) over(partition by se.user_id order by monthly_amount desc) as max_amount,
    FIRST_VALUE(monthly_amount) over(partition by se.user_id order by se.event_date desc) as last_amount
    from subscription_events se
)
select 
t.user_id, 
t.last_plan as current_plan, 
t.last_amount as current_monthly_amount,
t.max_amount as max_historical_amount,
DATEDIFF(max(t.event_date), min(t.event_date)) as days_as_subscriber
from temp t
where t.last_event != 'cancel'
group by t.user_id
having 
sum(t.downgrade_cnt) > 0 and
DATEDIFF(max(t.event_date), min(t.event_date)) >= 60 and
t.last_amount / t.max_amount < 0.5
order by days_as_subscriber desc, t.user_id asc