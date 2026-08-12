-- 코드를 작성해주세요

select distinct(d.ID), d.EMAIL, d.FIRST_NAME, d.LAST_NAME from DEVELOPERS d
join (
    SELECT *
    FROM SKILLCODES s
    WHERE s.category = 'Front End'
) s
on (d.SKILL_CODE & s.CODE) = s.CODE
order by d.ID asc



