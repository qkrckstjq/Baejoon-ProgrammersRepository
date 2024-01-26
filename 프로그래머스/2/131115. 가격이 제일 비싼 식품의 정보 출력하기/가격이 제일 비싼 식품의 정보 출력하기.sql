-- 코드를 입력하세요
with maxPrice as (
    SELECT max(PRICE) as maxPrice from FOOD_PRODUCT
)
select * from FOOD_PRODUCT f
where f.price = (select maxPrice from maxPrice )

