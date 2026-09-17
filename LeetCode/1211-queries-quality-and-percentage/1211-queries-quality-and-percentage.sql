# Write your MySQL query statement below
select 
q.query_name,
round(AVG(q.rating / q.position), 2) as quality,
round(AVG(case when q.rating < 3 then 1 else 0 end) * 100, 2) as poor_query_percentage
 from Queries q
group by q.query_name