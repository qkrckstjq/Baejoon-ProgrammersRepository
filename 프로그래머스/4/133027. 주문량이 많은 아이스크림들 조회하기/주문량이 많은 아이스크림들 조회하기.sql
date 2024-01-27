-- 코드를 입력하세요
with table1 as (
    SELECT f.flavor,
    (sum(f.total_order)+sum(j.total_order)) as sumAll
    from first_half f
    inner join july j
    on f.flavor = j.flavor
    group by f.flavor
)
select flavor from table1 t
order by t.sumAll desc
limit 3


