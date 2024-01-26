-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(p.price*os.sales_amount) SALES
from PRODUCT p
inner join OFFLINE_SALE os
on p.product_id = os.product_id
group by p.product_id
order by SALES desc, p.PRODUCT_CODE