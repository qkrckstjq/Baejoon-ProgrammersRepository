# Write your MySQL query statement below
select a.employee_id, a.department_id from (
    select *, row_number() over(
    partition by e.employee_id
    order by (
    case
        when e.primary_flag = 'Y'
        then 0
        else 1
    end
    )) as rn from Employee e    
) a
where a.rn = 1
