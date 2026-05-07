-- 코드를 입력하세요
SELECT c.CART_ID from CART_PRODUCTS c
where c.NAME = "Milk" or c.NAME = "Yogurt"
group by c.CART_ID
having count(DISTINCT(c.NAME)) >= 2
order by c.CART_ID asc