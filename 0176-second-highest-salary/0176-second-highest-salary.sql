# Write your MySQL query statement below
select MAX(e.salary) as SecondHighestSalary from (
    select salary, DENSE_RANK() over(
        order by salary desc) as d_rank from Employee
        ) e
where e.d_rank = 2