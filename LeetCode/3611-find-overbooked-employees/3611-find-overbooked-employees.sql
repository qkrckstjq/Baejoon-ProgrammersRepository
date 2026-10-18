# Write your MySQL query statement below
with temp as (
    select *, sum(m.duration_hours) as total from meetings m
    group by m.employee_id, year(m.meeting_date), week(m.meeting_date, 3)
)

-- select *, count(*) meeting_heavy_weeks from temp t
-- where t.total >= 20
-- group by t.employee_id
-- having meeting_heavy_weeks > 1

select e.employee_id, e.employee_name, e.department, t.meeting_heavy_weeks from employees e
right join (
    select *, count(*) meeting_heavy_weeks from temp t
    where t.total > 20
    group by t.employee_id
    having meeting_heavy_weeks > 1
) t
on e.employee_id = t.employee_id
order by t.meeting_heavy_weeks desc, e.employee_name asc


