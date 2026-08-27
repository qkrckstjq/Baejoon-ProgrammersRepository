# Write your MySQL query statement below
select e.name from Employee e
join (
    select e.managerId from Employee e
    group by e.managerId
    having count(*) >= 5
    ) m
on e.id = m.managerId

-- select e.managerId from Employee e
--     group by e.managerId
--     having count(*) >= 5