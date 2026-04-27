-- 코드를 입력하세요
SELECT DISTINCT(cr.CAR_ID) from CAR_RENTAL_COMPANY_CAR cr
left join CAR_RENTAL_COMPANY_RENTAL_HISTORY ch
on cr.CAR_ID = ch.CAR_ID
where cr.CAR_TYPE = "세단" and MONTH(DATE(ch.START_DATE)) = 10
order by cr.CAR_ID desc