# Write your MySQL query statement below

with d as (select distinct(i1.pid), i1.tiv_2016, i1.lat, i1.lon from Insurance i1
left join Insurance i2
on i1.pid != i2.pid and i1.tiv_2015 = i2.tiv_2015
where i2.pid is not null),
ui as (
    select * from Insurance i
    group by i.lat, i.lon
    having count(*) = 1
)
select round(sum(tiv_2016), 2) as tiv_2016 from d
where pid in (select pid from ui)

-- select round(sum(t.s), 2) as tiv_2016 from (select sum(u.tiv_2016) as s from ui u
-- group by u.lat, u.lon
-- having count(*) = 1) t

 
-- select round(sum(t.tiv_2016), 2) as tiv_2016 
-- from (
--     select distinct(u1.pid), u1.tiv_2016 from ui u1
--     left join ui u2
--     on u1.pid != u2.pid and u1.tiv_2015 = u2.tiv_2015
--     where u2.pid is not null
--     ) t


-- select * from ui u1
-- left join ui u2
-- on u1.pid != u2.pid and u1.tiv_2015 = u2.tiv_2015
-- where u2.pid is not null