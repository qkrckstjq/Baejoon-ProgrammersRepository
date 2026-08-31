-- -- # Write your MySQL query statement below
with sta as (
    select * from Stadium
    order by id asc
),
cond as (
    select 
    *,
    LAG(s1.id, 1) over () as s2_id,
    LAG(s1.people, 1) over () as s2_people,
    LEAD(s1.id, 1) over () as s3_id,
    LEAD(s1.people, 1) over () as s3_people
    from sta s1
),
result as (
    select * from cond c
    where c.people >= 100 and s2_id is not null and s2_people >= 100 and s3_id is not null and s3_people >= 100
)
select distinct(s.id) as id, s.visit_date, s.people from Stadium s
join result c
on s.id = c.id or s.id = c.s2_id or s.id = c.s3_id
order by s.id

-- select 
--     *,
--     LAG(s1.id, 1) over (),
--     LEAD(s1.id, 1) over ()
--     from stadium s1