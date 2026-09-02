# Write your MySQL query statement below

select distinct(e.id),
case
    when e.p_id is null
    then 'Root'
    when e.p_id is not null and c.id is null
    then 'Leaf'
    when e.p_id is not null and c.id is not null
    then 'Inner'
end as type
from Tree e
left join Tree c
on c.p_id = e.id