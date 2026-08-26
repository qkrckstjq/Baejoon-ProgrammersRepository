# Write your MySQL query statement below

-- select w.id from (select *, lag(temperature, 1) over(order by w.recordDate) front from Weather w) w
-- where w.temperature > front


select w1.id from Weather w1
left join Weather w2
on w1.recordDate = (w2.recordDate + interval 1 day)
where w1.temperature > w2.temperature