# Write your MySQL query statement below
select c.name as Customers from Customers c
left join (select customerId from Orders) o
on c.id = o.customerId
where o.customerId is null