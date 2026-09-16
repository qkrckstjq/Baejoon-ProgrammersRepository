# Write your MySQL query statement below
select q.person_name as person_name from (
    select *, sum(weight) over(order by q.turn rows between unbounded preceding and current row) as nuke from Queue q
    order by q.turn) q
where nuke <= 1000
order by nuke desc
limit 1



