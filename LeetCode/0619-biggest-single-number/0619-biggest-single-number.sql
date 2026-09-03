# Write your MySQL query statement below
select max(n.num) as num from (
    select n.num as num from MyNumbers n
    group by num
    having count(*) = 1
    order by n.num desc
    limit 1
    ) n