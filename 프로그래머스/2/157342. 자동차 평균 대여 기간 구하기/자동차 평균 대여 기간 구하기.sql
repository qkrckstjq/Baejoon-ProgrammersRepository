-- 코드를 입력하세요
with table1 as (
    select car_id, round(avg(datediff(end_date,start_date)+1),1) as average 
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    group by car_id
)
select CAR_ID, average AVERAGE_DURATION from table1
where average >= 7
order by average desc, car_id desc

