# Write your MySQL query statement below

select l.num as ConsecutiveNums from (select 
        num,
        LAG(num, 1) over() as prev,
        LEAD(num, 1) over() as next
        from Logs) l
where l.num = l.prev and l.num = l.next
group by l.num

