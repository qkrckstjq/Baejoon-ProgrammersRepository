-- 코드를 입력하세요

select cc.CAR_ID, cc.CAR_TYPE, FLOOR(cc.DAILY_FEE * 30 * 
        (1 - CAST(REPLACE(cp.DISCOUNT_RATE, '%', '') AS DECIMAL(5,2)) / 100)
    ) AS FEE from CAR_RENTAL_COMPANY_CAR cc 
# left join CAR_RENTAL_COMPANY_RENTAL_HISTORY ch
# on ch.CAR_ID = cc.CAR_ID
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN cp
on cc.CAR_TYPE = cp.CAR_TYPE
where NOT EXISTS (
        SELECT 1
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
        WHERE h.CAR_ID = cc.CAR_ID
          AND h.START_DATE <= '2022-11-30'
          AND h.END_DATE >= '2022-11-01'
  ) and
(cp.DURATION_TYPE = "30일 이상") and 
(cc.DAILY_FEE * 30 * (1 - CAST(REPLACE(cp.DISCOUNT_RATE, '%', '') AS DECIMAL(5,2)) / 100)) BETWEEN 500000 AND 1999999
order by FEE desc, CAR_TYPE asc, CAR_ID desc