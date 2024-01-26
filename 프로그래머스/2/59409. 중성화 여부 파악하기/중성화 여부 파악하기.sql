-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
(
    case
    when sex_upon_intake like '%Neutered%' or sex_upon_intake like '%Spayed%'
    then 'O'
    else 'X'
    end
) as 중성화
from ANIMAL_INS
order by ANIMAL_ID
