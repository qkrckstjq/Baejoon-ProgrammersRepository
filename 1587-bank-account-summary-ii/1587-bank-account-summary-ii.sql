# Write your MySQL query statement below
select * from (
    select u.name, sum(t.amount) as BALANCE from Users u
    inner join Transactions t
    on u.account = t.account
    group by u.account
) a
where a.BALANCE > 10000