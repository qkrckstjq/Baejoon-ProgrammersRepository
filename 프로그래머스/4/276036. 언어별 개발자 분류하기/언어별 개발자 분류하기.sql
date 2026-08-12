select * from (
select 
CASE
    when max(
        case
            when s.CATEGORY = 'Front End'
            then 1
            else 0
        end) &
        max(
        case
            when s.NAME = 'Python'
            then 1
            else 0
        end) = 1
    then 'A'
    when max(
        case
            when s.NAME = 'C#'
            then 1
            else 0
        end
        ) = 1
    then 'B'
    when max(
        case
            when s.CATEGORY = 'Front End'
            then 1
            else 0
        end
        ) = 1
    then 'C'
END as GRADE,
d.ID,
d.EMAIL
from developers d
join SKILLCODES s
on (d.SKILL_CODE & s.CODE) = s.CODE
group by d.ID
order by GRADE asc, d.ID asc
) as t
where GRADE is not null