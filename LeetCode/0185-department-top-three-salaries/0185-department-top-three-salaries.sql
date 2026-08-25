# Write your MySQL query statement below
select d.name as department, e.name as Employee, e.salary from (select *, DENSE_RANK() over(
    partition by e.departmentId
    order by e.salary desc
) as d_rank from Employee e) e
left join Department d
on e.departmentId = d.id
where e.d_rank in (1, 2, 3)
