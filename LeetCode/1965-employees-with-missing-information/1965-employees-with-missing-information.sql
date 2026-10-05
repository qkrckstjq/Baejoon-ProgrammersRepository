# Write your MySQL query statement below
with full as (
    select e.employee_id, s.employee_id as s_employee_id from Employees e
    left join Salaries s
    on e.employee_id = s.employee_id

    union

    select s.employee_id, e.employee_id as e_employee_id from Employees e
    right join Salaries s
    on e.employee_id = s.employee_id
)
select f.employee_id from full f
where f.s_employee_id is null
order by f.employee_id
