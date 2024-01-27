-- 코드를 입력하세요
# with table1 as (
#     select user_id, product_id, count(product_id) as countALl from online_sale
#     group by product_id, user_id 
#     order by user_id
# )
# select table1.user_id, table1.product_id from table1
# where countALl >= 2
# order by table1.user_id, table1.product_id desc

select user_id, product_id from online_sale
group by user_id, product_id
having count(*) >= 2
order by user_id, product_id desc