# Write your MySQL query statement below
-- select u.product_id, round(sum(u.units * p.price) / sum(u.units), 2) as average_price from UnitsSold u
-- left join Prices p
-- on u.product_id = p.product_id and u.purchase_date between p.start_date and p.end_date
-- group by u.product_id

select p.product_id, IFNULL(round(sum(IFNULL(u.units, 0) * p.price) / sum(IFNULL(u.units, 0)), 2), 0) as average_price from Prices p
left join UnitsSold u
on u.product_id = p.product_id and u.purchase_date between p.start_date and p.end_date
group by p.product_id