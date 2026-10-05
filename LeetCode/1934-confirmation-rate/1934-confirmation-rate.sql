# Write your MySQL query statement below
select s.user_id, round(IFNULL(a.confirmation_rate, 0), 2) as confirmation_rate from Signups s
left join (
    select c.user_id, sum(case when c.action = 'timeout' then 0 else 1 end) / count(*) as confirmation_rate from Confirmations c
    group by c.user_id
) a
on s.user_id = a.user_id