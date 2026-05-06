-- 코드를 입력하세요
SELECT f.CATEGORY, f.PRICE as MAX_PRICE, f.PRODUCT_NAME from FOOD_PRODUCT f
left join (
    select CATEGORY, MAX(PRICE) as PRICE from FOOD_PRODUCT 
    where CATEGORY in ("과자", "국", "김치", "식용유") 
    group by CATEGORY
) f2
on f.CATEGORY = f2.CATEGORY and f.PRICE = f2.PRICE
where f2.CATEGORY is NOT NULL
order by MAX_PRICE desc
