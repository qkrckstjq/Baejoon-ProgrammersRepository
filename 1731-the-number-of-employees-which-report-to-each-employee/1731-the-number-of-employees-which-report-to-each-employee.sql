# Write your MySQL query statement below
select e.employee_id, e.name, a.reports_count, a.average_age from Employees e
inner join (
    select e.reports_to, count(*) as reports_count, round(avg(e.age), 0) as average_age from Employees e
    group by reports_to
) a
on e.employee_id = a.reports_to
order by e.employee_id
