# Write your MySQL query statement below
select e.Department, e.name as Employee, e.salary from (select e.name, e.departmentId, e.salary, d.name as Department from Employee e left join Department d on e.departmentId = d.id) e
left join (select MAX(salary) as salary, departmentId from Employee group by departmentId) m
on e.salary = m.salary and e.departmentId = m.departmentId
where m.salary is not null