# Write your MySQL query statement below
select
s.id,
case 
    when n.student is not null
    then n.student
    else s.student
end as student
from Seat s
left join Seat n
on (s.id MOD 2 = 1 and s.id + 1 = n.id) or (s.id MOD 2 = 0 and s.id - 1 = n.id)
order by s.id asc
