-- 코드를 입력하세요
select 
year(sales_date) as YEAR,
month(sales_date) as MONTH,
count(*) as PURCHASED_USERS,
round((count(*) / (select count(*) from USER_INFO where year(joined) = '2021')), 1) as PUCHASED_RATIO
 from 
    (
        select * from online_sale
        group by year(sales_date), month(sales_date), user_id
    ) as o
left join USER_INFO ui
on o.USER_ID = ui.USER_ID
where year(ui.JOINED) = '2021'
group by year(sales_date), month(sales_date)
order by year(sales_date) asc, month(sales_date) asc