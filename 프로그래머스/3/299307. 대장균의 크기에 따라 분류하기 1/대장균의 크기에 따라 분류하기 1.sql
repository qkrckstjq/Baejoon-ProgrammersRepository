-- 코드를 작성해주세요

select 
ed.ID,
case
    when ed.SIZE_OF_COLONY between 0 and 100
    then "LOW"
    when ed.SIZE_OF_COLONY between 100 and 1000
    then "MEDIUM"
    when ed.SIZE_OF_COLONY > 1000
    then "HIGH"
end as SIZE
from ECOLI_DATA ed