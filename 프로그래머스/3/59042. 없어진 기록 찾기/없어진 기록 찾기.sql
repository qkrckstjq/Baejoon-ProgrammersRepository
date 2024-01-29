-- 코드를 입력하세요
SELECT ao.animal_id, ao.name from animal_outs ao
left join animal_ins ai
on ai.animal_id = ao.animal_id
where ao.datetime is not NULL and ai.datetime is NULL