-- 코드를 입력하세요
SELECT 
YEAR(os.SALES_DATE) as YEAR,
MONTH(os.SALES_DATE) as MONTH,
ui.GENDER,
count(DISTINCT(os.USER_ID)) as USERS
from ONLINE_SALE os
left join USER_INFO ui
on os.USER_ID = ui.USER_ID
where ui.GENDER is not NULL
group by YEAR, MONTH, ui.GENDER
order by YEAR asc, MONTH asc, ui.GENDER asc