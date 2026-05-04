# -- 코드를 입력하세요
select MONTH(c.START_DATE) as MONTH, c.CAR_ID, count(*) as RECORDS from CAR_RENTAL_COMPANY_RENTAL_HISTORY c
left join (SELECT c.CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY c
where c.START_DATE >= '2022-08-01'
  AND c.START_DATE < '2022-11-01'
group by c.CAR_ID
having count(*) >= 5
) e
on c.CAR_ID = e.CAR_ID
where e.CAR_ID is not NULL and (c.START_DATE >= '2022-08-01'
  AND c.START_DATE < '2022-11-01')
group by c.CAR_ID, MONTH(c.START_DATE)
order by MONTH, CAR_ID desc