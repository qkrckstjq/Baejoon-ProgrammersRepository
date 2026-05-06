-- 코드를 입력하세요
SELECT fd.PRODUCT_ID, fd.PRODUCT_NAME, (fd.PRICE * fo.T_AMOUNT) as TOTAL_SALES  from FOOD_PRODUCT fd
left join (
    select PRODUCT_ID, SUM(AMOUNT) as T_AMOUNT from FOOD_ORDER
    where YEAR(PRODUCE_DATE) = "2022" and MONTH(PRODUCE_DATE) = "5"
    group by PRODUCT_ID
) fo
on fd.PRODUCT_ID = fo.PRODUCT_ID
where fo.PRODUCT_ID is NOT NULL
order by TOTAL_SALES desc, fd.PRODUCT_ID asc