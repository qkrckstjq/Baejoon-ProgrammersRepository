# Write your MySQL query statement below
select *, 
case
    when (t.x + t.y <= t.z) or (t.x >= t.y + t.z) or (t.x + t.z <= t.y)
    then 'No'
    else 'Yes'
end as triangle
from Triangle t
