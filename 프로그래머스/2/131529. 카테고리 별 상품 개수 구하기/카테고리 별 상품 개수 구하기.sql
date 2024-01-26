-- 코드를 입력하세요
SELECT SUBSTRING(product_code,1,2) CATEGORY, count(*) PRODUCTS from PRODUCT
group by SUBSTRING(product_code,1,2)
order by SUBSTRING(product_code,1,2)