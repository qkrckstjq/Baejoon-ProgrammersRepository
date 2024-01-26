-- 코드를 입력하세요
SELECT ANIMAL_TYPE, 
(
    case
    when NAME is NULL 
    then 'No name'
    else NAME
    END
),
SEX_UPON_INTAKE from ANIMAL_INS
order by ANIMAL_ID
