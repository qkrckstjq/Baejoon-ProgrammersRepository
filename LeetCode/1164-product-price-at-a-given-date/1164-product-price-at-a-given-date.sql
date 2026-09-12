-- # Write your MySQL query statement below
select p.product_id, IFNULL(t.new_price, 10) as price from (select * from Products group by product_id) p
left join (
    select p.product_id, p.new_price from Products p
    inner join (
        select product_id, MAX(change_date) as change_date from Products p
        where change_date <= DATE('20190816')
        group by p.product_id
    ) t
    on p.product_id = t.product_id and p.change_date = t.change_date
) t
on p.product_id = t.product_id