-- 코드를 입력하세요
# (SELECT ch.HISTORY_ID, cc.DAILY_FEE, (ch.END_DATE - START_DATE) as dif
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY ch
# left join CAR_RENTAL_COMPANY_CAR cc
# on ch.CAR_ID = cc.CAR_ID
# where cc.CAR_TYPE = "트럭")


SELECT 
    t.HISTORY_ID,
    FLOOR(
        t.DAILY_FEE * t.dif
        * (100 - IFNULL(cp.DISCOUNT_RATE, 0)) / 100
    ) AS FEE
FROM (
    SELECT
        cc.CAR_TYPE,
        ch.HISTORY_ID,
        cc.DAILY_FEE,
        DATEDIFF(ch.END_DATE, ch.START_DATE) + 1 AS dif,
        (case
            when DATEDIFF(ch.END_DATE, ch.START_DATE) + 1 >= 90 
            then "90일 이상"
            when DATEDIFF(ch.END_DATE, ch.START_DATE) + 1 >= 30 
            then "30일 이상"
            when DATEDIFF(ch.END_DATE, ch.START_DATE) + 1 >= 7 
            then "7일 이상"
            else null
        end) as DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY ch
    LEFT JOIN CAR_RENTAL_COMPANY_CAR cc
    ON ch.CAR_ID = cc.CAR_ID
    WHERE cc.CAR_TYPE = '트럭'
) t
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN cp
    ON t.CAR_TYPE = cp.CAR_TYPE
   AND t.DURATION_TYPE = cp.DURATION_TYPE
ORDER BY FEE DESC, t.HISTORY_ID DESC

