-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, ai.NAME from ANIMAL_INS ai
left join ANIMAL_OUTS ao
on ai.ANIMAL_ID = ao.ANIMAL_ID
where ao.ANIMAL_ID is not NULL
order by (ao.DATETIME - ai.DATETIME) desc
limit 2
