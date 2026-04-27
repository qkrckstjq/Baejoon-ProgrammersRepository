# -- 코드를 입력하세요
SELECT DISTINCT(ch.CAR_ID), 
(case
    when MAX(
        case
        when(DATE(ch.START_DATE) <= DATE("2022-10-16") and DATE(ch.END_DATE) >= DATE("2022-10-16"))
        then 1
        else 0
        end) = 1
    then "대여중"
    else "대여 가능"
end) as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY ch
group by ch.CAR_ID
order by ch.CAR_ID desc

# select * from CAR_RENTAL_COMPANY_RENTAL_HISTORY ch