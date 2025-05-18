-- 코드를 입력하세요
# SELECT HISTORY_ID, CAR_ID,
# DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
# DATE_FORMAT(END_DATE  , '%Y-%m-%d') AS END_DATE,
# if(DATEDIFF(END_DATE, START_DATE) >= 30, '장기 대여', '단기 대여') as RENT_TYPE
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE START_DATE BETWEEN '2022-09-01' AND '2022-09-30'
# order by -HISTORY_ID

SELECT history_id, car_id, SUBSTRING(start_date, 1,12) as start_date
, SUBSTRING(end_date, 1,12) as end_date,
(case
 when DATE_ADD(start_date, INTERVAL 29 DAY) <= end_date
 then '장기 대여'
 else '단기 대여'
 end
) as RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date >= '2022-09-01' and start_date <= '2022-09-30'
order by HISTORY_ID desc