-- 코드를 작성해주세요
select e.ID from (select e.ID, e.PARENT_ID from (
    select * from ECOLI_DATA e
    where e.PARENT_ID is null
    ) as g1
    join ECOLI_DATA e
    on e.PARENT_ID = g1.ID) as g2
join ECOLI_DATA e
on e.PARENT_ID = g2.ID
order by e.ID asc